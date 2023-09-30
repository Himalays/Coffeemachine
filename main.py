from data import Resources,Menu,profit 

flag = True
def check_resources(order_ingredients):
    """ Returns true when order can be made, false if insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > Resources[item]:
            print(f"Sorry there not enough {item}.")
            return False
    return True

def coins():
    print("Insert coins")
    total = int(input (" How many quarters :")) *0.25
    total+= int(input (" How many dimes :")) *0.1
    total+= int(input (" How many nickle :")) * 0.05    
    total+= int(input (" How many pennies :")) * 0.01
    return total

def transaction(money_recieved, cost):
    global profit
    if money_recieved >= cost:
        change = round(money_recieved-cost,2)
        print(f"here is the change ${change} in change")
        profit+=cost
        return True 
    else:
        print("Not enough money")
        return False

def make_coffee(name, ingredients):
    for item in ingredients:
        Resources[item] -= ingredients[item]
    print(f" Here is your {name}.")

while flag:
    choice = input("Choose espresso/latte/capuccinho :")
    if choice == "off":
        flag= False
    elif choice=="report":
        print(f"Water : {Resources['water']}ml")
        print(f"Milk : {Resources['milk']}ml")
        print(f"Coffee : {Resources['coffee']}ml")
        print(f"Money : $ {profit}")
    else:
        drink = Menu[choice]
        if check_resources(drink["ingredients"]):
            payment = coins()
            if transaction(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

