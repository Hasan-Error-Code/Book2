class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
    def start(self):
        # print("name: ", self.name)
        # print("color: ", self.color)
        print("Starting the engine")

# my_car1 = Car("Corolla", "White")
# Car.start(my_car1)
# my_car2 = Car("Premio", "Red")
# Car.start(my_car2)
# my_car3 = Car("Allion", "Blue")
# Car.start(my_car3)
        
car = Car("Corolla", 'White')
car.year = 2023
print(car.name, car.color, car.year)