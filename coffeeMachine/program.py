from ast import While
from machineData import MENU, resources

def printResources():  # prints correct formatting for each key value pair
    for x, y in resources.items():  # iterate through each dictionary key value pair
        if x == 'water' or x == 'milk':
            print(f"{x.capitalize()}: {y}ml")
        elif x == 'coffee':
            print(f"{x.capitalize()}: {y}g")
        else:  # only other option is money
            print(f"{x.capitalize()}: ${y}")

# do math of total coins user inserted into machine and see if they have enough to buy coffee they want
def calculateCoins(userCoffeeChoice, userQuarters, userDimes, userNickels, userPennies):  
    userMoney = 0  # total money user has
    userCoffeeCost = MENU[userCoffeeChoice]['cost']  # cost of coffee user wants

    while True:  # do while still money left to calculate
        if userQuarters or userDimes or userNickels or userPennies:
            if userQuarters:
                userMoney += .25
                userQuarters -= 1  # remove coin
            elif userDimes:
                userMoney += .1
                userDimes -= 1
            elif userNickels:
                userMoney += .05
                userNickels -= 1
            else:  # only pennies left
                userMoney += .01
                userPennies -= 1
        else:  # no money left so end loop
            break

    userMoney = round(userMoney, 2)

    if userMoney > userCoffeeCost:  # if user has more money then the cost of item then give them change
        userMoney = round(userMoney - userCoffeeCost, 2)
        print(f"Here is ${userMoney} in change.\nHere is your {userCoffeeChoice} Enjoy!")
    elif userMoney < userCoffeeCost:  # user does not have enough money so inform them they need more money
        print(f"Sorry, you need more money to buy this item")
    else:  # user has exact amount of money so only give them item
        print(f"Here is your {userCoffeeChoice} Enjoy!")

def enoughResources(userCoffee):  # see if the machine has enough resources to make requested item
    if resources['water'] >= MENU[userCoffee]['ingredients']['water'] and resources['milk'] >= MENU[userCoffee]['ingredients']['milk'] and resources['coffee'] >= MENU[userCoffee]['ingredients']['coffee']:
        updateResources(userCoffee)  # take away specified resources from machine
        return True
    else:  # not enough resources so inform user
        if resources['water'] < MENU[userCoffee]['ingredients']['water']:
            lowResource = 'water'
        elif resources['milk'] < MENU[userCoffee]['ingredients']['milk']:
            lowResource = 'milk'
        else:
            lowResource = 'coffee'
            
        print(f"Sorry, there is not enough {lowResource}.")
        return False

def updateResources(userCoffee):  # updates resources available in the machine
    resources['water'] -= MENU[userCoffee]['ingredients']['water']  # use these resources to make coffee and remove them from machine
    resources['milk'] -= MENU[userCoffee]['ingredients']['milk']
    resources['coffee'] -= MENU[userCoffee]['ingredients']['coffee']
    resources['money'] += MENU[userCoffee]['cost']  # add funds to machine 

while True:
    userCoffee = input("What would you like? (espresso/latte/cappuccino) (type 'report' to see machine resources or 'off' to turn machine off): ")

    if userCoffee == "off":
        print("Coffee machine turned off.")
        break
    elif userCoffee == "report":  # show available resources in machine
        printResources()
    elif userCoffee == 'espresso' or userCoffee == 'latte' or userCoffee == 'cappuccino':  # user wants coffee
        if enoughResources(userCoffee):  # check if there are enough resources to make user's coffee
            print("Please insert coins.")
            userQuarters = int(input("How many quarters?: "))  # get money from user
            userDimes = int(input("How many dimes?: "))
            userNickels = int(input("How many nickles?: "))
            userPennies = int(input("How many pennies?: "))
            # see if user has enough money for coffee they want
            userCoffeeResult = calculateCoins(userCoffee, userQuarters, userDimes, userNickels, userPennies)
    