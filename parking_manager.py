from pricing import HourlyStrategy

class ParkingManager:
    def __init__(self, total_spaces=300):
        self.total_spaces = total_spaces
        self.occupied_spaces = {}
        self.pricing_strategy = HourlyStrategy()

    def enter_vehicle(self, vehicle, entry_time):
        if len(self.occupied_spaces) < self.total_spaces:
            self.occupied_spaces[vehicle.license_plate] = entry_time
            return True
        return False

    def exit_vehicle(self, vehicle, exit_time):
        if vehicle.license_plate in self.occupied_spaces:
            entry_time = self.occupied_spaces.pop(vehicle.license_plate)
            hours_parked = exit_time - entry_time
            fee = self.pricing_strategy.calculate_fee(hours_parked)
            return fee
        return 0
