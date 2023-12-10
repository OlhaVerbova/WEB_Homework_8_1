
# Напишіть скрипти для завантаження json файлів у хмарну базу даних.

import json
from pymongo import MongoClient


client = MongoClient("mongodb+srv://userweb17:567234@cluster0.x8roo9r.mongodb.net/hw8_1", ssl=True)
db = client["hw8_1"]
collection_authors = db["authors"]
collection_qoutes = db["qoutes"]


with open("authors.json", "r") as fd:
    author_data = json.load(fd)

with open("qoutes.json", "r") as fd:
    qoutes_data = json.load(fd)


collection_authors.insert_many(author_data)
collection_qoutes.insert_many(qoutes_data)