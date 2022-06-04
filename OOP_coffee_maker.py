def get_resource_amount():
    resources_choice = ['milk', 'water', 'coffee']
    valid = False
    while not valid:
        resource_fill = input("What resource would you like to refill? ").lower()
        if resource_fill in resources_choice:
            valid = True
        else:
            print("Please select milk, water, or coffee to refill.")
    valid = False
    while not valid:
        try:
            amount_to_fill = float(input("How much would you like to refill by? "))
            valid = True
        except ValueError:
            print("Please enter a valid number")
    
    return resource_fill, amount_to_fill

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refill_resource(self):
        item, amount = get_resource_amount()
        self.resources[item] += amount
