# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo

from pymongo import MongoClient

client= MongoClient("mongodb://localhost:27017/")

db_events = client ["EventsDB"]