from oopcoffeemaker import CoffeeMaker
from oopcoffeemenu import MenuItem, Menu
from oopcoffeemoneymachine import MoneyMachine
import sys

drink = Menu()
coffee_choice = CoffeeMaker()
coffee_price = MoneyMachine()
options = Menu()

while True: #redo == 'yes'

    user_choice = input(f"What would you like? {options.get_items()}: ").lower()

    

    if user_choice == 'off':
        sys.exit()


    elif user_choice == 'report':
        coffee_choice.report()
        coffee_price.report()
        continue

    beverage = drink.find_drink(user_choice)
    if beverage is None:
         continue

    elif beverage:
      if coffee_choice.is_resource_sufficient(beverage) and coffee_price.make_payment(beverage.cost):
         print(f"Allow us prepare your {user_choice} coffee")
         coffee_choice.make_coffee(beverage)

      redo = input ("Do you want to make another order? (yes/no): ").lower()
      if redo == 'yes':
          continue
      else:
          break

      
    

