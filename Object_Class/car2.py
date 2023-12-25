# class Car:
#     name = ""
#     color = ""
    
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def start(self):
#         print("Starting the Engine")
    
# my_car = Car("Corolla", "White")
# print(my_car.name)
# print(my_car.color)
# my_car.start()

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
    def start(self):
        print("Starting car Engine")
        
my_car = Car("Corolla", "White")
print(my_car.name)
print(my_car.color)
my_car.start()