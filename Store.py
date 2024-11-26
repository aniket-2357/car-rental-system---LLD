from VehicleInventoryManagement import VehicleInventoryManagement
from Reservation import Reservation
from User import User
from Product.Car import Car
from Location import Location
class Store:
    def __init__(self, store_id=None, store_location=None):
        self.store_id = store_id
        self.inventory_management = None
        self.store_location = store_location
        self.reservations = []

    def get_vehicles(self, vehicle_type):
        return self.inventory_management.get_vehicles()

    def set_vehicles(self, vehicles):
        self.inventory_management = VehicleInventoryManagement(vehicles)

    def create_reservation(self, vehicle, user):
        reservation = Reservation()
        reservation.create_reserve(user, vehicle)
        self.reservations.append(reservation)
        return reservation

    def complete_reservation(self, reservation_id):
        # take out the reservation from the list and call complete the reservation method.
        print('Complete the reservation method')
        return True

# Example usage:
store = Store(1, Location(403012, "Bangalore", "Karnataka", "India"))
vehicles = [Car(), Car()]
store.set_vehicles(vehicles)
user = User()
reservation = store.create_reservation(vehicles[0], user)
print(store.complete_reservation(reservation.reservation_id))
