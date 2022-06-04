import PP_coffee_machine_functions as cmf

resources = {                               # here we have what resources our coffee machine currently has
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

espresso = {                                # Then for each option, how many resources it takes
    'water': 50,
    'milk': 0,
    'coffee': 18,
    'money': 1.50
}

latte = {
    'water': 200,
    'milk': 150,
    'coffee': 24,
    'money': 2.50
}

cappuccino = {
    'water': 250,
    'milk': 100,
    'coffee': 24,
    'money': 3.00
}

drinks = {
    'espresso': espresso,                   # Dictionary for our options
    'latte': latte,
    'cappuccino': cappuccino
}

vend = True
while vend:                                 # While we are vending, we get our option for what drink to get
    choice = cmf.get_option(drinks)
    if choice == 'quit':
        vend = False
        break
    elif choice == 'report':                # Or print a report of what resources we have 
        cmf.print_report(resources)
        continue
    
    drink_choice = drinks.get(choice)
    has_resources = cmf.check_resources(resources, drink_choice) 
    if not has_resources:                   #if we do not have our resources, we should see if we want to refill any
        is_refill = True
        while is_refill:
            refill = input("would you like to refill any resources? (y/n): ")
            if refill == "y" or refill == 'yes':
                cmf.refill_resource(resources)          
            elif refill == 'n' or refill == 'no':
                is_refill = False                       
                continue
            else:
                print("Please enter a valid input (y/n).") #
        continue                            # If we have refilled or run out of resources, then we want to start our vending process over.
    
    if cmf.charge_amount(resources, drink_choice):            # perform the operation of getting money. Inside this function, we also test if we have received the right amount.
        cmf.subtract_resources(resources, drink_choice)           # If we have, then we subtract resources, add our money.
        cmf.refill_resource(resources, 'money', drink_choice['money'])
        print(f"Enjoy your {choice}!\n")

