
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):


def check_resources(user_choices):
    for y in MENU[user_choices]["ingredients"]:
        ingredient_value = MENU[user_choices]["ingredients"][y]
        resources_value = resources[y]
        if ingredient_value <= resources_value:
            return True
        else:
            return print(f"sorry {y} not available")


machine_on = True
resources["Money"] = 0
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print(f"water : {resources['water']} ml")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} grams")
        print(f"Money : ${resources['Money']}")
    elif user_choice == "off":
        machine_on = False
    else:
        resources_available = check_resources(user_choice)
        if resources_available:
            print("please insert coins.")
            quarter_coins = int(input("How many quarters?: "))
            dimes_coins = int(input("How many dimes?: "))
            nickles_coins = int(input("How many nickles?: "))
            pennies_coins = int(input("How many pennies?: "))
            coins_inserted = 0.25*quarter_coins + 0.1 * dimes_coins + 0.05 * nickles_coins + 0.01 * pennies_coins
            print(coins_inserted)
            coffee_cost = MENU[user_choice]["cost"]
            if coins_inserted >= coffee_cost:
                profit = resources["Money"] + coffee_cost
                resources["Money"] = profit
                change_to_user = coins_inserted - coffee_cost
                print(f"Here is ${round(change_to_user,2)} dollars in change")
                for x in MENU[user_choice]["ingredients"]:
                    deduct_resources = resources[x] - MENU[user_choice]["ingredients"][x]
                    resources[x] = deduct_resources
                print(f"Here's your {user_choice}☕. Enjoy!")
            elif coins_inserted < coffee_cost:
                print("sorry that's not enough money, Money refunded")
