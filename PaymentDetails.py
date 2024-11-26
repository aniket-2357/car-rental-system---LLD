from datetime import datetime
from enum import Enum

class PaymentMode(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    UPI = "UPI"
    CASH = "Cash"
    # Add other payment modes as necessary

class PaymentDetails:
    def __init__(self, payment_id, amount_paid, date_of_payment, is_refundable, payment_mode):
        self.payment_id = payment_id
        self.amount_paid = amount_paid
        self.date_of_payment = date_of_payment
        self.is_refundable = is_refundable
        self.payment_mode = payment_mode

# Example usage:
payment_details = PaymentDetails(1, 100, datetime.now(), True, PaymentMode.CREDIT_CARD)
