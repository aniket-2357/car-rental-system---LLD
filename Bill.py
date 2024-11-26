from Reservation import Reservation
class Bill:
    def __init__(self, reservation):
        self.reservation = reservation
        self.total_bill_amount = self.compute_bill_amount()
        self.is_bill_paid = False

    def compute_bill_amount(self):
        return 100.0

# Assuming the Reservation class is defined somewhere else in the system
# Example usage:
# reservation = Reservation()  # This would be your Reservation object
# bill = Bill(reservation)
