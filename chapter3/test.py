class Car():

    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading()
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def odometer_reading(self):
        print('haha')

my_used_car = Car('bens', 's400', '2013')
