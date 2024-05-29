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
            "Math"
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

    def parse_header(self, target, position, format_action):
        print(f"parsing header {target[position]}")
        for i in range(len(target[position]["c"])):
            if isinstance(target[position]["c"][i], list):
                for k in range(len(target[position]["c"][i])):
                    if isinstance(target[position]["c"][i][k], dict):
                        target_copy = copy.deepcopy(
                            target[position]["c"][i][k]
                            )
                        target[position]["c"][i][k]['t'] = format_action
                        target[position]["c"][i][k]['c'] = [target_copy]

    def format_changes(self, target, position, format_action):
        print(target, position)
        if isinstance(target[position], list):
            for i in range(len(target[position])):
                if target[position][i]['t'] in ("Para", "BulletList"):
                    self.parse_list_dict(target[position][i], format_action)
                    # if delete then return insert
                    to_insert = [target[position][i]]
        elif isinstance(target[position], dict) and target[position]["t"] == "Header":
            self.parse_header(target, position, format_action)
            to_insert = target[position]

        elif isinstance(target[position], dict) and target[position]['t'] in ("Para",
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

    def dict_depth(self, d, level=1):
        if not isinstance(d, dict) or not d:
            return level
        return max(self.dict_depth(v, level + 1) for k, v in d.items())

    def update(self, diffs, target, old_target, index):

        if len(list(diffs.values())) > 1 and all(isinstance(key, int)
                                                 for key in diffs.keys()):
            new_diffs = {}
            to_add = 0
            for key, value in diffs.items():
                print(value, self.dict_depth(value))
                if not self.dict_depth(value) > 3:
                    new_diffs[(key, key+to_add)] = value
                    to_add += 1
                else:
                    new_diffs[key, key+to_add] = value
            diffs = new_diffs
        print(diffs)
        print(index)
        if isinstance(index, tuple):
            index_update = index[1]
            index = index[0]
        else:
            index_update = index
        print(f"UPDATE {diffs} {index, index_update}")
        # print(f"TARGET {target}")
        # print(f"OLD_TARGET {old_target}")
        for key, value in diffs.items():
            print(key, value)
            if isinstance(target, list) and isinstance(target[index], dict) and target[index]["t"] in ["Link", "Image", "Math"]:
                print("LINK LUB IMAGE")
                target[index_update] = {"t": "Underline", "c": [target[index_update]]}
                target.insert(index_update, {"t": "Strikeout", "c": [old_target[index]]})

            elif (isinstance(value, list) and isinstance(value[0], dict) and
                    not isinstance(list(value[0].values())[0], dict)) or \
                    (isinstance(value, dict) and
                        not isinstance(list(value.values())[0], dict)):
                print("UPDATE ZWYKŁY")
                target_copy = copy.deepcopy(target[index_update])
                old_target_copy = copy.deepcopy(old_target[index])
                print(target_copy, old_target_copy)
                target[index_update] = {"t": "Strikeout",
                                        "c": [old_target_copy]
                                        }
                target.insert(index_update+1, {"t": "Underline",
                                               "c": [target_copy]})
            elif isinstance(key, Symbol):
                print("WEJŚCIE W SYMBOL")
                if key.label == 'update' and \
                   isinstance(list(value.values())[0], dict):
                    self.update(value, target, old_target, (index, index_update))
            else:
                print("ELSE")
                # print(f"OLD ELSE: {old_target}")
                # print(f"TARGET ELSE: {target}")
                print(f"INDEX: {index, index_update}")
                # print(target[index_update])
                # print(old_target[index])
                self.update(value,
                            target[index_update],
                            old_target[index],
                            key)

    def parse(self):
        if self.diffs:
            # self.diffs = self.update_insert_indexes(self.diffs)
            self.apply_diffs_recursive(self.diffs,
                                       self.parsed_changed_file,
                                       None,
                                       self.parsed_old_file,
                                       self.parsed_new_file, "insert")
        self.diffs = diff(self.parsed_old_file,
                          self.parsed_new_file,
                          syntax='explicit',
                          dump=False)
        print(f"DELETE DIFFS {self.diffs}")
        if self.diffs:
            self.apply_diffs_recursive(self.diffs,
                                       self.parsed_changed_file,
                                       None,
                                       self.parsed_old_file,
                                       self.parsed_new_file, "delete")
        print(f"OLD: {self.parsed_old_file}\n")
        print(f"NEW: {self.parsed_new_file}\n")
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
            if isinstance(position, tuple):
                target_position = position[0]
                position = position[1]
            else:
                target_position = position
            to_insert = self.format_changes(target, target_position, "Underline")
            if isinstance(to_insert, list):
                to_insert = [self.remove_formatting(to_insert[0],
                                                    "Underline")]
            else:
                to_insert = self.remove_formatting(to_insert, "Underline")
            parsed_old_file.insert(position, to_insert)
            print(f"PARSED OLD FILE: {parsed_old_file[position]}")

    def process_delete(self, diffs, target, parsed_old_file, parsed_new_file):
        diffs.reverse()
        print(f"diffs: {diffs}")
        # print(f"TARGET: {target}")
        # print(f"OLD FILE: {parsed_old_file}")
        # print(f"NEW FILE: {parsed_new_file}")
        # print(f"LEN:{to_add}")
        # to_add = []
        for delete_position in diffs:
            to_insert = self.format_changes(parsed_old_file,
                                            delete_position,
                                            "Strikeout")
            # print(parsed_old_file[delete_position])
            # print(target[delete_position])
            # print(parsed_new_file[delete_position])
            target.insert(delete_position, to_insert)
            if isinstance(to_insert, list):
                to_insert = [self.remove_formatting(to_insert[0],
                                                    "Strikeout")]
            else:
                to_insert = self.remove_formatting(to_insert, "Strikeout")
            parsed_old_file[delete_position] = to_insert
            parsed_new_file.insert(delete_position, to_insert)
            print(f"NOWE O {parsed_new_file[delete_position]}, {delete_position}")
        #     to_add.append(to_insert)
        # diffs.reverse()
        # # first = diffs[0]
        # print(f"TO_ADD: {to_add}")
        # for i, element in enumerate(reversed(to_add)):
        #     parsed_new_file.insert(diffs[-1], element)
        #     parsed_old_file[diffs[-1-i]] = to_add[i]
            # to_add = 0

    def update_insert_indexes(self, diffs):
        for key, value in diffs.items():
            if isinstance(key, int):
                pass
            elif key.label == "insert":
                insert_diffs = value
            elif key.label == "delete":
                delete_diffs = value
        new_insert_diffs = []
        for insert in insert_diffs:
            print(len([num for num in delete_diffs if num < insert[0]]))
            new_insert_diffs.append(((insert[0], insert[0] + len([num for num in delete_diffs if num < insert[0]])), insert[1]))
        for key, value in diffs.items():
            if isinstance(key, Symbol) and key.label == "insert":
                diffs[key] = new_insert_diffs
                break
        return diffs

    def apply_diffs_recursive(self, diffs,
                              target, current_action,
                              parsed_old_file, parsed_new_file, only):
        # print(target)
        # try:
        if isinstance(diffs, dict):
            if all(elem in [symbol.label for symbol in list(diffs.keys()) if isinstance(symbol, Symbol)] for elem in ["insert", "delete"]):
                diffs = self.update_insert_indexes(diffs)
                print(diffs)
                print("ZNALAZŁO")

        if current_action is None or current_action == "update":
            print("----------UPDATING----------")
            print(f"diffs: {diffs}")
            print(target)
            print(f"OLD: {parsed_old_file}")
            sorted_diffs = []
            for key, value in reversed(list(diffs.items())):
                if key == Symbol("delete"):
                    sorted_diffs.insert(0, (key, value))
                else:
                    sorted_diffs.append((key, value))
            print(sorted_diffs)
            for key, value in sorted_diffs:
                if isinstance(key, Symbol):  # character is action
                    next_action = key.label
                    self.apply_diffs_recursive(value, target,
                                            next_action, parsed_old_file,
                                            parsed_new_file, only)
                elif isinstance(target, dict) and "t" in target.keys() and target["t"] in ["Link", "Image", "Math"]:
                    continue

                elif isinstance(value, dict):
                    if isinstance(parsed_old_file, list) and \
                            isinstance(key, int):
                        if len(parsed_old_file) <= key:
                            self.apply_diffs_recursive(
                                value,
                                target[key],
                                current_action,
                                parsed_old_file,
                                parsed_new_file[key], only)
                        else:
                            self.apply_diffs_recursive(value, target[key],
                                                    current_action,
                                                    parsed_old_file[key],
                                                    parsed_new_file[key], only)
                    else:
                        self.apply_diffs_recursive(value, target[key],
                                                current_action,
                                                parsed_old_file[key],
                                                parsed_new_file[key], only)
                elif isinstance(value, list):
                    for i, v in enumerate(value):
                        if isinstance(v, dict):
                                self.apply_diffs_recursive(v, target[key][i],
                                                        current_action,
                                                        parsed_old_file[key][i],
                                                        parsed_new_file[key][i], only)
                        else:
                            target[key][i] = v

        elif current_action == "insert" and only == "insert":
            print("----------INSERTING----------")
            print(f"diffs: {diffs}")
            self.process_insert(diffs, target, parsed_old_file)

        elif current_action == "delete" and only == "delete":
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
