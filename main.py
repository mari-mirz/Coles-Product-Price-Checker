from coles import Coles

MY_EMAIL = "myemail@email.com"
MY_PASSWORD = "password"
EMAILS = [
    "email1@email.com",
    "email2@email.com"
    ]

coles = Coles(my_email=MY_EMAIL, my_password=MY_PASSWORD, email_list=EMAILS)
coles.get_products(my_email=MY_EMAIL, my_password=MY_PASSWORD, email_list=EMAILS)
