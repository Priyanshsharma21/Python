# Coffee Machine
# Give a resource of coffee and its cost, ingeridants
# We have coin -> peeny(0.01) 1 cent , dime(0.10) 10 cents , nickel(0.05) 5 cents, quarer(0.25) 25 cents
# 1. We want our coffee machine to print repote
# 2. check the resource
# 3. process coins
# 4. Check transiction
# ------------------------------------------------------------

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# --------------------Let the code begin------------------------------













def is_resource_sufficient(order_ingrediants):
    for item in order_ingrediants:
        if order_ingrediants[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transiction_success(money_recived,total_cost):
    if money_recived>=total_cost:
        change = round(money_recived-total_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += total_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_name,ingredients_of_coffee):
    for item in ingredients_of_coffee:
        resources[item] -= ingredients_of_coffee[item]
    print(f"Here is your {coffee_name}, enjoy😁☕🍵")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        print("Power off....................")
        is_on=False
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transiction_success(payment, drink['cost']):
                make_coffee(choice,drink['ingredients'])

