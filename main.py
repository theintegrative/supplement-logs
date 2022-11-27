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
 
    # supplement
    def add_supplement(self, name, low, high, start, step, unit):
        supplement = {"name": name, "range": {"low": low, "high": high}, "start": start, "step": step, "unit": unit}
        self.mysupplements.insert_one(supplement)

    def import_supplement(self, data):
        self.mysupplements.insert_many(data) 

    def show_supplement(self):
        items = self.mysupplements.find({})
        for item in items:
            print(item)

    def drop_supplement(self):
        self.mysupplements.drop()

    # stacks
    def add_stack(self, name, content_list):
        stack = {"name": name, "version": 0, "supplements": content_list}
        self.mystacks.insert_one(stack)
    
    def import_stack(self, data):   
        self.mystacks.insert_many(data)
                            
    def show_stack(self):
        items = self.mystacks.find({})
        for item in items:          
            print(item)             
                            
    def drop_stack(self):
        self.mystacks.drop()

    # intake
    def add_intake(self, note, content_list):
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
