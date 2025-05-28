class Debt():
    def calculate_payments(self, balance, apr):
        pass
    def payment_made(self):
        pass
    def add_balance(self):
        pass


class CreditCard(Debt):
    card_name = ""
    balance = 0
    APR = 0

    def __init__(self, card_name, balance, apr):
        self.card_name = card_name
        self.balance = float(balance)
        self.APR = apr

class Loan(Debt):
    loan_name = ""
    balance = 0
    APR = 0
    loan_type = ""

