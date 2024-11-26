class VehicleRentalSystem:
    def __init__(self, stores, users):
        self.store_list = stores
        self.user_list = users

    def get_store(self, location):
        # Based on location, filter out the Store from store_list.
        # For simplicity, just return the first store in the list.
        return self.store_list[0]