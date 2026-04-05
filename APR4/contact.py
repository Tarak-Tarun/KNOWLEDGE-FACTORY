import json

# new contact
new_contact = {"name": input("Name: "), "phone": input("Phone: ")}

# read existing data
try:
    with open("contacts.json", "r") as f:
        data = json.load(f)
except:
    data = []

# add new contact
data.append(new_contact)

# write back to file
with open("contacts.json", "w") as f:
    json.dump(data, f, indent=4)