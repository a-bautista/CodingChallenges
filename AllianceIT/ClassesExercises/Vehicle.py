class Vehicle(object):
    # class attribute
    color = 'White'

    def __init__(self, model, type, mileage, max_speed):
        self.model = model
        self.type = type
        self.mileage = mileage
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of a {self.type} is {self.capacity}"

    def fare(self):
        return self.capacity * 100