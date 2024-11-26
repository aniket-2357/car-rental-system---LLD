from enum import Enum

class PaymentMode(Enum):
    CASH = 1
    ONLINE = 2

# Example usage
mode = PaymentMode.CASH

if mode == PaymentMode.CASH:
    print("Payment mode is cash.")
elif mode == PaymentMode.ONLINE:
    print("Payment mode is online.")
