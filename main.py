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
    
    # inventory
    def add_inventory(self, name, amount, unit):
        inventory = { "name": name, "amount": amount, "unit": unit }
        self.myinventory.insert_one(inventory)

    def import_inventory(self, data):
        self.myinventory.insert_many(data) 

    def show_inventory(self):
        items = self.myinventory.find({})
        for item in items:
            print(item)

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
    def add_intake(self, note, content_list):
        # for every item in content_list
            # check if supplement.name is in inventory
                # remove from that the item.amount if < suplement.amount and update the value
        intake = {"datetime": datetime.datetime.utcnow(), "note": note, "supplements": content_list}
        self.myintake.insert_one(intake)
                            
    def import_intake(self, data):   
        self.myintake.insert_many(data)   

    def show_intake(self):
        items = self.myintake.find({})
        for item in items:
            print(item)
                                        
    def drop_intake(self):
        self.myintake.drop()
