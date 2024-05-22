from jsondiff import diff
from jsondiff.symbols import Symbol

import json
import copy
from FileConverter import FileConverter


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

    def decorator_format_para(func):
        def wrapper(self, para, underline_strike):
            print(f"Applying decorator to paragraph: {para}")
            if isinstance(para, dict):
                if "c" in para.keys():
                    return func(self, para["c"], underline_strike)
                else:
                    return func(self, para, underline_strike)
            elif isinstance(para, list):
                return func(self, para, underline_strike)
            else:
                print(f"Unsupported type for para: {type(para)}")
                return None
        return wrapper


    def parse_dict(self, dict, underline_strike):
        print(f"parse_dict: {dict}")
        if dict["t"] in ("Link", "Math", "Str", "Emph", "Strong", "Superscript", "Subscript", "SmallCaps", "Quoted", "Cite", "Code", "Space", "SoftBreak", "LineBreak"): # type of char
            para_copy = copy.deepcopy(dict)
            dict['t'] = underline_strike
            dict["c"] = [para_copy]
        elif dict["t"] in ("InlineMath", "DefaultStyle", "DefaultDelim", "DisplayMath"): # just skip "DefaultStyle", "DefaultDelim" and the rest as for now
            print(f"Skipping {dict}")
        else:
            self.parse_list_dict(dict, underline_strike)

    @decorator_format_para
    def parse_list_dict(self, para, underline_strike):
        print(f"parse_list_dict: {para}")
        if isinstance(para, list):
            for i, element in enumerate(para):
                if isinstance(element, dict):
                    self.parse_dict(para[i], underline_strike)
                elif isinstance(element, list):
                    self.parse_list_dict(para[i], underline_strike)
        else:
            if isinstance(para, dict):
                self.parse_dict(para, underline_strike)


    def parse_header(self, target, position, format_action):
        print(f"parsing header {target[position]}")
        for i in range(len(target[position]["c"])):
            if isinstance(target[position]["c"][i], list):
                for k in range(len(target[position]["c"][i])):
                    if isinstance(target[position]["c"][i][k], dict):
                        target_copy = copy.deepcopy(target[position]["c"][i][k])
                        target[position]["c"][i][k]['t'] = format_action
                        target[position]["c"][i][k]['c'] =  [target_copy]


    def format_changes(self, target, position, format_action):
        if isinstance(target[position], list):
            for i in range(len(target[position])):
                if target[position][i]['t'] in ("Para", "BulletList"):
                    self.parse_list_dict(target[position][i], format_action)
                    # if delete then return insert
                    to_insert = [target[position][i]]
        elif target[position]["t"] == "Header":
                self.parse_header(target, position, format_action)
                to_insert = target[position]
        elif target[position]['t'] in ("Para", "BulletList", "OrderedList", "Div", "CodeBlock"):
                self.parse_list_dict(target[position], format_action)
                to_insert = target[position]
        else:
            target_copy = copy.deepcopy(target[position])
            target[position]= {"t": format_action, "c": [target_copy]}
            to_insert = target[position]
            return to_insert
        
    def update(self, diffs, target, old_target, index):
        print(f"UPDATE {diffs} {index}")
        if len(list(diffs.values())) > 1 and all(isinstance(key, int) for key in diffs.keys()):
            new_diffs = {}
            for to_add, (key, value) in enumerate(diffs.items()):
                new_diffs[(key, key+to_add)] = value
            diffs = new_diffs
        for key, value in diffs.items():
            if not isinstance(list(value.values())[0], dict):
                target_copy = copy.deepcopy(target[index[1]])
                old_target_copy = copy.deepcopy(old_target[index[0]])
                target[index[1]] = {"t": "Strikeout", "c": [old_target_copy]}
                target.insert(index[1]+1, {"t": "Underline", "c": [target_copy]})
            elif isinstance(key, Symbol):
                if key.label == 'insert':
                    continue
                elif key.label == 'delete':
                    continue
                elif key.label == 'update' and isinstance(list(value.values())[0], dict):
                    self.update(value, target, old_target, index)
            else:
                self.update(value, target[index], old_target[index], key)


    def parse(self):
        if self.diffs:
            self.apply_diffs_recursive(self.diffs, self.parsed_changed_file, None, self.parsed_old_file, self.parsed_new_file)
        self.diffs = diff(self.parsed_old_file, self.parsed_new_file, syntax='explicit', dump=False)
        print(f"NEW DIFFS: {self.diffs}")
        if self.diffs:
            key = None
            while not isinstance(key, int):
                for key, value in self.diffs.items():
                    if isinstance(key, int):
                        self.update(value, self.parsed_changed_file['blocks'], self.parsed_old_file['blocks'], key)
                    else:
                        self.diffs = value
                        

    def apply_diffs_recursive(self, diffs, target, current_action, parsed_old_file, parsed_new_file):
            # print(target)
        # try:                   
            if current_action is None or current_action == "update":
                print("----------UPDATING----------")
                print(f"diffs: {diffs}")
                for key, value in diffs.items():
                    if isinstance(key, Symbol): # character is action
                        next_action = key.label
                        self.apply_diffs_recursive(value, target, next_action, parsed_old_file, parsed_new_file)
                    elif isinstance(value, dict):
                        if isinstance(parsed_old_file, list) and isinstance(key,int):
                            if len(parsed_old_file) <= key:
                                self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file, parsed_new_file[key])
                            else:
                                self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key], parsed_new_file[key])
                        else:
                            print(target, key)
                            self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key], parsed_new_file[key])
                    elif isinstance(value, list):
                        for i, v in enumerate(value):
                            if isinstance(v, dict):
                                self.apply_diffs_recursive(v, target[key][i], current_action, parsed_old_file[key][i], parsed_new_file[key][i])
                            else:
                                target[key][i] = v
                    else:
                        # above should also add old version
                        # if key == "c" or key == "t":
                        #     target_copy = copy.deepcopy(target)
                        #     target['t'] = 'Underline'
                        #     target['c'] =  [target_copy]
                        continue

            elif current_action == "insert":
                print("----------INSERTING----------")
                print(f"diffs: {diffs}")

                for change in diffs:
                    position, value = change
                    print(f"target[position] {target[position]}")
                    to_insert = self.format_changes(target, position, "Underline")
                    parsed_old_file.insert(position, to_insert["c"][0])


            elif current_action == "delete":
                print("----------DELETE----------")
                diffs.reverse()
                print(f"diffs: {diffs}")
                for delete_position in diffs:
                    to_insert = self.format_changes(parsed_old_file, delete_position, "Strikeout")
                    target.insert(delete_position, to_insert)
                    parsed_new_file.insert(delete_position, to_insert['c'][0])
                    
        # except Exception as e:
        #     print(f"Parsing error: {e}")
        #     print(f"Skipping...")

def main():
    # later add paths from user arguments
    file_converter = FileConverter()
    file_converter.convert_with_pandoc('typst', 'json', 'new.typ', 'new.json')
    file_converter.convert_with_pandoc('typst', 'json', 'old.typ', 'old.json')
    comparison = Comparison("new.json", "old.json")
    comparison.parse()
    print(comparison.parsed_new_file)
    print(comparison.parsed_old_file)
    file_converter.write_to_json_file(comparison.parsed_changed_file, 'compared_new.json')
    print("zapisało")
    file_converter.convert_with_pandoc('json', 'typst', 'compared_new.json', 'compared_new.typ')
    # later add user arguments to format text
    format_lines = [f"#show underline : it => {{highlight(fill: teal,text(red, it))}}", f"#show strike : it => {{highlight(fill: green, text(yellow, it))}}"]
    file_converter.write_lines(format_lines, 'compared_new.typ')
    file_converter.compile_to_pdf("compared_new.typ")

if __name__ == "__main__":
    main()