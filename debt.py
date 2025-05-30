import math
class Debt:
    def calculate_payoff(self, balance, apr, payment):
        rate = apr/100
        payment_per_year = 12
        
        monthly_interest = balance * (rate/payment_per_year)
        if payment <= monthly_interest:
            return "payment too small"
        
        numerator = -math.log(1-(rate*balance)/(payment*payment_per_year))
        denominator = payment_per_year*math.log(1+(rate/payment_per_year))
        time_years = numerator/denominator

        return time_years
    
    def monthly_payment_made(self, balance, apr):
        daily_apr = (apr/100)/365
        interest_on_principle = round(balance * (daily_apr * 30),2)
        principle_due = round(balance*.01, 2)
        return [interest_on_principle, principle_due]


class CreditCard(Debt):

    def __init__(self, card_name: str, balance, apr, due_date):
        self.debt_type = "credit".upper()
        self.card_name = card_name.upper()
        self.balance = float(balance)
        self.APR = float(apr)
        self.due_date = int(due_date)
    
    def __str__(self):
        return self.debt_type+ " - " + self.card_name
    
    def storage_helper(self):
        return list(vars(self).values())
    
    def type_file_store(self):
        return ",".join([self.debt_type, self.card_name, str(self.balance), str(self.APR), str(self.due_date)])
    
    def monthly_payment_made(self, payment):
        interest,principle = super().monthly_payment_made(self.balance, self.APR)
        while payment >= (interest+principle):
            self.balance = self.balance - (payment-interest)
            print(self.balance)
            return
        print("Payment not enough")

    def add_charge(self, charge):
        self.balance += charge

class Loan(Debt):

    def __init__(self, loan_name: str, balance, apr, due_date, min_payment):
        self.debt_type = "loan"
        self.loan_name = loan_name.upper()
        self.balance = float(balance)
        self.APR = float(apr)
        self.due_date = int(due_date)
        self.min_payment = float(min_payment)
    
    def calculate_payoff(self, payment):
        if payment == 0:
            payment = self.min_payment
        return super().calculate_payoff(self.balance, self.APR, payment)
    
    def monthly_payment_made(self, payment):
        interest, principle = super().monthly_payment_made(self.balance, self.APR)
        while payment >= interest+principle:
            self.balance = self.balance - (payment - interest)
            print(self.balance)
            return
        print("Payment not adequate")

    def __str__(self):
        return [self.debt_type, self.loan_name, self.balance, self.APR, self.due_date, self.min_payment]
    
    def type_file_store(self):
        return ",".join([self.debt_type, self.loan_name, str(self.balance), str(self.APR), str(self.due_date), str(self.min_payment)])

