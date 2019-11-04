import json

x={"name":"swara","age":20}
y=json.dumps(x)
print(y)

p='{"name":"swa","age":4}'
q=json.loads(p)
print(q)

