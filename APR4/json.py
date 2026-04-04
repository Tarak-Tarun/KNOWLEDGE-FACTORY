import json

data = {"name": "Tarak", "age": 20}

f = open("data.json", "w")
json.dump(data, f)
f.close()

f = open("data.json", "r")
data = json.load(f)
f.close()

print(data)