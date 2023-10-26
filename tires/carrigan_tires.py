from tires.tires import Tires


class CarrigranTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(tire >= 0.9 for tire in self.tire_wear)
