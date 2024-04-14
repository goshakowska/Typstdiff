from jsondiff import diff
import json

# dokumenty zamienione z typsta
with open('old_v.json', 'rb') as old_file:
    parsed_old_file = json.load(old_file)

with open('new_v.json', 'rb') as changed_file:
    parsed_changed_file = json.load(changed_file)

print(diff(parsed_old_file, parsed_changed_file, syntax='explicit', dump=True))


# # json niezmieniony
# with open('sample_old.json', 'rb') as original_file:
#     parsed_original_file = json.load(original_file)


# # json z samymi aktualizacjami
# with open('sample_updated.json', 'rb') as updated_file:
#     parsed_updated_file = json.load(updated_file)


# print(diff(parsed_original_file, parsed_updated_file, syntax='explicit'))


# # json z samymi usunięciami
# with open('sample_deleted.json', 'rb') as deleted_in_file:
#     parsed_deleted_in_file = json.load(deleted_in_file)


# print(diff(parsed_original_file, parsed_deleted_in_file, syntax='explicit'))


# # json z samymi dodanymi elementami
# with open('sample_added.json', 'rb') as added_to_file:
#     parsed_added_to_file = json.load(added_to_file)


# print(diff(parsed_original_file, parsed_added_to_file, syntax='explicit'))


# # json wiele modyfikacji
# with open('sample_many_modified.json', 'rb') as many_modifications_file:
#     parsed_many_modifications_file = json.load(many_modifications_file)


# modifications = diff(parsed_original_file, parsed_many_modifications_file, syntax='explicit')
