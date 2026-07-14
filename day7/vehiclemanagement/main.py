from car import Car
from EV import EV
from polynorphism import Overriding_demo

#create ogject for the class
car1 = Car("Toyota", "Camry", 2020)
ev1 = EV("Tesla", "Model 3", 2021, 75)

car1.set_owner("Alice")
print(car1.get_owner())  # Output: Alice

# Call methods on the objects
car1.start_engine()
car1.show_info()

ev1.show_info()
ev1.start_engine()
ev1.charge_battery()

Overriding_demo()