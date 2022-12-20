import pytest
import main

log = main.SuplementLog()

def populate_all():
    names = ["Vit-B6","Vit-c","Vit-B10","Vit-B12","Vit-D3","Magnesium","Zink"]
    for name in names:
        log.add_inventory(name, 1000, "MG")
        log.add_intake("note", [{"name": name, "amount": 100, "unit": "MG"}])
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
    list_items = [{"s_type": "single", "name": "vitamin-b", "amount": 100, "unit": "MG"}]
    log.add_intake("Testing remove from inventory enough", list_items)
    result = log.show_inventory()
    # the result will be that there is less in inventory
    remove_all()
    assert result[0]["amount"] == 900
    # this maybe later be expanded to a series of tests
    # now it is only visually validated

def removefrominventory_not_enough():
    remove_all()
    log.add_inventory("vitamin-b", 100, "MG")
    list_items = [{"s_type": "single", "name": "vitamin-b", "amount": 1000, "unit": "MG"}]
    log.show_inventory()
    log.add_intake("Test remove from inventory not enough", list_items)
    # result will be that there will not be anything removed or taken in
    result = log.show_inventory()
    print(result[0])
    remove_all()
    assert result[0]["amount"] == 100

def removefrominventory_not_existing():
    remove_all()
    log.add_inventory("vitamin-b", 1000, "MG")   
    list_items = [{"s_type": "single", "name": "cocaine", "amount": 100, "unit": "MG"}]
    log.show_inventory()
    log.add_intake("Test remove from inventory not existing", list_items)
    # result will be that there will not be anything removed or taken in
    result = log.show_inventory()
    remove_all()
    assert result[0]["amount"] == 1000

def presetting_only_name():
    remove_all()
    item = [{"name": "L-tyrosine"}]
    preset = log.add_supplement("L-tyrosine", 50, 5000, 80, 15, "MG")
    result = log.presetting(item)
    # you give in a item or pre-stack and it will apply a preset if matching with presets 
    assert result[0][0] == "L-tyrosine"

def presetting_full_single():
    remove_all()
    log.presetting(item)

def presetting_mixed():
    remove_all()
    log.presetting(item)


if __name__ == '__main__':
    removefrominventory_enough()
    removefrominventory_not_enough()
    removefrominventory_not_existing()
