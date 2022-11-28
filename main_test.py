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

if __name__ == '__main__':
    populate_all()
    show_all()
    remove_all()
