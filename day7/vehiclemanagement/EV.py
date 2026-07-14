from car import Car


class EV(Car):
    def __init__(self, brand, model, year, battery_capacity, owner=None):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity  # Additional attribute for electric vehicles
        if owner is not None:
            self.set_owner(owner)

    def start_engine(self):
        print(f"The electric engine of the {self.brand} {self.model} is starting silently.")

    def charge_battery(self):
        print(f"The battery of the {self.brand} {self.model} is charging. Capacity: {self.battery_capacity} kWh.")