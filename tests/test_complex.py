import pytest
from typstdiff.file_converter import FileConverter
from typstdiff.comparison import Comparison
from typstdiff.main import get_file_path_without_extension
import json

pytestmark = [
    pytest.mark.update,
    pytest.mark.delete,
    pytest.mark.insert,
    pytest.mark.mix,
]


def perform_jsondiff_on_typst_files(old_version_file, new_version_file, diff_file):
    old_v_file = get_file_path_without_extension(old_version_file)
    new_v_file = get_file_path_without_extension(new_version_file)
    diff_file = get_file_path_without_extension(diff_file)

    file_converter = FileConverter()
    file_converter.convert_with_pandoc(
        "typst",
        "json",
        f"./tests/test_complex/{old_v_file}/{new_v_file}.typ",
        f"./tests/test_complex/{old_v_file}/{new_v_file}.json",
    )
    file_converter.convert_with_pandoc(
        "typst",
        "json",
        f"./tests/test_complex/{old_v_file}/{old_v_file}.typ",
        f"./tests/test_complex/{old_v_file}/{old_v_file}.json",
    )
    comparison = Comparison(
        f"./tests/test_complex/{old_v_file}/{new_v_file}.json",
        f"./tests/test_complex/{old_v_file}/{old_v_file}.json",
    )
    comparison.parse()
    return comparison.parsed_changed_file


@pytest.fixture
def setup_files_update(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_updated.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_updated.json"
    expected_file = f"test_complex/{filename}/{filename}_updated_expected.json"
    return old_version_file, new_version_file, diff_file, expected_file


@pytest.fixture
def setup_files_delete(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_deleted.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_deleted.json"
    expected_file = f"test_complex/{filename}/{filename}_deleted_expected.json"
    return old_version_file, new_version_file, diff_file, expected_file


@pytest.fixture
def setup_files_insert(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_inserted.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_inserted.json"
    expected_file = f"test_complex/{filename}/{filename}_inserted_expected.json"
    return old_version_file, new_version_file, diff_file, expected_file


@pytest.fixture
def setup_files_mix(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_mix.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_mix.json"
    expected_file = f"test_complex/{filename}/{filename}_mix_expected.json"
    return old_version_file, new_version_file, diff_file, expected_file


def create_result_files(diff_json, folder, json_filename, expected_file):
    with open(f"tests/test_complex/{folder}/{json_filename}.json", "w") as json_file:
        json.dump(diff_json, json_file)
    file_converter = FileConverter()
    file_converter.convert_with_pandoc(
        "json",
        "typst",
        f"./tests/test_complex/{folder}/{json_filename}.json",
        f"./tests/test_complex/{folder}/{json_filename}.typ",
    )
    with open(f"./tests/{expected_file}", "r") as file:
        expected_json = json.load(file)
    file_converter.compile_to_pdf(f"./tests/test_complex/{folder}/{json_filename}.typ")
    return expected_json


@pytest.mark.parametrize("setup_files_update", ["para"], indirect=True)
@pytest.mark.update
def test_complex_update_para(setup_files_update):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "para", "para_updated_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["para"], indirect=True)
@pytest.mark.delete
def test_complex_delete_para(setup_files_delete):

    old_version_file, new_version_file, diff_file, expected_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "para", "para_deleted_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["para"], indirect=True)
@pytest.mark.insert
def test_complex_insert_para(setup_files_insert):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "para", "para_inserted_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["para"], indirect=True)
@pytest.mark.mix
def test_complex_mix_para(setup_files_mix):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "para", "para_mix_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_update", ["ordered_list"], indirect=True)
@pytest.mark.update
def test_complex_update_ordered_list(setup_files_update):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "ordered_list", "ordered_list_updated_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["ordered_list"], indirect=True)
@pytest.mark.delete
def test_complex_delete_ordered_list(setup_files_delete):

    old_version_file, new_version_file, diff_file, expected_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "ordered_list", "ordered_list_deleted_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["ordered_list"], indirect=True)
@pytest.mark.insert
def test_complex_insert_ordered_list(setup_files_insert):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "ordered_list", "ordered_list_inserted_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["ordered_list"], indirect=True)
@pytest.mark.mix
def test_complex_mix_ordered_list(setup_files_mix):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "ordered_list", "ordered_list_mix_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_update", ["text_formats"], indirect=True)
@pytest.mark.update
def test_complex_update_text_formats(setup_files_update):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "text_formats", "text_formats_updated_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["text_formats"], indirect=True)
@pytest.mark.delete
def test_complex_delete_text_formats(setup_files_delete):

    old_version_file, new_version_file, diff_file, expected_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "text_formats", "text_formats_deleted_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["text_formats"], indirect=True)
@pytest.mark.insert
def test_complex_insert_text_formats(setup_files_insert):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "text_formats", "text_formats_inserted_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["text_formats"], indirect=True)
@pytest.mark.mix
def test_complex_mix_text_formats(setup_files_mix):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "text_formats", "text_formats_mix_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["all_types_working"], indirect=True)
@pytest.mark.delete
def test_complex_delete_all_types_working(setup_files_delete):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "all_types_working", "all_types_working_delete_result", expected_file
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_update", ["all_types_working"], indirect=True)
@pytest.mark.update
def test_complex_update_all_types_working(setup_files_update):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json,
        "all_types_working",
        "all_types_working_updated_result",
        expected_file,
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["all_types_working"], indirect=True)
@pytest.mark.insert
def test_complex_insert_all_types_working(setup_files_insert):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json,
        "all_types_working",
        "all_types_working_inserted_result",
        expected_file,
    )
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["all_types_working"], indirect=True)
@pytest.mark.mix
def test_complex_mix_all_types_working(setup_files_mix):
    old_version_file, new_version_file, diff_file, expected_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    expected_json = create_result_files(
        diff_json, "all_types_working", "all_types_working_mix_result", expected_file
    )
    assert diff_json == expected_json
