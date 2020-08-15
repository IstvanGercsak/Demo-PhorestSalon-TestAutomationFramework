# Test data
class Card:
    def __init__(self, cardholder_name, zip_code, card_number, valid_til, cvc):
        self.cardholder_name = cardholder_name
        self.zip_code = zip_code
        self.card_number = card_number
        self.valid_til = valid_til
        self.cvc = cvc


class Customer:
    def __init__(self, email_address, first_name, last_name):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
