from datetime import datetime
from ReservationType import ReservationType
from ReservationStatus import ReservationStatus
from User import User
from Product.Vehicle import Vehicle
from Location import Location

class Reservation:
    def __init__(self):
        self.reservation_id = None
        self.user = None
        self.vehicle = None
        self.booking_date = None
        self.date_booked_from = None
        self.date_booked_to = None
        self.from_timestamp = None
        self.to_timestamp = None
        self.pick_up_location = None
        self.drop_location = None
        self.reservation_type = None
        self.reservation_status = None
        self.location = None

    def create_reserve(self, user, vehicle):
        # Generate new id (In a real-world scenario, this would be generated dynamically)
        self.reservation_id = 12232
        self.user = user
        self.vehicle = vehicle
        self.reservation_type = ReservationType.DAILY
        self.reservation_status = ReservationStatus.SCHEDULED
        self.booking_date = datetime.now()

        return self.reservation_id

    # Add other CRUD operations as needed

# Example usage
user = User()
vehicle = Vehicle()
location = Location(12345,'Hingoli','Maharashtra',"India")

reservation = Reservation()
reservation_id = reservation.create_reserve(user, vehicle)

print(f"Reservation created with ID: {reservation_id}")
