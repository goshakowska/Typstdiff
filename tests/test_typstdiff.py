from typstdiff import __version__
import pytest
from typstdiff.file_converter import FileConverter
from typstdiff.comparison import Comparison
from typstdiff.main import get_file_path_without_extension


pytestmark = [
    pytest.mark.update,
    pytest.mark.delete,
    pytest.mark.insert
]


def test_typstdiff_version():
    assert __version__ == '0.1.0'

def perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file):
    old_v_file = get_file_path_without_extension(old_version_file)
    new_v_file = get_file_path_without_extension(new_version_file)
    diff_file = get_file_path_without_extension(diff_file)

    file_converter = FileConverter()
    file_converter.convert_with_pandoc('typst', 'json', f'./tests/test_working_types/{old_v_file}/{new_v_file}.typ', f'./tests/test_working_types/{old_v_file}/{new_v_file}.json')
    file_converter.convert_with_pandoc('typst', 'json', f'./tests/test_working_types/{old_v_file}/{old_v_file}.typ', f'./tests/test_working_types/{old_v_file}/{old_v_file}.json')
    comparison = Comparison(f'./tests/test_working_types/{old_v_file}/{new_v_file}.json', f'./tests/test_working_types/{old_v_file}/{old_v_file}.json')
    comparison.parse()
    return comparison.parsed_changed_file


@pytest.fixture
def setup_files_update(request):
    filename = request.param
    old_version_file = f'test_working_types/{filename}/{filename}.typ'
    new_version_file = f'test_working_types/{filename}/{filename}_updated.typ'
    diff_file = f'test_working_types/{filename}/{filename}_diff_updated.json'
    return old_version_file, new_version_file, diff_file


@pytest.fixture
def setup_files_delete(request):
    filename = request.param
    old_version_file = f'test_working_types/{filename}/{filename}.typ'
    new_version_file = f'test_working_types/{filename}/{filename}_deleted.typ'
    diff_file = f'test_working_types/{filename}/{filename}_diff_deleted.json'
    return old_version_file, new_version_file, diff_file


@pytest.fixture
def setup_files_insert(request):
    filename = request.param
    old_version_file = f'test_working_types/{filename}/{filename}.typ'
    new_version_file = f'test_working_types/{filename}/{filename}_inserted.typ'
    diff_file = f'test_working_types/{filename}/{filename}_diff_inserted.json'
    return old_version_file, new_version_file, diff_file


@pytest.mark.parametrize('setup_files_update', ['header'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_header(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"Header","c":[1,["",[],[]],[{"t":"Strikeout","c":[{"t":"Str","c":"Heading"}]}, {"t":"Underline","c":[{"t":"Str","c":"Updatedheading"}]}]]},{"t":"Header","c":[1,["",[],[]],[{"t":"Str","c":"Second"},{"t":"Space"},{"t":"Str","c":"heading"}]]}]}
    print(diff_json)
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['header'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_header(setup_files_delete):

    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {"pandoc-api-version": [1, 23, 1], "meta": {}, "blocks": [{"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading"}]]}, {"t": "Header", "c": [1, ["", [], []], [{"t": "Strikeout", "c": [{"t": "Str", "c": "Second"}]}, {"t": "Strikeout", "c": [{"t": "Space"}]}, {"t": "Strikeout", "c": [{"t": "Str", "c": "heading"}]}]]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['header'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_header(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Header', 'c': [1, ['', [], []], [{'t': 'Str', 'c': 'Heading'}]]}, {'t': 'Header', 'c': [1, ['', [], []], [{'t': 'Str', 'c': 'Second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'heading'}]]}, {'t': 'Header', 'c': [1, ['', [], []], [{'t': 'Underline', 'c': [{'t': 'Str', 'c': 'Inserted'}]}, {'t': 'Underline', 'c': [{'t': 'Space'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'heading'}]}]]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['link'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_link(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"Para","c":[{"t":"Strikeout","c":[{"t":"Link","c":[["",[],[]],[{"t":"Str","c":"https://typst.app/"}],["https://typst.app/",""]]}]},{"t":"Underline","c":[{"t":"Link","c":[["",[],[]],[{"t":"Str","c":"https://typst.app/docs/"}],["https://typst.app/docs/",""]]}]},{"t": "SoftBreak"},{"t":"Link","c":[["",[],[]],[{"t":"Str","c":"https://pl.wikipedia.org/"}],["https://pl.wikipedia.org/",""]]}]}]}
    assert diff_json == expected_json



@pytest.mark.parametrize('setup_files_delete', ['link'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_link(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Link', 'c': [['', [], []], [{'t': 'Str', 'c': 'https://typst.app/'}], ['https://typst.app/', '']]}, {'t': 'Strikeout', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Link', 'c': [['', [], []], [{'t': 'Str', 'c': 'https://pl.wikipedia.org/'}], ['https://pl.wikipedia.org/', '']]}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['link'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_link(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Link', 'c': [['', [], []], [{'t': 'Str', 'c': 'https://typst.app/'}], ['https://typst.app/', '']]}, {'t': 'SoftBreak'}, {'t': 'Link', 'c': [['', [], []], [{'t': 'Str', 'c': 'https://pl.wikipedia.org/'}], ['https://pl.wikipedia.org/', '']]}, {'t': 'Underline', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Link', 'c': [['', [], []], [{'t': 'Str', 'c': 'https://gitlab-stud.elka.pw.edu.pl/dferfeck/zprp-typstdiff'}], ['https://gitlab-stud.elka.pw.edu.pl/dferfeck/zprp-typstdiff', '']]}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['str'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_str(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"Para","c":[{"t":"Str","c":"First"},{"t":"Space"},{"t":"Strikeout","c":[{"t":"Str","c":"second"}]},{"t":"Underline","c":[{"t":"Str","c":"updated"}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['str'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_str(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Strikeout', 'c': [{'t': 'Space'}]}, {'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'second'}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['str'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_str(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Space'}, {'t': 'Str', 'c': 'second'}, {'t': 'Underline', 'c': [{'t': 'Space'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'third'}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['emph'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_emph(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"Para","c":[{"t":"Emph","c":[{"t":"Strikeout","c":[{"t":"Str","c":"first"}]}, {"t":"Underline","c":[{"t":"Str","c":"upgraded"}]},{"t":"Space"},{"t":"Str","c":"emphasis"}]},{"t":"SoftBreak"},{"t":"Emph","c":[{"t":"Str","c":"second"},{"t":"Space"},{"t":"Str","c":"emphasis"}]}]}]}
    assert diff_json == expected_json



@pytest.mark.parametrize('setup_files_delete', ['emph'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_emph(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Emph', 'c': [{'t': 'Str', 'c': 'first'}, {'t': 'Space'}, {'t': 'Str', 'c': 'emphasis'}]}, {'t': 'Strikeout', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Emph', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'emphasis'}]}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['emph'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_emph(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Emph', 'c': [{'t': 'Str', 'c': 'first'}, {'t': 'Space'}, {'t': 'Str', 'c': 'emphasis'}]}, {'t': 'SoftBreak'}, {'t': 'Emph', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'emphasis'}]}, {'t': 'Underline', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Emph', 'c': [{'t': 'Str', 'c': 'inserted'}, {'t': 'Space'}, {'t': 'Str', 'c': 'emphasis'}]}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['strong'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_strong(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Strong', 'c': [{'t': 'Str', 'c': 'first'}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'second'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'second_updated'}]}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'third'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'third_updated'}]}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Str', 'c': 'forth'}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['strong'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_strong(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Strong', 'c': [{'t': 'Str', 'c': 'first'}]}]}, {'t': 'Strikeout', 'c': [{'t': 'LineBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Strong', 'c': [{'t': 'Str', 'c': 'second'}]}]}, {'t': 'Strikeout', 'c': [{'t': 'LineBreak'}]}, {'t': 'Strong', 'c': [{'t': 'Str', 'c': 'third'}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Str', 'c': 'forth'}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['strong'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_strong(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Strong', 'c': [{'t': 'Str', 'c': 'first'}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Str', 'c': 'second'}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Str', 'c': 'third'}]}, {'t': 'LineBreak'}, {'t': 'Strong', 'c': [{'t': 'Str', 'c': 'forth'}]}, {'t': 'Underline', 'c': [{'t': 'LineBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Strong', 'c': [{'t': 'Str', 'c': 'fifth'}]}]}, {'t': 'Underline', 'c': [{'t': 'LineBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Strong', 'c': [{'t': 'Str', 'c': 'sixth'}]}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['super_script'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_superscript(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Superscript', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'super'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'updated'}]}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Normal'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Second'}, {'t': 'Superscript', 'c': [{'t': 'Str', 'c': 'super'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['super_script'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_superscript(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Strikeout', 'c': [{'t': 'Superscript', 'c': [{'t': 'Str', 'c': 'super'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Normal'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Second'}, {'t': 'Superscript', 'c': [{'t': 'Str', 'c': 'super'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['super_script'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_superscript(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Superscript', 'c': [{'t': 'Str', 'c': 'super'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Normal'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}, {'t': 'Underline', 'c': [{'t': 'Superscript', 'c': [{'t': 'Str', 'c': 'inserted'}, {'t': 'Space'}, {'t': 'Str', 'c': 'super'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Second'}, {'t': 'Superscript', 'c': [{'t': 'Str', 'c': 'super'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}]}

    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['sub_script'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_subscript(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Subscript', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'first'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'updated'}]}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Normal'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Second'}, {'t': 'Subscript', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['sub_script'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_subscript(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    print(diff_json)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Strikeout', 'c': [{'t': 'Subscript', 'c': [{'t': 'Str', 'c': 'first'}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Normal'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Second'}, {'t': 'Subscript', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['sub_script'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_subscript(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)

    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'First'}, {'t': 'Subscript', 'c': [{'t': 'Str', 'c': 'first'}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Normal'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}, {'t': 'Underline', 'c': [{'t': 'Subscript', 'c': [{'t': 'Str', 'c': 'inserted'}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}, {'t': 'SoftBreak'}, {'t': 'Str', 'c': 'Second'}, {'t': 'Subscript', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'sub'}, {'t': 'Space'}, {'t': 'Str', 'c': 'text'}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['quoted'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_quoted(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'I'}, {'t': 'Space'}, {'t': 'Str', 'c': 'know'}, {'t': 'Space'}, {'t': 'Str', 'c': 'that'}, {'t': 'Underline', 'c': [{'t': 'Space'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'this'}]}, {'t': 'Space'}, {'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'I'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'quote'}]}, {'t': 'Space'}, {'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'know'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'was'}]}, {'t': 'Space'}, {'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'nothing.'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'updated.'}]}]]}, {'t': 'SoftBreak'}, {'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'Only'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'dead'}, {'t': 'Space'}, {'t': 'Str', 'c': 'have'}, {'t': 'Space'}, {'t': 'Str', 'c': 'seen'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'end'}, {'t': 'Space'}, {'t': 'Str', 'c': 'of'}, {'t': 'Space'}, {'t': 'Str', 'c': 'war.'}]]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['quoted'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_quoted(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'I'}, {'t': 'Space'}, {'t': 'Str', 'c': 'know'}, {'t': 'Space'}, {'t': 'Str', 'c': 'that'}, {'t': 'Space'}, {'t': 'Str', 'c': 'I'}, {'t': 'Space'}, {'t': 'Str', 'c': 'know'}, {'t': 'Space'}, {'t': 'Str', 'c': 'nothing.'}]]}, {'t': 'Strikeout', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'Only'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'dead'}, {'t': 'Space'}, {'t': 'Str', 'c': 'have'}, {'t': 'Space'}, {'t': 'Str', 'c': 'seen'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'end'}, {'t': 'Space'}, {'t': 'Str', 'c': 'of'}, {'t': 'Space'}, {'t': 'Str', 'c': 'war.'}]]}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['quoted'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_quoted(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'I'}, {'t': 'Space'}, {'t': 'Str', 'c': 'know'}, {'t': 'Space'}, {'t': 'Str', 'c': 'that'}, {'t': 'Space'}, {'t': 'Str', 'c': 'I'}, {'t': 'Space'}, {'t': 'Str', 'c': 'know'}, {'t': 'Space'}, {'t': 'Str', 'c': 'nothing.'}]]}, {'t': 'SoftBreak'}, {'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'Only'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'dead'}, {'t': 'Space'}, {'t': 'Str', 'c': 'have'}, {'t': 'Space'}, {'t': 'Str', 'c': 'seen'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'end'}, {'t': 'Space'}, {'t': 'Str', 'c': 'of'}, {'t': 'Space'}, {'t': 'Str', 'c': 'war.'}]]}, {'t': 'Underline', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Quoted', 'c': [{'t': 'DoubleQuote'}, [{'t': 'Str', 'c': 'Ignorance,'}, {'t': 'Space'}, {'t': 'Str', 'c': 'the'}, {'t': 'Space'}, {'t': 'Str', 'c': 'root'}, {'t': 'Space'}, {'t': 'Str', 'c': 'and'}, {'t': 'Space'}, {'t': 'Str', 'c': 'stem'}, {'t': 'Space'}, {'t': 'Str', 'c': 'of'}, {'t': 'Space'}, {'t': 'Str', 'c': 'every'}, {'t': 'Space'}, {'t': 'Str', 'c': 'evil.'}]]}]}]}]}
    assert diff_json == expected_json


# @pytest.mark.parametrize('setup_files_update', ['code'], indirect=True)
# @pytest.mark.update
# def test_typstdiff_update_code(setup_files_update):
#     old_version_file, new_version_file, diff_file = setup_files_update
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json =  {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"Para","c":[{"t":"Strikeout","c":[{"t":"Code","c":[["",[],[]],"print(\"first line\")"]}]},{"t":"SoftBreak"},{"t":"Underline","c":[{"t":"Code","c":[["",[],[]],"print(\"updated line\")"]}]},{"t":"SoftBreak"},{"t":"Code","c":[["",[],[]],"print(\"second line\")"]}]}]}
#     assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['code'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_code(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Code', 'c': [['', [], []], 'print("first line")']}, {'t': 'Strikeout', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Code', 'c': [['', [], []], 'print("second line")']}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['code'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_code(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Code', 'c': [['', [], []], 'print("first line")']}, {'t': 'SoftBreak'}, {'t': 'Code', 'c': [['', [], []], 'print("second line")']}, {'t': 'Underline', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Code', 'c': [['', [], []], 'print("third line")']}]}]}]}
    assert diff_json == expected_json


# @pytest.mark.parametrize('setup_files_update', ['space'], indirect=True) #TODO
# @pytest.mark.update
# def test_typstdiff_update_space(setup_files_update):
#     old_version_file, new_version_file, diff_file = setup_files_update
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json = {}
#     assert diff_json == expected_json


# @pytest.mark.parametrize('setup_files_delete', ['space'], indirect=True)
# @pytest.mark.delete
# def test_typstdiff_delete_space(setup_files_delete):
#     old_version_file, new_version_file, diff_file = setup_files_delete
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'FirstSpace'}]}, {'t': 'Strikeout', 'c': [{'t': 'Space'}]}, {'t': 'Str', 'c': 'FirstSpaceSecondSpace'}]}]}
#     assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['space'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_space(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'FirstSpace'}, {'t': 'Space'}, {'t': 'Str', 'c': 'SecondSpace'}]}]}
    assert diff_json == expected_json


# @pytest.mark.parametrize('setup_files_update', ['line_break'], indirect=True) # does not work solely on line breaks
# @pytest.mark.update
# def test_typstdiff_update_linebreak(setup_files_update):
#     old_version_file, new_version_file, diff_file = setup_files_update
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json = {}
#     assert diff_json == expected_json


# line break by itself (deleted, inserted and updated) is not marked! FIXME!
# @pytest.mark.parametrize('setup_files_delete', ['line_break'], indirect=True)
# @pytest.mark.delete
# def test_typstdiff_delete_linebreak(setup_files_delete):
#     old_version_file, new_version_file, diff_file = setup_files_delete
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Math', 'c': [{'t': 'InlineMath'}, 'z - x = y']}, {'t': 'SoftBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, '\\longrightarrow']}, {'t': 'LineBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, 'x + y = z']}, {'t': 'SoftBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, 'a + b = c']}]}]}
#     assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['line_break'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_linebreak(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Math', 'c': [{'t': 'InlineMath'}, 'z - x = y']}, {'t': 'LineBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, '\\longrightarrow']}, {'t': 'LineBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, 'x + y = z']}, {'t': 'SoftBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, 'a + b = c']}, {'t': 'Underline', 'c': [{'t': 'LineBreak'}]}]}]}
    assert diff_json == expected_json


# @pytest.mark.parametrize('setup_files_update', ['inline_math'], indirect=True)
# @pytest.mark.update
# def test_typstdiff_update_inlinemath(setup_files_update):
#     old_version_file, new_version_file, diff_file = setup_files_update
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json = {"pandoc-api-version": [1, 23, 1], "meta": {}, "blocks": [{"t": "Para", "c": [{"t": "Strikeout", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "Q = \\rho Av + C"]}]}, {"t": "Underline", "c": [{"t": "SoftBreak"}]}, {"t": "Underline", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "Q = \\left| {B + C} \\right|"]}]}, {"t": "SoftBreak"}, {"t": "Math", "c": [{"t": "InlineMath"}, "a^{2} + b^{2} = c^{2}"]}]}]}
#     assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['inline_math'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_inlinemath(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Math', 'c': [{'t': 'InlineMath'}, 'Q = \\rho Av + C']}, {'t': 'Strikeout', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Math', 'c': [{'t': 'InlineMath'}, 'A^{2} + B^{2} = C^{2}']}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['inline_math'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_inlinemath(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Math', 'c': [{'t': 'InlineMath'}, 'Q = \\rho Av + C']}, {'t': 'SoftBreak'}, {'t': 'Math', 'c': [{'t': 'InlineMath'}, 'A^{2} + B^{2} = C^{2}']}, {'t': 'Underline', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Math', 'c': [{'t': 'InlineMath'}, 'm \\ast \\frac{V^{2}}{2}']}]}]}]}
    assert diff_json == expected_json


# @pytest.mark.parametrize('setup_files_update', ['display_math'], indirect=True)
# @pytest.mark.update
# def test_typstdiff_update_displaymath(setup_files_update):
#     old_version_file, new_version_file, diff_file = setup_files_update
#     diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
#     expected_json = {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"Para","c":[{"t":"Strikeout","c":[{"t":"Math","c":[{"t":"DisplayMath"},"Q = \\rho Av + C"]}]}, {"t": "Underline", "c": [{"t": "SoftBreak"}]}, {"t":"Underline","c":[{"t":"Math","c":[{"t":"DisplayMath"},"Q = \\left| {B + C} \\right|"]}]},{"t":"SoftBreak"},{"t":"Math","c":[{"t":"DisplayMath"},"a^{2} + b^{2} = c^{2}"]}]}]}
#     assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_delete', ['display_math'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_displaymath(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Math', 'c': [{'t': 'DisplayMath'}, 'Q = \\rho Av + C']}, {'t': 'Strikeout', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Strikeout', 'c': [{'t': 'Math', 'c': [{'t': 'DisplayMath'}, 'a^{2} + b^{2} = c^{2}']}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['display_math'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_displaymath(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'Para', 'c': [{'t': 'Math', 'c': [{'t': 'DisplayMath'}, 'Q = \\rho Av + C']}, {'t': 'SoftBreak'}, {'t': 'Math', 'c': [{'t': 'DisplayMath'}, 'a^{2} + b^{2} = c^{2}']}, {'t': 'Underline', 'c': [{'t': 'SoftBreak'}]}, {'t': 'Underline', 'c': [{'t': 'Math', 'c': [{'t': 'DisplayMath'}, 'm \\ast \\frac{V^{2}}{2}']}]}]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['bullet_list'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_bulletlist(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'BulletList', 'c': [[{'t': 'Para', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'first'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'updated'}]}, {'t': 'Space'}, {'t': 'Str', 'c': 'item'}]}], [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'item'}]}]]}]}
    assert diff_json == expected_json



@pytest.mark.parametrize('setup_files_delete', ['bullet_list'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_bulletlist(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'BulletList', 'c': [[{'t': 'Para', 'c': [{'t': 'Str', 'c': 'first'}, {'t': 'Space'}, {'t': 'Str', 'c': 'item'}]}], [{'t': 'Para', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'second'}]}, {'t': 'Strikeout', 'c': [{'t': 'Space'}]}, {'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'item'}]}]}]]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['bullet_list'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_bulletlist(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'BulletList', 'c': [[{'t': 'Para', 'c': [{'t': 'Str', 'c': 'first'}, {'t': 'Space'}, {'t': 'Str', 'c': 'item'}]}], [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'second'}, {'t': 'Space'}, {'t': 'Str', 'c': 'item'}]}], [{'t': 'Para', 'c': [{'t': 'Underline', 'c': [{'t': 'Str', 'c': 'inserted'}]}, {'t': 'Underline', 'c': [{'t': 'Space'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'item'}]}]}]]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_update', ['ordered_list'], indirect=True)
@pytest.mark.update
def test_typstdiff_update_orderedlist(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {"pandoc-api-version":[1,23,1],"meta":{},"blocks":[{"t":"OrderedList","c":[[1,{"t":"DefaultStyle"},{"t":"DefaultDelim"}],[[{"t":"Para","c":[{"t":"Str","c":"The"},{"t":"Space"},{"t":"Strikeout","c":[{"t":"Str","c":"first"}]},{"t":"Underline","c":[{"t":"Str","c":"updated"}]}]}],[{"t":"Para","c":[{"t":"Str","c":"The"},{"t":"Space"},{"t":"Str","c":"second"}]}]]]}]}
    assert diff_json == expected_json



@pytest.mark.parametrize('setup_files_delete', ['ordered_list'], indirect=True)
@pytest.mark.delete
def test_typstdiff_delete_orderedlist(setup_files_delete):
    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'OrderedList', 'c': [[1, {'t': 'DefaultStyle'}, {'t': 'DefaultDelim'}], [[{'t': 'Para', 'c': [{'t': 'Str', 'c': 'The'}, {'t': 'Space'}, {'t': 'Str', 'c': 'first'}]}], [{'t': 'Para', 'c': [{'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'The'}]}, {'t': 'Strikeout', 'c': [{'t': 'Space'}]}, {'t': 'Strikeout', 'c': [{'t': 'Str', 'c': 'second'}]}]}]]]}]}
    assert diff_json == expected_json


@pytest.mark.parametrize('setup_files_insert', ['ordered_list'], indirect=True)
@pytest.mark.insert
def test_typstdiff_insert_orderedlist(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file)
    expected_json = {'pandoc-api-version': [1, 23, 1], 'meta': {}, 'blocks': [{'t': 'OrderedList', 'c': [[1, {'t': 'DefaultStyle'}, {'t': 'DefaultDelim'}], [[{'t': 'Para', 'c': [{'t': 'Str', 'c': 'The'}, {'t': 'Space'}, {'t': 'Str', 'c': 'first'}]}], [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'The'}, {'t': 'Space'}, {'t': 'Str', 'c': 'second'}]}], [{'t': 'Para', 'c': [{'t': 'Underline', 'c': [{'t': 'Str', 'c': 'The'}]}, {'t': 'Underline', 'c': [{'t': 'Space'}]}, {'t': 'Underline', 'c': [{'t': 'Str', 'c': 'third'}]}]}]]]}]}
    assert diff_json == expected_json
