from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
keurig = CoffeeMaker()
register = MoneyMachine()

in_process = True
while in_process:
    item = input(f"What would you like to order? ({menu.get_items()}) ")
    if item == "report":
        register.report()
        continue
    menu_item = menu.find_drink(item)
    if not menu_item:
        continue
    while not keurig.is_resource_sufficient(menu_item):
        keurig.refill_resource()
        
    if register.make_payment(menu_item.cost):
        keurig.make_coffee(menu_item)
