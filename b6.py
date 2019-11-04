
import json

data1={"name":"swarali","age":19}
y=json.dumps(data1)
print(y)
print(data1["name"])

data={}
data['people']=[]

data['people'].append({'name':'sd','comapny':'dffs'})
data['people'].append({'name':'sg','comapny':'gffs'})

x=json.dumps(data,indent=4)
print(x)
print(data["people"])

print(data["people"][0])

print(data["people"][0]["name"])

#decoding
p='{"name":"swa","age":4}'
q=json.loads(p)
print(q)

#dump used for encoding and loads used for encoding


