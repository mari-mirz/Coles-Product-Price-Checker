from bs4 import BeautifulSoup
import requests
import smtplib


class Coles:
    def __init__(self, my_email, my_password, email_list):
        self.my_email = my_email
        self.my_password = my_password
        self.email_list = email_list

    def get_products(self, my_email, my_password, email_list):
        # scrape coles website
        response = requests.get(
            url="https://www.coles.com.au/browse/pantry/health-foods-sports-nutrition-diet/nutrition-powders?filter_Special"
                "=all&page=1")
        content = response.text
        soup = BeautifulSoup(content, "html.parser")

        # get product names
        products_raw = soup.find_all('h2', attrs={"class": "product__title"})
        products = []

        for product in products_raw:
            products.append(product.get_text())

        # get product prices
        costs_raw = soup.find_all('span', attrs={"class": "price__value"})

        costs = []

        for cost in costs_raw:
            costs.append(cost.get_text())

        del costs[::2]

        # combine products and costs list into dictionary
        special_items = {}

        for product in products:
            for cost in costs:
                special_items[product] = cost
                costs.remove(cost)
                break

        # format into text
        string = ""

        def create_text(dictionary, string):
            for element in dictionary.keys():
                string += f"{element} : {dictionary[element]}\n\n"
            return string

        # send email
        for email in email_list:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject: Weekly Health Supplement Specials \n\n\n "
                        f"|These are this week's specials at Coles for muscle supplements| \n\n "
                        f"{create_text(special_items, string)}"
                )
