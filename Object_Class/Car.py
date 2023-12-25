class Car:
    name = ""
    color = ""

    def start(self):
        print("Starting the engine")

# Car.name = "Axio"
# Car.color = "Black"

# print("Name of the car", Car.name)
# print("Color of the car", Car.color)

# Car.start()
# print(dir(Car))
        
#*************Create a class "obejct" *******************

my_car = Car()
my_car.name = "Allion"
my_car.color = "red"

print(my_car.name)
print("My car color is", my_car.color)

my_car.start()