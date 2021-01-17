from pymongo import MongoClient
import os

cluster = MongoClient(os.getenv("MONGDB_URL"))
database = cluster["Test"]
command_list = database["Commands"]