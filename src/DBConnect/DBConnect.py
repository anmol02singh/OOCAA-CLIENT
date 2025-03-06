import pymongo

client = pymongo.MongoClient('mongodb://localhost/cdm-data')

db = client['cdm-data']

db_collections = db['cdms']

i = 0
for document in db_collections.find():
    if(i < 3):
        print(document)
        i += 1
    else:
        break