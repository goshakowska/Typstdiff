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

def apply_format_to_para(para, underline_strike):
    print("here")
    print(para)
    if isinstance(para, dict):
        if isinstance(para["c"], list):
            for i, element in enumerate(para["c"]):
                print(element)
                # para
                if isinstance(element, dict):
                    if element.get("t") == "Str":
                        para["c"][i] = {"t": underline_strike, "c": [element]}
                    else:
                        apply_format_to_para(element, underline_strike)
                # header
                elif isinstance(element, list):
                    print(element)
                    for i in range(len(element)):
                        apply_format_to_para(element[i], "Underline")
        else:
            para_copy = copy.deepcopy(para)
            para["t"] = underline_strike
            para["c"] = [para_copy]
            print(para)

def delete_for_para(para, strike):
    print("delete_for_para")
    print(para["c"])
    for i, element in enumerate(para["c"]):
        if isinstance(element, dict):
            print(element)
            if element.get("t") == "Str":
                para["c"][i] = {"t": strike, "c": [element]}
                print(para["c"])
            else:
                print("AAAAA")
                delete_for_para(element, strike)
        if isinstance(element, list):
            print(element)
            for i, value in enumerate(element):
                if isinstance(value, dict):
                    value_copy = copy.deepcopy(value)
                    value["t"] = strike
                    value["c"] = [value_copy]
    print(para["c"])
    para_copy = copy

def apply_diffs_recursive(diffs, target, current_action, parsed_old_file):
    try:
                        
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
                    if isinstance(parsed_old_file, list) and isinstance(key,int):
                        print("Aaaaa")
                        print(parsed_old_file)
                        print(key)
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
                            print(target[key])
                            print(i)
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
                print(f"target[position] {target[position]}")

                # check if this is para
                if isinstance(target[position], list):
                    for i in range(len(target[position])):
                        if target[position][i]['t'] == "Para":
                            apply_format_to_para(target[position][i], "Underline")
                else:
                    if target[position]['t'] != "Str":
                        apply_format_to_para(target[position], "Underline")

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
                print("aaa")
                print(parsed_old_file[delete_position])

                if isinstance(parsed_old_file[delete_position], list):
                    for i in range(len(parsed_old_file[delete_position])):
                        if parsed_old_file[delete_position][i]['t'] == "Para":
                            print("bbb")
                            print(parsed_old_file[delete_position][i])
                            to_insert = delete_for_para(parsed_old_file[delete_position][i], "Strikeout") # przecież to nic nie zwraca
                            to_insert = [{"t": "Para", "c": to_insert}]
                            print(f"to_insert {to_insert}")
                elif parsed_old_file[delete_position]["t"] == "Header":
                   
                        print(parsed_old_file[delete_position])
                        delete_for_para(parsed_old_file[delete_position], "Strikeout")
                        print(parsed_old_file[delete_position])
                        to_insert = parsed_old_file[delete_position]
                        print(f"to_insert {to_insert}")
                else:
                    to_insert = {"t": "Strikeout", "c": [deleted_copy]}
                target.insert(delete_position, to_insert)
    except Exception as e:
        print(f"Parsing error: {e}")
        print(f"Skipping...")

apply_diffs_recursive(diffs, parsed_new_file, None, parsed_old_file)

print(parsed_new_file)

with open('compared_new.json', 'w') as updated_file:
    json.dump(parsed_new_file, updated_file, indent=4)