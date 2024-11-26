from datetime import datetime
from enum import Enum

# class VehicleType(Enum):
#     SEDAN = "SEDAN"
#     SUV = "SUV"
#     HATCHBACK = "HATCHBACK"
#     MOTORCYCLE = "MOTORCYCLE"

# class Status(Enum):
#     ACTIVE = "ACTIVE"
#     INACTIVE = "INACTIVE"

class Vehicle:
    def __init__(self):
        self.vehicle_id = None
        self.vehicle_number = None
        self.vehicle_type = None
        self.company_name = None
        self.model_name = None
        self.km_driven = None
        self.manufacturing_date = None
        self.average = None
        self.cc = None
        self.daily_rental_cost = None
        self.hourly_rental_cost = None
        self.no_of_seat = None
        self.status = None

    # Getters
    def get_vehicle_id(self):
        return self.vehicle_id

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_company_name(self):
        return self.company_name

    def get_model_name(self):
        return self.model_name

    def get_km_driven(self):
        return self.km_driven

    def get_manufacturing_date(self):
        return self.manufacturing_date

    def get_average(self):
        return self.average

    def get_cc(self):
        return self.cc

    def get_daily_rental_cost(self):
        return self.daily_rental_cost

    def get_hourly_rental_cost(self):
        return self.hourly_rental_cost

    def get_no_of_seat(self):
        return self.no_of_seat

    def get_status(self):
        return self.status

    # Setters
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_vehicle_number(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_model_name(self, model_name):
        self.model_name = model_name

    def set_km_driven(self, km_driven):
        self.km_driven = km_driven

    def set_manufacturing_date(self, manufacturing_date):
        self.manufacturing_date = manufacturing_date

    def set_average(self, average):
        self.average = average

    def set_cc(self, cc):
        self.cc = cc

    def set_daily_rental_cost(self, daily_rental_cost):
        self.daily_rental_cost = daily_rental_cost

    def set_hourly_rental_cost(self, hourly_rental_cost):
        self.hourly_rental_cost = hourly_rental_cost

    def set_no_of_seat(self, no_of_seat):
        self.no_of_seat = no_of_seat

    def set_status(self, status):
        self.status = status
