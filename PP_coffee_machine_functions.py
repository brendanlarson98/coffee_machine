def print_report(resources):
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money:', "${:,.2f}".format(resources['money']))

def subtract_resources(resources, item):
    for i in resources:
        if i == 'money':
            continue
        resources[i] -= item[i]

def refill_resource(resource, item = None, amount = None):
    if item == None and amount == None:
        item, amount = get_resource_amount()
    resource[item] += amount

def check_resources(resources, item):
    good_amount = True
    for resource in resources:
        if resource == 'money':
            continue
        if item[resource] > resources[resource]:
            good_amount = False
            print("There isn't enough", resource)

    return good_amount

def get_option(drinks):
    valid = False
    options = ['report', 'espresso', 'latte', 'cappucino', 'quit']
    while not valid:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice not in options:
            print("Please enter a valid input.")
        else:
            valid = True
    return choice

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

def check_price(paid, cost):
    if paid < cost:
        print(f"Not enough money inserted.\nAmount refunded:", "${:,.2f}".format(paid))
        return False
    else:
        change = paid - cost
        print(f"Change refunded:", "${:,.2f}".format(change))
        return True

def check_number(value):
    valid = False
    while not valid:
        try:
            num = int(input(f"{value}: "))
            valid = True
        except ValueError:
            print("Not a valid number.")
    return num

def charge_amount(resources, item):                         # Here we check to see what money input we receive
    print(item)
    print("Cost:", "${:,.2f}".format(item['money']), "\nPlease insert money.") 
    amount_paid = 0
    coins = ["Quarters", "Dimes", "Nickels", "Pennies"]
    amounts = [0.25, 0.1, 0.05, 0.01]
    for coin, amount in zip(coins, amounts):
        amount_paid += (amount * check_number(coin))

    return check_price(amount_paid, item['money'])          # Compare input amount to the cost of our item.
