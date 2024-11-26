# // package LowLevelDesign.LLDCarRentalSystem;

# // public class Payment {

# //     public void payBill(Bill bill) {
# //         //do payment processing and update the bill status;
# //     }
# // }
class Payment:
    def pay_bill(self, bill):
        # do payment processing and update the bill status
        self.process_payment(bill.total_bill_amount)
        bill.is_bill_paid=True

    def process_payment(self, amount):
        # simulate payment processing
        print(f"Processing payment of ${amount}...")