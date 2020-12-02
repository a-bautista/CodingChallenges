from Vehicle import Vehicle
class Bus(Vehicle):

    # override the method with super
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        normal_fare = super().fare()
        return (normal_fare*0.1)+normal_fare

