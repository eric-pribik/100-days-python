
def transaction_check(order, choice):
    insered_cash = int(input("How many quarters?: ")) * 0.25
    insered_cash += int(input("How many dimes?: ")) * 0.10
    insered_cash += int(input("How many nickels?: ")) * 0.05
    if insered_cash >= int(order["price"]):
        print(f"your change is ${insered_cash - order["price"]} \n Here is your {choice}")
        return True
    else:
        print("Sorry that is not enough change")
        return False

def resource_check(order, resources):
    a = True
    for key in order:
        if key == "price":
            continue
        if order[key] > resources[key]:
            a = key
    return a

def update_resources(drink, resources):
    new_resources_dict = {}
    for key in drink:
        if key == "price":
            new_resources_dict.update({"money": resources['money'] + drink["price"]})
        else:
            new_resources_value = resources[key] - drink[key]
            new_resources_dict.update({key: new_resources_value})
    return new_resources_dict

def main():
    current_resource_values = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
    "money": 50
    }
    menu = {
    "espresso": {"water": 50, "coffee": 18,"price": 3},
    "latte": {"water": 200,"coffee": 24,"milk": 150,"price": 2.5},
    "cappuccino": {"water": 250,"coffee": 24,"milk": 100,"price": 3.5}
    }

    continue_opperation = True
    while continue_opperation:
        user_input = input("What would you like? (espresso/latte/cappuccino):")
        if user_input == "report":
            print(f"Water: {current_resource_values['water']}ml\nMilk: {current_resource_values['milk']}ml\nCoffee: {current_resource_values['coffee']}g\nMoney: ${current_resource_values['money']}")
        elif user_input == "off":
            print("The Coffee Machine is powering off...")
            continue_opperation = False
        else:
            user_choice = menu.get(user_input)
            if user_choice is None:
                continue
            a = resource_check(user_choice, current_resource_values)
            if a == True:
                a = transaction_check(user_choice, user_input)
                if a == True:
                    a = update_resources(user_choice, current_resource_values)
                    current_resource_values = a
            else:
                print(f"we are out of {a}")

if __name__ == "__main__":
    main()
