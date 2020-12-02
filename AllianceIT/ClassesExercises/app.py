# Pycharm marks this as an error but it isn't at all
from Vehicle import Vehicle
from Bus import Bus

def main():

    kia = Vehicle('sportage','SUV',133000, 200)
    school_bus = Bus('Volvo', 'SchoolBus', 100000, 35)
    school_bus.seating_capacity(20)

    print(kia.mileage)
    print(school_bus.mileage)
    print(school_bus.seating_capacity())
    print(school_bus.color)
    print(school_bus.fare())

    # Exercise Question 8: Determine if School_bus is also an instance of the Vehicle class
    print(isinstance(school_bus, Bus))

if __name__ == "__main__":
    main()