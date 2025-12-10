# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"

# my_Car = Car("toyota","corolla")
# print(my_Car.brand)
# print(my_Car.model)
# print(my_Car.full_name())

# my_new_car = Car("tata","safari")
# print(my_new_car.model)

# -------------------------------
# inheritance

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
# my_tesla = ElectricCar("tesla","model s","85kwh")
# print(my_tesla.full_name())

#-----------------------------------------------------------

#encapsulation
class Car:
    def __init__(self, brand):
        self.__brand = brand  #now it's private by __brand variable

    def get_brand(self):
        return self.__brand + "!"

my_car = Car("Tesla")
print(my_car.get_brand())  # works
print(my_car.__brand)      # error Encapsulated, not accessible directly
