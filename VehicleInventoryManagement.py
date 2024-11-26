class VehicleInventoryManagement:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def get_vehicles(self):
        # Filtering logic can be added here if needed
        return self.vehicles

    def set_vehicles(self, vehicles):
        self.vehicles = vehicles

# Example usage:
# vehicles = [Car(), Car()]
# vehicle_inventory = VehicleInventoryManagement(vehicles)
# vehicle_inventory.get_vehicles()
# vehicle_inventory.set_vehicles([Car(), Car(), Bike()])
# vehicle_inventory.get_vehicles()
