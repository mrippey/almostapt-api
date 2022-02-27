from pymongo import MongoClient

conn_mongo_cli = 'path to mongodb compass'

client = MongoClient(conn_mongo_cli, authSource='admin')
db = client['tagroupdb']
db_collection = db.tagroups
