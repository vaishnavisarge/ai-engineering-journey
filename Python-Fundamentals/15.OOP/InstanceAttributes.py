# Instance attributes are variables that belong to individual objects.
# They store information specific to each object.
# Usually, we create them using self inside __init__().

class ElectricityMeter:

    def __init__(self, house, units):
        self.house = house
        self.units = units

    def bill(self):
        amount = self.units * 8
        print(self.house, "Bill:", amount)


house1 = ElectricityMeter("House A", 120)
house2 = ElectricityMeter("House B", 250)

house1.bill()
house2.bill()


