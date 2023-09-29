from data import Resources,Menu,profit 

def is_resources_sufficient(order_ingredients):
    """ Returns true when order can be made, false if insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > Resources[item]:
            print(f"Sorry there not enough {item}.")
            return False
    return True

def process_coins():
    print("Insert coins")
    total = int(input (" How many quarters :")) *0.25
    total+= int(input (" How many dimes :")) *0.1
    total+= int(input (" How many nickle :")) * 0.05    
    total+= int(input (" How many pennies :")) * 0.01
    return total


