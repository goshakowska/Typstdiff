from jsondiff import diff
from jsondiff.symbols import Symbol
import json
import copy
# from_ pandoc
with open('new.json', 'rb') as changed_file:
    parsed_new_file = json.load(changed_file)


with open('old.json', 'rb') as old_file:
    parsed_old_file = json.load(old_file)

with open('new.json', 'rb') as changed_file:
    parsed_changed_file = json.load(changed_file)

diffs = diff(parsed_old_file, parsed_changed_file, syntax='explicit', dump=False)

# print(parsed_new_file)
print(diffs)

def apply_diffs_recursive(diffs, target, current_action):
    if current_action is None or current_action == "update":
        print("AAAAA")
        print(diffs)
        for key, value in diffs.items():
            if isinstance(key, Symbol): # character is action
                next_action = key.label
                apply_diffs_recursive(value, target, next_action)
            elif isinstance(value, dict):
                apply_diffs_recursive(value, target[key], current_action)
            elif isinstance(value, list):
                for i, v in enumerate(value):
                    if isinstance(v, dict):
                        apply_diffs_recursive(v, target[key][i], current_action)
                    else:
                        target[key][i] = v
            else:
                if key == "c":
                    target_copy = copy.deepcopy(target)
                    target['t'] = 'Underline'
                    target['c'] =  [target_copy]
                    print(f"target {target}")
                elif key == "t":
                    target_copy = copy.deepcopy(target)
                    target['t'] = 'Underline'
                    target['c'] =  [target_copy]



apply_diffs_recursive(diffs, parsed_new_file, None)

print(parsed_new_file)

with open('compared_new.json', 'w') as updated_file:
    json.dump(parsed_new_file, updated_file, indent=4)