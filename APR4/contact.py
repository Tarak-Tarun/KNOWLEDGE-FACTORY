import json
new_contact = {"name": input("Name: "), "phone": input("Phone: ")}
try:
    with open("contacts.json", "r") as f:
        data = json.load(f)
except:
    data = []
data.append(new_contact)
with open("contacts.json", "w") as f:
    json.dump(data, f, indent=4)