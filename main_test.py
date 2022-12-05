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
    remove_all()
    log.add_inventory("vitamin-b", 1000, "MG")
    print(log.show_inventory())
    list_items = [{"s_type": "single", "name": "vitamin-b", "amount": 100, "unit": "MG"}]
    log.add_intake("Testing remove from inventory enough", list_items)
    print("Log added")
    # the result will be that there is less in inventory
    assert log.show_inventory()[0]["amount"] == 900
    # this maybe later be expanded to a series of tests
    # now it is only visually validated

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
    removefrominventory_enough()

