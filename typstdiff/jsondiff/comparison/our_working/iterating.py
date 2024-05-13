from jsondiff import diff
from jsondiff.symbols import Symbol
import json
import copy


class Comparison:
    def __init__(self, new_path, old_path):
        self.parsed_new_file = self.parse_load_file(new_path)
        self.parsed_old_file = self.parse_load_file(old_path)
        self.parsed_changed_file = self.parse_load_file(new_path)
        self.diffs = diff(self.parsed_old_file, self.parsed_changed_file, syntax='explicit', dump=False)

    def parse_load_file(self, path):
        with open(path, 'rb') as file:
            parsed_file = json.load(file)
        return parsed_file

    def format_paragraph(self, para, underline_strike):
        print(f"formating paragraph: {para}")
        if isinstance(para, dict):
            if "c" in para.keys():
                self.parse_list_dict(para["c"], underline_strike)
            else:
                self.parse_list_dict(para, underline_strike)
        elif isinstance(para, list):
            self.parse_list_dict(para, underline_strike)


    def parse_dict(self, dict, underline_strike):
        print(f"parse_dict: {dict}")
        if dict["t"] in ("Str", "Emph", "Strong", "Superscript", "Subscript", "SmallCaps", "Quoted", "Cite", "Code", "Space", "SoftBreak", "LineBreak"): # type of char
            para_copy = copy.deepcopy(dict)
            dict['t'] = underline_strike
            dict["c"] = [para_copy]
        elif dict["t"] in ("InlineMath", "DefaultStyle", "DefaultDelim", "DisplayMath", "Link"): # just skip "DefaultStyle", "DefaultDelim" and the rest as for now
            print(f"Skipping {dict}")
        else:
            self.format_paragraph(dict, underline_strike)


    def parse_list_dict(self, para, underline_strike):
        print(f"parse_list_dict: {para}")
        if isinstance(para, list):
            for i, element in enumerate(para):
                if isinstance(element, dict):
                    self.parse_dict(para[i], underline_strike)
                elif isinstance(element, list):
                    self.format_paragraph(para[i], underline_strike)
        else:
            if isinstance(para, dict):
                self.parse_dict(para, underline_strike)


    def parse_header(self, target, position):
        print(f"parsing header {target[position]}")
        for i in range(len(target[position]["c"])):
            if isinstance(target[position]["c"][i], list):
                for k in range(len(target[position]["c"][i])):
                    if isinstance(target[position]["c"][i][k], dict):
                        target_copy = copy.deepcopy(target[position]["c"][i][k])
                        target[position]["c"][i][k]['t'] = 'Underline'
                        target[position]["c"][i][k]['c'] =  [target_copy]


    def apply_diffs_recursive(self, diffs, target, current_action, parsed_old_file):
        try:                    
            if current_action is None or current_action == "update":
                print("----------UPDATING----------")
                print(f"diffs: {diffs}")
                for key, value in diffs.items():
                    if isinstance(key, Symbol): # character is action
                        next_action = key.label
                        self.apply_diffs_recursive(value, target, next_action, parsed_old_file)
                    elif isinstance(value, dict):
                        if isinstance(parsed_old_file, list) and isinstance(key,int):
                            if len(parsed_old_file) <= key:
                                self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file)
                            else:
                                self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key])
                        else:
                            self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key])
                    elif isinstance(value, list):
                        for i, v in enumerate(value):
                            if isinstance(v, dict):
                                self.apply_diffs_recursive(v, target[key][i], current_action, parsed_old_file[key][i])
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
                                self.format_paragraph(target[position][i], "Underline")
                    elif target[position]["t"] == "Header":
                            self.parse_header(target, position)
                    elif target[position]['t'] != "Str":
                            self.format_paragraph(target[position], "Underline")
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
                                self.format_paragraph(parsed_old_file[delete_position][i], "Strikeout")
                                # to_insert = [{"t": "Para", "c": parsed_old_file[delete_position][i]}]
                                to_insert = [parsed_old_file[delete_position][i]]

                    elif parsed_old_file[delete_position]["t"] in ("Para", "BulletList", "OrderedList"):
                            self.format_paragraph(parsed_old_file[delete_position], "Strikeout")
                            to_insert = parsed_old_file[delete_position]
                    
                    elif parsed_old_file[delete_position]["t"] == "Header":
                            self.parse_header(parsed_old_file, delete_position)
                            to_insert = parsed_old_file[delete_position]
                    else:
                        to_insert = {"t": "Strikeout", "c": [deleted_copy]}
            
                    target.insert(delete_position, to_insert)
                    
        except Exception as e:
            print(f"Parsing error: {e}")
            print(f"Skipping...")

comparison = Comparison("new.json", "old.json")

comparison.apply_diffs_recursive(comparison.diffs, comparison.parsed_new_file, None, comparison.parsed_old_file)

print(comparison.parsed_new_file)

with open('compared_new.json', 'w') as updated_file:
    json.dump(comparison.parsed_new_file, updated_file, indent=4)