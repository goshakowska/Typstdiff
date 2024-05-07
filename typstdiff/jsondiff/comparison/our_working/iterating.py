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

def format_paragraph(para, underline_strike):
    print(f"formating paragraph: {para}")
    if isinstance(para, dict):
        if "c" in para.keys():
            parse_list_dict(para["c"], underline_strike)
        else:
            parse_list_dict(para, underline_strike)
    elif isinstance(para, list):
        parse_list_dict(para, underline_strike)


def parse_dict(dict, underline_strike):
    print(f"parse_dict: {dict}")
    if dict["t"] in ("Str", "Emph", "Strong", "Superscript", "Subscript", "SmallCaps", "Quoted", "Cite", "Code", "Space", "SoftBreak", "LineBreak"): # type of char
        para_copy = copy.deepcopy(dict)
        dict['t'] = underline_strike
        dict["c"] = [para_copy]
    elif dict["t"] in ("InlineMath", "DefaultStyle", "DefaultDelim", "DisplayMath", "Link"): # just skip "DefaultStyle", "DefaultDelim" and the rest as for now
        print(f"Skipping {dict}")
    else:
        format_paragraph(dict, underline_strike)


def parse_list_dict(para, underline_strike):
    print(f"parse_list_dict: {para}")
    if isinstance(para, list):
        for i, element in enumerate(para):
            if isinstance(element, dict):
                parse_dict(para[i], underline_strike)
            elif isinstance(element, list):
                format_paragraph(para[i], underline_strike)
    else:
        if isinstance(para, dict):
            parse_dict(para, underline_strike)


def parse_header(target, position):
    print(f"parsing header {target[position]}")
    for i in range(len(target[position]["c"])):
        if isinstance(target[position]["c"][i], list):
            for k in range(len(target[position]["c"][i])):
                if isinstance(target[position]["c"][i][k], dict):
                    target_copy = copy.deepcopy(target[position]["c"][i][k])
                    target[position]["c"][i][k]['t'] = 'Underline'
                    target[position]["c"][i][k]['c'] =  [target_copy]


def apply_diffs_recursive(diffs, target, current_action, parsed_old_file):
    try:                    
        if current_action is None or current_action == "update":
            print("----------UPDATING----------")
            print(f"diffs: {diffs}")
            for key, value in diffs.items():
                if isinstance(key, Symbol): # character is action
                    next_action = key.label
                    apply_diffs_recursive(value, target, next_action, parsed_old_file)
                elif isinstance(value, dict):
                    if isinstance(parsed_old_file, list) and isinstance(key,int):
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
                    # above should also add old version
                    if key == "c" or key == "t":
                        target_copy = copy.deepcopy(target)
                        target['t'] = 'Underline'
                        target['c'] =  [target_copy]

        elif current_action == "insert":
            print("----------INSERTING----------")
            print(f"diffs: {diffs}")

            for change in diffs:
                position, value = change
                print(f"target[position] {target[position]}")

                if isinstance(target[position], list):
                    for i in range(len(target[position])):
                        if target[position][i]['t'] in ("Para", "BulletList"):
                            format_paragraph(target[position][i], "Underline")
                elif target[position]["t"] == "Header":
                        parse_header(target, position)
                elif target[position]['t'] != "Str":
                        format_paragraph(target[position], "Underline")
                elif target[position]['t'] == "Str":
                    target_copy = copy.deepcopy(target[position])
                    target[position]= {"t": "Underline", "c": [target_copy]}


        elif current_action == "delete":
            print("----------DELETE----------")
            diffs.reverse()
            print(f"diffs: {diffs}")
            for delete_position in diffs:
                deleted_copy = copy.deepcopy(parsed_old_file[delete_position])

                if isinstance(parsed_old_file[delete_position], list):
                    for i in range(len(parsed_old_file[delete_position])):
                        if parsed_old_file[delete_position][i]['t'] in ("Para", "BulletList"):
                            format_paragraph(parsed_old_file[delete_position][i], "Strikeout")
                            # to_insert = [{"t": "Para", "c": parsed_old_file[delete_position][i]}]
                            to_insert = [parsed_old_file[delete_position][i]]

                elif parsed_old_file[delete_position]["t"] in ("Para", "BulletList", "OrderedList"):
                        format_paragraph(parsed_old_file[delete_position], "Strikeout")
                        to_insert = parsed_old_file[delete_position]
                
                elif parsed_old_file[delete_position]["t"] == "Header":
                        parse_header(parsed_old_file, delete_position)
                        to_insert = parsed_old_file[delete_position]
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