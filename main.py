import pymongo
import datetime

class SuplementLog:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["supplement-logs"]
        self.mysupplements = self.mydb["supplements"]
        self.mystacks = self.mydb["stacks"]
        self.myintake = self.mydb["intake-logs"]
        self.myinventory = self.mydb["inventory"]

    def add_to_collection(self, attribute, value):
        return getattr(self, attribute).insert_one(value)

    def import_to_collection(self, attribute, value):
        getattr(self, attribute).insert_many(value)

    def show_to_collection(self, attribute, value):
        return getattr(self, attribute).insert_many(value)

    def get_from_collection(self, attribute, query):
        return getattr(self, attribute).find(query)

    def drop_collection(self, attribute, value):
        getattr(self, attribute).drop()
    
    def add_intake_collection(self, note, item_x_list, attribute):
        item_y_old = []
        item_y_new = []
        for item_x in item_x_list:
            item_y_list = self.get_from_collection(attribute, { "name": item_x["name"]})
            for item_y in item_y_list:
                if item_x["amount"] < item_y["amount"]:
                    item_y_old.append({"name": item_y["name"], "amount": item_y["amount"], "unit": item_y["unit"]})
                    new_value = item_y["amount"] - item_x["amount"]
                    item_y_new.append({ "$set":{"name": item_y["name"], "amount": new_value, "unit": item_y["unit"]}})
        for match in zip(item_y_old, item_y_new):
            self.myinventory.update_one(*match)
        intake = {"datetime": datetime.datetime.utcnow(), "note": note, "supplements": item_x_list}
        self.myintake.insert_one(intake)

    # inventory
    def add_inventory(self, name, amount, unit):
        inventory = { "name": name, "amount": amount, "unit": unit }
        self.add_to_collection("myinventory", inventory)

    def import_inventory(self, data):
        self.myinventory.insert_many(data) 

    def show_inventory(self):
        inventory = []
        items = self.myinventory.find({})
        for item in items:
            inventory.append(item)
        return inventory

    def get_inventory(self, query):
        return self.myinventory.find(query)

    def drop_inventory(self):
        self.myinventory.drop()
 
    # supplement - is one single compound
    def add_supplement(self, name, low, high, start, step, unit):
        supplement = {"s_type": "single", "name": name, "range": {"low": low, "high": high}, "start": start, "step": step, "unit": unit}
        self.mysupplements.insert_one(supplement)

    def import_supplement(self, data):
        self.mysupplements.insert_many(data) 

    def show_supplement(self):
        items = self.mysupplements.find({})
        for item in items:
            print(item)

    def drop_supplement(self):
        self.mysupplements.drop()

    # stacks - can only consist of single supplements
    def add_stack(self, name, content_list):
        stack = {"s_type": "stack", "name": name, "version": 0, "supplements": content_list}
        self.mystacks.insert_one(stack)
    
    def import_stack(self, data):   
        self.mystacks.insert_many(data)
                            
    def show_stack(self):
        items = self.mystacks.find({})
        for item in items:          
            print(item)             
                            
    def drop_stack(self):
        self.mystacks.drop()

    # intake - can consist of stacks and singles
    def add_intake(self, note, list_items):
        self.add_intake_collection(note, list_items, "myinventory")
                            
    def import_intake(self, data):   
        self.myintake.insert_many(data)   

    def show_intake(self):
        items = self.myintake.find({})
        for item in items:
            print(item)
                                        
    def drop_intake(self):
        self.myintake.drop()
