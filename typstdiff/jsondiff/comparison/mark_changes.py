import json

with open('new.json', 'rb') as changed_file:
    parsed_new_file = json.load(changed_file)

print(parsed_new_file['blocks'][0]["c"][2])
print(parsed_new_file['blocks'][0]["c"][2]["c"])
# value = parsed_new_file['blocks'][0]["c"][2]["c"]
value = parsed_new_file['blocks'][0]["c"][2]
parsed_new_file['blocks'][0]["c"][2] = {"t":"Underline", "c": [value] }
print(parsed_new_file['blocks'][0]["c"][2])
# print({"t": "Underline", "c": value })




with open('compared.json', 'w') as updated_file:
    json.dump(parsed_new_file, updated_file, indent=4)