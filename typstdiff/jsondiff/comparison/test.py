from jsondiff import diff
from jsondiff.symbols import Symbol
import json

# from_ pandoc
with open('new_v.json', 'rb') as changed_file:
    parsed_new_file = json.load(changed_file)

paragraphs_list = parsed_new_file['blocks']

# dokumenty zamienione z typsta
with open('old_v.json', 'rb') as old_file:
    parsed_old_file = json.load(old_file)

with open('new_v.json', 'rb') as changed_file:
    parsed_changed_file = json.load(changed_file)

diffs = diff(parsed_old_file, parsed_changed_file, syntax='explicit', dump=False)

update = Symbol("update")
print(diffs)
print("AAA")

# def skip_layer(diffs, symbol_label):
#     symbol = Symbol(symbol_label)
#     keys = diffs.keys()
#     if len(keys) == 1:
#         if keys[0] is i
#     for key in diffs.keys():
#         diffs = diffs[key]
#     return diffs

# change later
keys = list(diffs.keys())
diffs = diffs[keys[0]]

keys = list(diffs.keys())
diffs = diffs[keys[0]] 

# keys = diffs.keys()
# diffs = diffs[keys]

print(diffs) # we have list of changes
list_of_changed_paragraphs = list(diffs.keys())


def parse_index(to_change, paragraphed_changed, current_action):

    keys = list(to_change.keys())
    character = keys[0]
    to_change = to_change[keys[0]]

    if current_action is None or current_action == "update":
        if isinstance(character, int): # character is index for list
            paragraphed_changed = paragraphed_changed[character]
        elif character in paragraphed_changed.keys():
            print(paragraphed_changed.keys())
            paragraphed_changed = paragraphed_changed[character]
        elif isinstance(character, Symbol): # character is action
            next_action = character.label
    elif current_action == "delete":
        pass
        
    
    print(f"character: {character}")
    print(f"paragraph changed: {paragraphed_changed}")


    return (to_change, paragraphed_changed, next_action)


for paragraph_index in list_of_changed_paragraphs:
    print("----------------------- CHANGE PROCESS -------------------------")
    to_change = diffs[paragraph_index]
    print(f"TO CHANGE: {to_change}")
    paragraphed_changed = paragraphs_list[paragraph_index]
    print(f"PARAGRAPH CHANGED: {paragraphed_changed}")

    current_action = None
    while isinstance(to_change, dict):
        to_change, paragraphed_changed, current_action = parse_index(to_change, paragraphed_changed, current_action)


# print(keys)
# print(f"FIRST CHANGE: {diffs[1]}") # first change
# first_change = diffs[1]

# keys = list(first_change.keys())
# first_change = first_change[keys[0]]

# print(first_change)
# print(first_change['c'])
# print(first_change['c'][2])




