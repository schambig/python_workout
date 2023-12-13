#!/urs/bin/python3
from pay import Pay


class PayPal(Pay):
    def __init__(self, email):
        self.email = email

    
    def make_pay(self, quantity):
        payment_info = super().make_pay(quantity)
        payment_info['platform'] = 'PayPal'
        payment_info['email'] = self.email
        return payment_info
