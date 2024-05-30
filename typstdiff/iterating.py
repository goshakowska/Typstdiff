from jsondiff import diff
from jsondiff.symbols import Symbol

import json
import copy

class CouldNotParseFiles(Exception):
    pass

class InvalidJsonDiffOutput(Exception):
    pass

class Comparison:

    def __init__(self, new_path, old_path, insert_format="Underline", delete_format="Strikeout"):
        self.parsed_new_file = self.parse_load_file(new_path)
        self.parsed_old_file = self.parse_load_file(old_path)
        self.parsed_changed_file = self.parse_load_file(new_path)
        self.diffs = diff(self.parsed_old_file, self.parsed_changed_file, syntax='explicit', dump=False)
        self.insert_format = insert_format
        self.delete_format = delete_format

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
            "Math",
            "CodeBlock"
        }

        self.LIST_DICT_TYPES = {
            "Para",
            "BulletList",
            "OrderedList",
            "Div"
        }

        self.UPDATE_ONLY = {
            "Link",
            "Image",
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
                if target[position][i]['t'] in self.LIST_DICT_TYPES:
                    self.parse_list_dict(target[position][i], format_action)
                    to_insert = [target[position][i]]
        elif isinstance(target[position], dict) and target[position]["t"] == "Header":
            self.parse_header(target, position, format_action)
            to_insert = target[position]

        elif isinstance(target[position], dict) and target[position]['t'] in self.LIST_DICT_TYPES:
            self.parse_list_dict(target[position], format_action)
            to_insert = target[position]
        else:
            target_copy = copy.deepcopy(target[position])
            target[position] = {"t": format_action, "c": [target_copy]}
            to_insert = target[position]
        return to_insert

    def dict_depth(self, d, level=1):
        if not isinstance(d, dict) or not d:
            return level
        return max(self.dict_depth(v, level + 1) for k, v in d.items())

    def update_index(self, diffs):
        if len(list(diffs.values())) > 1 and all(isinstance(key, int) for key in diffs.keys()):
            new_diffs = {}
            to_add = 0
            for key, value in diffs.items():
                if not self.dict_depth(value) > 3:
                    new_diffs[(key, key+to_add)] = value
                    to_add += 1
                else:
                    new_diffs[key, key+to_add] = value
            return new_diffs
        return diffs

    def update(self, diffs, target, old_target, index):
        diffs = self.update_index(diffs)
        index, index_update = self.split_index_tuple(index)
        for key, value in diffs.items():
            if isinstance(target, list) and isinstance(target[index], dict) and target[index]["t"] in self.UPDATE_ONLY:
                target[index_update] = {"t": self.insert_format, "c": [target[index_update]]}
                target.insert(index_update, {"t": self.delete_format, "c": [old_target[index]]})
            elif (isinstance(value, list) and self.dict_depth(value[0]) or
                    self.dict_depth(value) == 2):
                print(f"VALUE {value}, {self.dict_depth(value)}")
                target_copy = copy.deepcopy(target[index_update])
                old_target_copy = copy.deepcopy(old_target[index])
                target[index_update] = {"t": self.delete_format, "c": [old_target_copy]}
                target.insert(index_update+1, {"t": self.insert_format, "c": [target_copy]})
            elif isinstance(key, Symbol):
                if key.label == 'update' and \
                   isinstance(list(value.values())[0], dict):
                    self.update(value, target, old_target, (index, index_update))
            else:
                self.update(value, target[index_update], old_target[index], key)

    def parse(self):
        try:
            if self.diffs:
                self.apply_diffs_recursive(self.diffs, self.parsed_changed_file, None, self.parsed_old_file, self.parsed_new_file, "insert")
            self.diffs = diff(self.parsed_old_file, self.parsed_new_file, syntax='explicit', dump=False)
            if self.diffs:
                self.apply_diffs_recursive(self.diffs, self.parsed_changed_file, None, self.parsed_old_file, self.parsed_new_file, "delete")
            self.diffs = diff(self.parsed_old_file, self.parsed_new_file, syntax='explicit', dump=False)
            if self.diffs:
                key = None
                while not isinstance(key, int):
                    for key, value in self.diffs.items():
                        if isinstance(key, int):
                            self.update(value, self.parsed_changed_file['blocks'], self.parsed_old_file['blocks'], key)
                        else:
                            self.diffs = value
        except (TypeError, IndexError) as e:
            raise InvalidJsonDiffOutput(f"Could not parse jsondiff output: {e}")
        except Exception as e:
            raise CouldNotParseFiles(f"Used type unsupported by pandoc: [{e}]")

    def split_index_tuple(self, index):
        if isinstance(index, tuple):
            return index[0], index[1]
        else:
            return index, index

    def process_insert(self, diffs, target, parsed_old_file):
        for change in diffs:
            position, _ = change
            target_position, position = self.split_index_tuple(position)
            to_insert = self.format_changes(target, target_position, self.insert_format)
            if isinstance(to_insert, list):
                to_insert = [self.remove_formatting(to_insert[0], self.insert_format)]
            else:
                to_insert = self.remove_formatting(to_insert, self.insert_format)
            parsed_old_file.insert(position, to_insert)

    def process_delete(self, diffs, target, parsed_old_file, parsed_new_file):
        diffs.reverse()
        print(f"diffs: {diffs}")
        for delete_position in diffs:
            to_insert = self.format_changes(parsed_old_file, delete_position, self.delete_format)
            target.insert(delete_position, to_insert)
            if isinstance(to_insert, list):
                to_insert = [self.remove_formatting(to_insert[0], self.delete_format)]
            else:
                to_insert = self.remove_formatting(to_insert, self.delete_format)
            parsed_old_file[delete_position] = to_insert
            parsed_new_file.insert(delete_position, to_insert)

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
            new_insert_diffs.append(((insert[0], insert[0] + len([num for num in delete_diffs if num < insert[0]])), insert[1]))
        for key, value in diffs.items():
            if isinstance(key, Symbol) and key.label == "insert":
                diffs[key] = new_insert_diffs
                break
        return diffs

    def sort_diffs(self, diffs):
        sorted_diffs = []
        for key, value in reversed(list(diffs.items())):
            if key == Symbol("insert"):
                sorted_diffs.insert(0, (key, value))
            else:
                sorted_diffs.append((key, value))
        return sorted_diffs

    def apply_diffs_recursive(self, diffs, target, current_action, parsed_old_file, parsed_new_file, only):
        if isinstance(diffs, dict):
            if all(elem in [symbol.label for symbol in list(diffs.keys()) if isinstance(symbol, Symbol)] for elem in ["insert", "delete"]):
                diffs = self.update_insert_indexes(diffs)

        if current_action is None or current_action == "update":
            print("----------UPDATING----------")
            print(f"diffs: {diffs}")
            print(target)
            print(f"OLD: {parsed_old_file}")
            sorted_diffs = self.sort_diffs(diffs)
            for key, value in sorted_diffs:
                if isinstance(key, Symbol):  # character is action
                    next_action = key.label
                    self.apply_diffs_recursive(value, target, next_action, parsed_old_file, parsed_new_file, only)
                elif isinstance(target, dict) and "t" in target.keys() and target["t"] in self.UPDATE_ONLY:
                    continue

                elif isinstance(value, dict):
                    if isinstance(parsed_old_file, list) and \
                            isinstance(key, int):
                        if len(parsed_old_file) <= key:
                            self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file, parsed_new_file[key], only)
                        else:
                            self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key], parsed_new_file[key], only)
                    else:
                        self.apply_diffs_recursive(value, target[key], current_action, parsed_old_file[key], parsed_new_file[key], only)
                elif isinstance(value, list):
                    for i, v in enumerate(value):
                        if isinstance(v, dict):
                                self.apply_diffs_recursive(v, target[key][i], current_action, parsed_old_file[key][i], parsed_new_file[key][i], only)
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
