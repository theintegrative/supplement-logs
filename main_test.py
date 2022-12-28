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
    log.show_inventory()
    log.show_supplement()
    log.show_stack()
    log.show_intake()

def remove_all():
    log.drop_inventory()
    log.drop_supplement()
    log.drop_stack()
    log.drop_intake()

@pytest.mark.parametrize("control_item_amount, control_item_name, test_item_amount, test_item_name, result", 
        [
            (1000, "SAME-ITEM", 100, "SAME-ITEM", 900),
            (100, "SAME-ITEM", 1000, "SAME-ITEM", 100),
            (1000, "SAME-ITEM", 100, "DIFF-ITEM", 1000)
            ]
        )
def test_inventory(control_item_amount, control_item_name, test_item_amount, test_item_name, result):
    remove_all()
    unit = "UNIT"                                                                            
    log.add_inventory(control_item_name, control_item_amount, unit)
    list_items = [{"name": test_item_name, "amount": test_item_amount, "unit": unit}]
    log.add_intake("TEST", list_items)
    assert log.show_inventory()[0]["amount"] == result
    remove_all()

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
