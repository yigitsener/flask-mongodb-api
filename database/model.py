from datetime import datetime
from time import time
from pymongo import MongoClient

class Mongodb():
    def __init__(self):
        try:
            client = MongoClient(
                "mongodb+srv://yigitsener:H3ujfxD0rP5XutK1@cluster0-mtpcl.mongodb.net/test?retryWrites=true&w=majority")
            db = client['pydata']
        except:
            client = MongoClient("mongodb://yigitsener:H3ujfxD0rP5XutK1@cluster0-mtpcl.mongodb.net/")
            db = client['pydata']
        self.collect = db.users_and_properties

    def createUser(self,username,password):
        if self.collect.find_one({"username":username}) != None:
            return False
        else:
            self.collect.insert_one({"username":username,
                                "password":password})
            return True

    def authUser(self,username,password):
        if self.collect.find_one({"username":username,"password":password}) != None:
            return True
        return False

    def createProperty(self,username,name,numberOfBedrooms,numberOfRooms):
        if self.collect.find_one({"username":username}) != None:
            property_1 = {"property_id": int(str(time()).replace(".", "")),
                          "createDate": datetime.now(),
                          "name": name,
                          "numberOfBedrooms": numberOfBedrooms,
                          "numberOfRooms": numberOfRooms}
            self.collect.update({"username": username}, {'$push': {"properties": property_1}})
            return property_1.get("property_id")
        return "User not found"

    def allKeys(self,key="properties"):
        l = []
        for _ in self.collect.find():
            l.append(_.get(key))
        if len(l) == 0:
            return "That key has no records"
        return l

    def getProperty(self,name):
        l = []
        for _ in self.allKeys():
            for j in _:
                if j.get("name") == name:
                    l.append(j)
        if len(l) == 0:
            return "That name has no property"
        return l

    def deleteProperty(self,username,property_id):
        result = self.collect.update({"username": username}, {"$pull": {"properties": {"property_id": property_id}}}).get("nModified")
        if result == 0:
            return "There already hasn't been id exists"
        return True


