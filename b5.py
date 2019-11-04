import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["MyDatabase"]

print(myclient.list_database_names())

mylist=myclient.list_database_names()
if "MyDatabase" in mylist:
   print('The database exists')

mycol=mydb['Customers']
print(mydb.list_collection_names())

#mydict={"name":"swarali","city":"pune"}
#x=mycol.insert_one(mydict)
#print(x.inserted_id)

mydict=[
{"name":"swarali","city":"pune"},
{"name":"priyanka","city":"indore"},
{"name":"leena","city":"mumbai"},
]

x=mycol.insert_many(mydict)
print(x.inserted_ids)

#y=mycol.find_one()
#print(y)

#x=mycol.find()
#print(x)

for y in mycol.find({},{"_id":0,"name":1,"city":1}):
    print(y)

myquery={"name":"swarali"}
w=mycol.find(myquery)

for p in w:
	print(p)

myquery = { "city": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

SORT
UPDATE
LIMIT
