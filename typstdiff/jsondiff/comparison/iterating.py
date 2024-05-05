from jsondiff import diff
from jsondiff.symbols import Symbol
import json
import copy

with open('new.json', 'rb') as changed_file:
    parsed_new_file = json.load(changed_file)

with open('old.json', 'rb') as old_file:
    parsed_old_file = json.load(old_file)

with open('new.json', 'rb') as changed_file:
    parsed_changed_file = json.load(changed_file)

diffs = diff(parsed_old_file, parsed_changed_file, syntax='explicit', dump=False)

# print(parsed_new_file)
print(diffs)

def apply_diffs_recursive(diffs, target, current_action, parsed_old_file):
    print(diffs)
    if current_action is None or current_action == "update":
        print(diffs)
        for key, value in diffs.items():
            if isinstance(key, Symbol): # character is action
                next_action = key.label
                apply_diffs_recursive(value, target, next_action, parsed_old_file)
            elif isinstance(value, dict):
                print("CHECKING")
                print(f"key: {key}")
                print(f"target: {target}")
                print(f"target[key]: {target[key]}")
                print(f"current_action: {current_action}")
                print(f"parsed_old_file: {parsed_old_file}")
                # if isinstance(key, int):
                #     if isinstance(parsed_old_file, list):
                #         if len(parsed_old_file) <= key:
                #             parsed_old_file = parsed_old_file[key]
                #     elif isinstance(parsed_old_file, dict):
                #         if key in parsed_old_file.keys():
                #             parsed_old_file = parsed_old_file[key]
                if isinstance(parsed_old_file, list):
                    if len(parsed_old_file) <= key:
                        apply_diffs_recursive(value, target[key], current_action, parsed_old_file)
                    else:
                        apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key])
                else:
                    apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key])
            elif isinstance(value, list):
                for i, v in enumerate(value):
                    if isinstance(v, dict):
                        apply_diffs_recursive(v, target[key][i], current_action, parsed_old_file[key][i])
                    else:
                        target[key][i] = v
            else:
                # wyżej powinno jeszcze dodać starą wersję
                if key == "c":
                    target_copy = copy.deepcopy(target)
                    target['t'] = 'Underline'
                    target['c'] =  [target_copy]
                    print(f"target {target}")
                elif key == "t":
                    target_copy = copy.deepcopy(target)
                    target['t'] = 'Underline'
                    target['c'] =  [target_copy]

    elif current_action == "insert":
        print("----------INSERTING----------")
        print(f"target {target}")
        print(diffs)

        for change in diffs:
            position, value = change
            print(change)
            print(target)
            print(target[position])
            target_copy = copy.deepcopy(target[position])
            target[position] = {"t":"Underline","c":[target_copy]}

    elif current_action == "delete":
        print("----------DELETE----------")
        diffs.reverse()
        print(f"diffs {diffs}")
        print(f"target {target}")
        print(f"parsed_old_file {parsed_old_file}")
        for delete_position in diffs:
            print(f"delete_position: {delete_position}")
            print(parsed_old_file[delete_position])
            print(target[delete_position-1])
            target_copy = copy.deepcopy(target[delete_position-1])
            deleted_copy = copy.deepcopy(parsed_old_file[delete_position])
            to_insert = {"t":"Strikeout","c":[deleted_copy]}
            target.insert(delete_position, to_insert)

apply_diffs_recursive(diffs, parsed_new_file, None, parsed_old_file)

print(parsed_new_file)

with open('compared_new.json', 'w') as updated_file:
    json.dump(parsed_new_file, updated_file, indent=4)