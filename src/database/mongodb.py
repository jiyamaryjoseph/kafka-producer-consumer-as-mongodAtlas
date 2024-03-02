import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:
        # MONGO_DB_URL='mongodb+srv://jiyamary:jiyasensor@cluster0.pqsvitg.mongodb.net/?retryWrites=true&w=majority'
        mongo_db_url = os.getenv('MONGO_DB_URL')
        print("MongoDB URL from environment variable:", mongo_db_url)
        self.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
        
        # self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)
        print(self.client )
        
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
    
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
