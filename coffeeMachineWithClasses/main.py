from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()  # menu object
coffeMachine = CoffeeMaker()  # coffee machine object
moneyMachine = MoneyMachine()  # payment processing object

while True:
    userCoffee = input("What would you like? (espresso/latte/cappuccino) (type 'report' to see machine resources or 'off' to turn machine off): ")

    if userCoffee == "off":
        print("Coffee machine turned off.")
        break
    elif userCoffee == "report":  # show available resources in machine
        coffeMachine.report()
    elif userCoffee == 'espresso' or userCoffee == 'latte' or userCoffee == 'cappuccino':  # user wants coffee
        coffeeItem = menu.find_drink(userCoffee)  # coffee that the user wants
        # check if there are enough resources to make user's coffee and if user has enough money for coffee they want
        if coffeMachine.is_resource_sufficient(coffeeItem) and moneyMachine.make_payment(coffeeItem.cost):  
            coffeMachine.make_coffee(coffeeItem)
            
            