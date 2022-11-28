import pytest
import main

log = main.SuplementLog()

def populate_all():
    names = ["Vit-B6","Vit-c","Vit-B10","Vit-B12","Vit-D3","Magnesium","Zink"]
    for name in names:
        log.add_inventory(name, "test", "MG")
        log.add_intake("note", {"name": name})
        log.add_supplement(name, 10, 100, 30, 10, "MG")
        log.add_stack(name + " stack", { "name": name, "amount": 100, "unit": "MG" })

def show_all():
    print("Inventory")
    log.show_inventory()
    print("Supplements")
    log.show_supplement()
    print("Stacks")
    log.show_stack()
    print("Intake")
    log.show_intake()

def remove_all():
    print("Drop Inventory")
    log.drop_inventory()
    print("Drop Supplements")
    log.drop_supplement()
    print("Drop Stacks")
    log.drop_stack()
    print("Drop Intake")
    log.drop_intake()

def removefrominventory_enough():
    log.add_inventory("vitamin-b", 1000, "MG")
    log.show_inventory()
    log.add_intake("Test remove from inventory enough", {"": name})
    # the result will be that there is less in inventory
    log,show_inventory()

def removefrominventory_not_enough():
    log.add_inventory("vitamin-b", 1000, "MG")
    log.show_inventory()
    log.add_intake("Test remove from inventory not enough", {"name": name})
    # result will be that there will not be anything removed or taken in
    log.show_inventory()

def removefrominventory_not_existing():         
    log.add_inventory("vitamin-b", 1000, "MG")   
    log.show_inventory()
    log.add_intake("Test remove from inventory not existing", {"name": name})
    # result will be that there will not be anything removed or taken in
    log.show_inventory()


if __name__ == '__main__':
    show_all()
    remove_all()
    show_all()
