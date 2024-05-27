from jsondiff import diff
from jsondiff.symbols import Symbol

import json
import copy


class Comparison:

    def __init__(self, new_path, old_path):
        self.parsed_new_file = self.parse_load_file(new_path)
        self.parsed_old_file = self.parse_load_file(old_path)
        self.parsed_changed_file = self.parse_load_file(new_path)
        self.diffs = diff(self.parsed_old_file,
                          self.parsed_changed_file,
                          syntax='explicit',
                          dump=False)

        self.PARAGRAPH_TYPES = {
            dict: lambda para: para["c"] if "c" in para.keys() else para,
            list: lambda para: para
            }

        self.PARSERS_TYPES = {
            dict: lambda a: a,
            list: lambda a: a
        }

        self.DICT_TYPES = {
            "Link",
            "Math",
            "Str",
            "Emph",
            "Strong",
            "Superscript",
            "Subscript",
            "SmallCaps",
            "Quoted",
            "Cite",
            "Code",
            "Space",
            "SoftBreak",
            "LineBreak",
            "InlineMath"
        }

    def parse_load_file(self, path):
        try:
            with open(path, 'rb') as file:
                return json.load(file)
        except:  # TODO! Implement parsing erro
            pass

    def decorator_format_para(func):
        def wrapper(self, para, underline_strike):
            print(f"Applying decorator to paragraph: {para}")
            para_type = type(para)
            if para_type in self.PARAGRAPH_TYPES:
                para = self.PARAGRAPH_TYPES[para_type](para)
                return func(self, para, underline_strike)
            else:
                print(f"Unsupported type for para: {type(para)}")
                return None
        return wrapper

    def parse_dict(self, dict, underline_strike):
        print(f"parse_dict: {dict}")
        if dict["t"] in self.DICT_TYPES:
            para_copy = copy.deepcopy(dict)
            dict['t'] = underline_strike
            dict["c"] = [para_copy]
        elif dict["t"] in ("DefaultStyle",
                           "DefaultDelim",
                           "DisplayMath"):  # just skip ... for now
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

    def format_changes(self, target, position, format_action):
        print(target)
        if isinstance(target[position], list):
            for i in range(len(target[position])):
                if target[position][i]['t'] in ("Para", "BulletList"):
                    self.parse_list_dict(target[position][i], format_action)
                    # if delete then return insert
                    to_insert = [target[position][i]]
        elif target[position]['t'] in ("Para",
                                       "BulletList",
                                       "OrderedList",
                                       "Div",
                                       "CodeBlock"):
            self.parse_list_dict(target[position], format_action)
            to_insert = target[position]
        else:
            target_copy = copy.deepcopy(target[position])
            target[position] = {"t": format_action, "c": [target_copy]}
            to_insert = target[position]
            print(target, position, to_insert, format_action)
        return to_insert

    def update(self, diffs, target, old_target, index):
        print(f"UPDATE {diffs} {index}")
        print(f"TARGET {target}")
        if len(list(diffs.values())) > 1 and all(isinstance(key, int)
                                                 for key in diffs.keys()):
            new_diffs = {}
            for to_add, (key, value) in enumerate(diffs.items()):
                new_diffs[(key, key+to_add)] = value
            diffs = new_diffs
        if isinstance(index, tuple):
            index_update = index[1]
            index = index[0]
        else:
            index_update = index
        if isinstance(target, list) and target[index]["t"] in ["Link"]:
            target.insert(index+1, {"t": "Underline", "c": [target[index]]})
            target[index] = {"t": "Strikeout", "c": [old_target[index]]}
        else:
            for key, value in diffs.items():
                print(key, value)
                if (isinstance(value, list) and isinstance(value[0], dict) and
                        not isinstance(list(value[0].values())[0], dict)) or \
                        (isinstance(value, dict) and
                         not isinstance(list(value.values())[0], dict)):
                    target_copy = copy.deepcopy(target[index_update])
                    old_target_copy = copy.deepcopy(old_target[index])
                    target[index_update] = {"t": "Strikeout",
                                            "c": [old_target_copy]
                                            }
                    target.insert(index_update+1, {"t": "Underline",
                                                   "c": [target_copy]})
                elif isinstance(key, Symbol):
                    if key.label == 'update' and \
                       isinstance(list(value.values())[0], dict):
                        self.update(value, target, old_target, index)
                else:
                    self.update(value,
                                target[index_update],
                                old_target[index],
                                key)

    def parse(self):
        if self.diffs:
            self.apply_diffs_recursive(self.diffs,
                                       self.parsed_changed_file,
                                       None,
                                       self.parsed_old_file,
                                       self.parsed_new_file)
        self.diffs = diff(self.parsed_old_file,
                          self.parsed_new_file,
                          syntax='explicit',
                          dump=False)
        print(f"NEW DIFFS: {self.diffs}")
        if self.diffs:
            key = None
            while not isinstance(key, int):
                for key, value in self.diffs.items():
                    if isinstance(key, int):
                        self.update(value,
                                    self.parsed_changed_file['blocks'],
                                    self.parsed_old_file['blocks'],
                                    key)
                    else:
                        self.diffs = value

    def process_insert(self, diffs, target, parsed_old_file):
        for change in diffs:
            position, _ = change
            to_insert = self.format_changes(target, position, "Underline")
            if isinstance(to_insert, list):
                to_insert = [self.remove_formatting(to_insert[0],
                                                    "Underline")]
            else:
                to_insert = self.remove_formatting(to_insert, "Underline")
            parsed_old_file.insert(position, to_insert)

    def process_delete(self, diffs, target, parsed_old_file, parsed_new_file):
        diffs.reverse()
        print(f"diffs: {diffs}")
        for delete_position in diffs:
            to_insert = self.format_changes(parsed_old_file,
                                            delete_position,
                                            "Strikeout")
            print(parsed_old_file)

            target.insert(delete_position, to_insert)
            if isinstance(to_insert, list):
                to_insert = [self.remove_formatting(to_insert[0],
                                                    "Strikeout")]
            else:
                to_insert = self.remove_formatting(to_insert, "Strikeout")
            parsed_new_file.insert(delete_position, to_insert)
            parsed_old_file[delete_position] = to_insert

    def apply_diffs_recursive(self, diffs,
                              target, current_action,
                              parsed_old_file, parsed_new_file):
        # print(target)
        # try:
        if current_action is None or current_action == "update":
            print("----------UPDATING----------")
            print(f"diffs: {diffs}")
            print(target)
            for key, value in diffs.items():
                if key == "c" and target["t"] in ["Link"]:
                    continue
                elif isinstance(key, Symbol):  # character is action
                    next_action = key.label
                    self.apply_diffs_recursive(value, target,
                                               next_action, parsed_old_file,
                                               parsed_new_file)
                elif isinstance(value, dict):
                    if isinstance(parsed_old_file, list) and \
                            isinstance(key, int):
                        if len(parsed_old_file) <= key:
                            self.apply_diffs_recursive(
                                value,
                                target[key],
                                current_action,
                                parsed_old_file,
                                parsed_new_file[key])
                        else:
                            self.apply_diffs_recursive(value, target[key],
                                                       current_action,
                                                       parsed_old_file[key],
                                                       parsed_new_file[key])
                    else:
                        self.apply_diffs_recursive(value, target[key],
                                                   current_action,
                                                   parsed_old_file[key],
                                                   parsed_new_file[key])
                elif isinstance(value, list):
                    for i, v in enumerate(value):
                        if isinstance(v, dict):
                            self.apply_diffs_recursive(v, target[key][i],
                                                       current_action,
                                                       parsed_old_file[key][i],
                                                       parsed_new_file[key][i])
                        else:
                            target[key][i] = v

        elif current_action == "insert":
            print("----------INSERTING----------")
            print(f"diffs: {diffs}")
            self.process_insert(diffs, target, parsed_old_file)

        elif current_action == "delete":
            print("----------DELETE----------")
            self.process_delete(diffs, target, parsed_old_file,
                                parsed_new_file)

    def remove_formatting(self, data, formatting):
        if isinstance(data, dict):
            if data.get('t') == formatting:
                return data.get('c')[0]
            else:
                return {key: self.remove_formatting(value, formatting) for
                        key, value in data.items()}
        elif isinstance(data, list):
            return [self.remove_formatting(item, formatting) for item in data]
        else:
            return data
