import pytest
from typstdiff.file_converter import FileConverter
from typstdiff.comparison import Comparison
from typstdiff.main import get_file_path_without_extension
import json

# ------------------------------------------------------------
# duplicated setup and fixtures - to improve later

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
    return old_version_file, new_version_file, diff_file


@pytest.fixture
def setup_files_delete(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_deleted.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_deleted.json"
    return old_version_file, new_version_file, diff_file


@pytest.fixture
def setup_files_insert(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_inserted.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_inserted.json"
    return old_version_file, new_version_file, diff_file


@pytest.fixture
def setup_files_mix(request):
    filename = request.param
    old_version_file = f"test_complex/{filename}/{filename}.typ"
    new_version_file = f"test_complex/{filename}/{filename}_mix.typ"
    diff_file = f"test_complex/{filename}/{filename}_diff_mix.json"
    return old_version_file, new_version_file, diff_file


# ------------------------------------------------------------


def create_result_files(diff_json, folder, json_filename):
    with open(f"tests/test_complex/{folder}/{json_filename}.json", "w") as json_file:
        json.dump(diff_json, json_file)
    file_converter = FileConverter()
    file_converter.convert_with_pandoc(
        "json",
        "typst",
        f"./tests/test_complex/{folder}/{json_filename}.json",
        f"./tests/test_complex/{folder}/{json_filename}.typ",
    )
    # file_converter.compile_to_pdf(f'./tests/test_complex/{folder}/{json_filename}.typ')


@pytest.mark.parametrize("setup_files_update", ["para"], indirect=True)
@pytest.mark.update
def test_complex_update_para(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "para", "para_updated_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "report,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Space"},
                    {
                        "t": "Emph",
                        "c": [
                            {"t": "Str", "c": "fluid"},
                            {"t": "SoftBreak"},
                            {"t": "Str", "c": "dynamics"},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "glaciers"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "ha"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "contribute"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "formation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "behaviour"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "these"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "natural"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "structures."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "All"},
                    {"t": "Space"},
                    {"t": "Str", "c": "manuscripts"},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "be"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "submitted"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "electronically"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ScholarOne"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Abstracts"},
                    {"t": "Space"},
                    {"t": "Str", "c": "site"},
                    {"t": "Space"},
                    {"t": "Str", "c": "created"},
                    {"t": "Space"},
                    {"t": "Str", "c": "for"},
                    {"t": "Space"},
                    {"t": "Str", "c": "each"},
                    {"t": "Space"},
                    {"t": "Str", "c": "conference."},
                    {"t": "Space"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "manuscript"},
                    {"t": "Space"},
                    {"t": "Str", "c": "upload"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "be"},
                    {"t": "Space"},
                    {"t": "Str", "c": "enabled"},
                    {"t": "Space"},
                    {"t": "Str", "c": "several"},
                    {"t": "Space"},
                    {"t": "Str", "c": "weeks"},
                    {"t": "Space"},
                    {"t": "Str", "c": "after"},
                    {"t": "Space"},
                    {"t": "Str", "c": "acceptance"},
                    {"t": "Space"},
                    {"t": "Str", "c": "notices"},
                    {"t": "Space"},
                    {"t": "Str", "c": "have"},
                    {"t": "Space"},
                    {"t": "Str", "c": "been"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sent."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Presenting"},
                    {"t": "Space"},
                    {"t": "Str", "c": "authors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "accepted"},
                    {"t": "Space"},
                    {"t": "Str", "c": "papers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "receive"},
                    {"t": "Space"},
                    {"t": "Str", "c": "an"},
                    {"t": "Space"},
                    {"t": "Str", "c": "email"},
                    {"t": "Space"},
                    {"t": "Str", "c": "with"},
                    {"t": "Space"},
                    {"t": "Str", "c": "instructions"},
                    {"t": "Space"},
                    {"t": "Str", "c": "when"},
                    {"t": "Space"},
                    {"t": "Str", "c": "manuscript"},
                    {"t": "Space"},
                    {"t": "Str", "c": "submission"},
                    {"t": "Space"},
                    {"t": "Str", "c": "opens."},
                    {"t": "Space"},
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "important"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "presenting"},
                    {"t": "Space"},
                    {"t": "Str", "c": "authors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "keep"},
                    {"t": "Space"},
                    {"t": "Str", "c": "their"},
                    {"t": "Space"},
                    {"t": "Str", "c": "email"},
                    {"t": "Space"},
                    {"t": "Str", "c": "addresses"},
                    {"t": "Space"},
                    {"t": "Str", "c": "up-to-date"},
                    {"t": "Space"},
                    {"t": "Str", "c": "so"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Space"},
                    {"t": "Str", "c": "not"},
                    {"t": "Space"},
                    {"t": "Str", "c": "miss"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "notice."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "responsibility"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "author"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "obtain"},
                    {"t": "Space"},
                    {"t": "Str", "c": "any"},
                    {"t": "Space"},
                    {"t": "Str", "c": "required"},
                    {"t": "Space"},
                    {"t": "Str", "c": "government"},
                    {"t": "Space"},
                    {"t": "Str", "c": "or"},
                    {"t": "Space"},
                    {"t": "Str", "c": "company"},
                    {"t": "Space"},
                    {"t": "Str", "c": "reviews"},
                    {"t": "Space"},
                    {"t": "Str", "c": "for"},
                    {"t": "Space"},
                    {"t": "Str", "c": "their"},
                    {"t": "Space"},
                    {"t": "Str", "c": "papers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "advance"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "publication."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Start"},
                    {"t": "Space"},
                    {"t": "Str", "c": "early"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "determine"},
                    {"t": "Space"},
                    {"t": "Str", "c": "if"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "reviews"},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "required;"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "process"},
                    {"t": "Space"},
                    {"t": "Str", "c": "can"},
                    {"t": "Space"},
                    {"t": "Str", "c": "take"},
                    {"t": "Space"},
                    {"t": "Str", "c": "several"},
                    {"t": "Space"},
                    {"t": "Str", "c": "weeks."},
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["para"], indirect=True)
@pytest.mark.delete
def test_complex_delete_para(setup_files_delete):

    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "para", "para_deleted_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "report,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Emph",
                                "c": [
                                    {"t": "Str", "c": "fluid"},
                                    {"t": "SoftBreak"},
                                    {"t": "Str", "c": "dynamics"},
                                ],
                            }
                        ],
                    },
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "glaciers"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "ha"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "they"}]},
                    {"t": "Strikeout", "c": [{"t": "SoftBreak"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "contribute"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "formation"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "and"}]},
                    {"t": "Strikeout", "c": [{"t": "SoftBreak"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "behaviour"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "these"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "natural"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "structures."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "All"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "manuscripts"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "are"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "be"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "submitted"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "electronically"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "ScholarOne"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Abstracts"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "site"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "created"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "for"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "each"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "conference."}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "manuscript"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "upload"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "be"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "enabled"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "several"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "weeks"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "after"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "acceptance"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "notices"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "have"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "been"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "sent."}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Presenting"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "authors"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "accepted"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "papers"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "receive"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "an"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "email"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "with"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "instructions"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "when"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "manuscript"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "submission"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "opens."}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "It"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "important"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "that"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "presenting"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "authors"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "keep"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "their"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "email"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "addresses"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "up-to-date"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "so"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "they"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "do"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "not"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "miss"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "this"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "notice."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "responsibility"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "author"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "obtain"},
                    {"t": "Space"},
                    {"t": "Str", "c": "any"},
                    {"t": "Space"},
                    {"t": "Str", "c": "required"},
                    {"t": "Space"},
                    {"t": "Str", "c": "government"},
                    {"t": "Space"},
                    {"t": "Str", "c": "or"},
                    {"t": "Space"},
                    {"t": "Str", "c": "company"},
                    {"t": "Space"},
                    {"t": "Str", "c": "reviews"},
                    {"t": "Space"},
                    {"t": "Str", "c": "for"},
                    {"t": "Space"},
                    {"t": "Str", "c": "their"},
                    {"t": "Space"},
                    {"t": "Str", "c": "papers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "advance"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "publication."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Start"},
                    {"t": "Space"},
                    {"t": "Str", "c": "early"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "determine"},
                    {"t": "Space"},
                    {"t": "Str", "c": "if"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "reviews"},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "required;"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "process"},
                    {"t": "Space"},
                    {"t": "Str", "c": "can"},
                    {"t": "Space"},
                    {"t": "Str", "c": "take"},
                    {"t": "Space"},
                    {"t": "Str", "c": "several"},
                    {"t": "Space"},
                    {"t": "Str", "c": "weeks."},
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["para"], indirect=True)
@pytest.mark.insert
def test_complex_insert_para(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "para", "para_inserted_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "report,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Space"},
                    {
                        "t": "Emph",
                        "c": [
                            {"t": "Str", "c": "fluid"},
                            {"t": "SoftBreak"},
                            {"t": "Str", "c": "dynamics"},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glaciers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ha"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "contribute"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "formation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "behaviour"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "these"},
                    {"t": "Space"},
                    {"t": "Str", "c": "natural"},
                    {"t": "Space"},
                    {"t": "Str", "c": "structures."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Something"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "new."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "All"},
                    {"t": "Space"},
                    {"t": "Str", "c": "manuscripts"},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "be"},
                    {"t": "Space"},
                    {"t": "Str", "c": "submitted"},
                    {"t": "Space"},
                    {"t": "Str", "c": "electronically"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ScholarOne"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Abstracts"},
                    {"t": "Space"},
                    {"t": "Str", "c": "site"},
                    {"t": "Space"},
                    {"t": "Str", "c": "created"},
                    {"t": "Space"},
                    {"t": "Str", "c": "for"},
                    {"t": "Space"},
                    {"t": "Str", "c": "each"},
                    {"t": "Space"},
                    {"t": "Str", "c": "conference."},
                    {"t": "Space"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "manuscript"},
                    {"t": "Space"},
                    {"t": "Str", "c": "upload"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "be"},
                    {"t": "Space"},
                    {"t": "Str", "c": "enabled"},
                    {"t": "Space"},
                    {"t": "Str", "c": "several"},
                    {"t": "Space"},
                    {"t": "Str", "c": "weeks"},
                    {"t": "Space"},
                    {"t": "Str", "c": "after"},
                    {"t": "Space"},
                    {"t": "Str", "c": "acceptance"},
                    {"t": "Space"},
                    {"t": "Str", "c": "notices"},
                    {"t": "Space"},
                    {"t": "Str", "c": "have"},
                    {"t": "Space"},
                    {"t": "Str", "c": "been"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sent."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Presenting"},
                    {"t": "Space"},
                    {"t": "Str", "c": "authors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "accepted"},
                    {"t": "Space"},
                    {"t": "Str", "c": "papers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "receive"},
                    {"t": "Space"},
                    {"t": "Str", "c": "an"},
                    {"t": "Space"},
                    {"t": "Str", "c": "email"},
                    {"t": "Space"},
                    {"t": "Str", "c": "with"},
                    {"t": "Space"},
                    {"t": "Str", "c": "instructions"},
                    {"t": "Space"},
                    {"t": "Str", "c": "when"},
                    {"t": "Space"},
                    {"t": "Str", "c": "manuscript"},
                    {"t": "Space"},
                    {"t": "Str", "c": "submission"},
                    {"t": "Space"},
                    {"t": "Str", "c": "opens."},
                    {"t": "Space"},
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "important"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "presenting"},
                    {"t": "Space"},
                    {"t": "Str", "c": "authors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "keep"},
                    {"t": "Space"},
                    {"t": "Str", "c": "their"},
                    {"t": "Space"},
                    {"t": "Str", "c": "email"},
                    {"t": "Space"},
                    {"t": "Str", "c": "addresses"},
                    {"t": "Space"},
                    {"t": "Str", "c": "up-to-date"},
                    {"t": "Space"},
                    {"t": "Str", "c": "so"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Space"},
                    {"t": "Str", "c": "not"},
                    {"t": "Space"},
                    {"t": "Str", "c": "miss"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "notice."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "responsibility"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "author"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "obtain"},
                    {"t": "Space"},
                    {"t": "Str", "c": "any"},
                    {"t": "Space"},
                    {"t": "Str", "c": "required"},
                    {"t": "Space"},
                    {"t": "Str", "c": "government"},
                    {"t": "Space"},
                    {"t": "Str", "c": "or"},
                    {"t": "Space"},
                    {"t": "Str", "c": "company"},
                    {"t": "Space"},
                    {"t": "Str", "c": "reviews"},
                    {"t": "Space"},
                    {"t": "Str", "c": "for"},
                    {"t": "Space"},
                    {"t": "Str", "c": "their"},
                    {"t": "Space"},
                    {"t": "Str", "c": "papers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "advance"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "publication."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Start"},
                    {"t": "Space"},
                    {"t": "Str", "c": "early"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "determine"},
                    {"t": "Space"},
                    {"t": "Str", "c": "if"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "reviews"},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "required;"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "process"},
                    {"t": "Space"},
                    {"t": "Str", "c": "can"},
                    {"t": "Space"},
                    {"t": "Str", "c": "take"},
                    {"t": "Space"},
                    {"t": "Str", "c": "several"},
                    {"t": "Space"},
                    {"t": "Str", "c": "weeks."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "New"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "paragraph."}]},
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["para"], indirect=True)
@pytest.mark.mix
def test_complex_mix_para(setup_files_mix):
    old_version_file, new_version_file, diff_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "para", "para_mix_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "report,"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed,"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "explore"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Space"},
                    {
                        "t": "Emph",
                        "c": [
                            {"t": "Str", "c": "fluid"},
                            {"t": "SoftBreak"},
                            {"t": "Str", "c": "dynamics"},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "glaciers"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "ha"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "they"}]},
                    {"t": "Strikeout", "c": [{"t": "SoftBreak"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "contribute"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "formation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "behaviour"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "these"},
                    {"t": "Space"},
                    {"t": "Str", "c": "natural"},
                    {"t": "Space"},
                    {"t": "Str", "c": "structures."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "All"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "manuscripts"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "are"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "be"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "submitted"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "electronically"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "ScholarOne"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Abstracts"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "site"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "created"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "for"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "each"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "conference."}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "manuscript"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "upload"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "be"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "enabled"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "several"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "weeks"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "after"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "acceptance"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "notices"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "have"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "been"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "sent."}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Presenting"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "authors"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "accepted"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "papers"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "receive"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "an"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "email"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "with"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "instructions"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "when"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "manuscript"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "submission"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "opens."}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "It"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "important"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "that"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "presenting"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "authors"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "keep"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "their"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "email"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "addresses"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "up-to-date"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "so"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "they"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "do"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "not"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "miss"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Something"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "this"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "new."}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "notice."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Monkey."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "All"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "are"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "be"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "It"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "electronically"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "site"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "created"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "for"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "each"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "conference."}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "manuscript"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "upload"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "responsibility"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "be"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "enabled"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "several"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "author"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "weeks"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "after"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "obtain"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "acceptance"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "any"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "notices"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "required"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "have"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "government"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "been"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "or"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "sent."}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "company"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Presenting"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "reviews"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "authors"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "for"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "their"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "accepted"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "papers"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "receive"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "an"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "email"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "with"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "instructions"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "when"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "manuscript"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "submission"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "opens."}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "advance"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "It"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "publication."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "important"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Start"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "that"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "early"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "presenting"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "authors"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "determine"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "keep"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "if"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "their"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "email"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "reviews"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "addresses"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "are"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "up-to-date"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "required;"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "so"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "this"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "they"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "process"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "do"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "can"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "not"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "take"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "miss"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "several"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "this"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "weeks."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "notice."}]},
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_update", ["ordered_list"], indirect=True)
@pytest.mark.update
def test_complex_update_ordered_list(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "ordered_list", "ordered_list_updated_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "OrderedList",
                "c": [
                    [1, {"t": "DefaultStyle"}, {"t": "DefaultDelim"}],
                    [
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "The"},
                                    {"t": "Space"},
                                    {
                                        "t": "Strikeout",
                                        "c": [{"t": "Str", "c": "climate"}],
                                    },
                                    {
                                        "t": "Underline",
                                        "c": [{"t": "Str", "c": "CLIMATE"}],
                                    },
                                ],
                            },
                            {
                                "t": "BulletList",
                                "c": [
                                    [
                                        {
                                            "t": "Para",
                                            "c": [
                                                {
                                                    "t": "Strikeout",
                                                    "c": [
                                                        {
                                                            "t": "Str",
                                                            "c": "Precipitation",
                                                        }
                                                    ],
                                                },
                                                {
                                                    "t": "Underline",
                                                    "c": [
                                                        {
                                                            "t": "Str",
                                                            "c": "Precipitation2",
                                                        }
                                                    ],
                                                },
                                            ],
                                        }
                                    ],
                                    [
                                        {
                                            "t": "Para",
                                            "c": [{"t": "Str", "c": "Temperature"}],
                                        },
                                        {
                                            "t": "OrderedList",
                                            "c": [
                                                [
                                                    1,
                                                    {"t": "DefaultStyle"},
                                                    {"t": "DefaultDelim"},
                                                ],
                                                [
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Str",
                                                                    "c": "degree",
                                                                }
                                                            ],
                                                        },
                                                        {
                                                            "t": "BulletList",
                                                            "c": [
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Strikeout",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "hot",
                                                                                    }
                                                                                ],
                                                                            },
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "cold",
                                                                                    }
                                                                                ],
                                                                            },
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "really",
                                                                                    }
                                                                                ],
                                                                            },
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Space"
                                                                                    }
                                                                                ],
                                                                            },
                                                                            {
                                                                                "t": "Strikeout",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "cold",
                                                                                    }
                                                                                ],
                                                                            },
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "hot",
                                                                                    }
                                                                                ],
                                                                            },
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "warm",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                            ],
                                                        },
                                                    ],
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Strikeout",
                                                                    "c": [
                                                                        {
                                                                            "t": "Str",
                                                                            "c": "sun",
                                                                        }
                                                                    ],
                                                                },
                                                                {
                                                                    "t": "Underline",
                                                                    "c": [
                                                                        {
                                                                            "t": "Str",
                                                                            "c": "rain",
                                                                        }
                                                                    ],
                                                                },
                                                            ],
                                                        }
                                                    ],
                                                ],
                                            ],
                                        },
                                    ],
                                ],
                            },
                        ],
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "The"},
                                    {"t": "Space"},
                                    {
                                        "t": "Strikeout",
                                        "c": [{"t": "Str", "c": "geology"}],
                                    },
                                    {
                                        "t": "Underline",
                                        "c": [{"t": "Str", "c": "GEOLOGY"}],
                                    },
                                ],
                            }
                        ],
                    ],
                ],
            }
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["ordered_list"], indirect=True)
@pytest.mark.delete
def test_complex_delete_ordered_list(setup_files_delete):

    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "ordered_list", "ordered_list_deleted_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "OrderedList",
                "c": [
                    [1, {"t": "DefaultStyle"}, {"t": "DefaultDelim"}],
                    [
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "The"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "climate"},
                                ],
                            },
                            {
                                "t": "BulletList",
                                "c": [
                                    [
                                        {
                                            "t": "Para",
                                            "c": [{"t": "Str", "c": "Precipitation"}],
                                        }
                                    ],
                                    [
                                        {
                                            "t": "Para",
                                            "c": [{"t": "Str", "c": "Temperature"}],
                                        },
                                        {
                                            "t": "OrderedList",
                                            "c": [
                                                [
                                                    1,
                                                    {"t": "DefaultStyle"},
                                                    {"t": "DefaultDelim"},
                                                ],
                                                [
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Str",
                                                                    "c": "degree",
                                                                }
                                                            ],
                                                        },
                                                        {
                                                            "t": "BulletList",
                                                            "c": [
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "hot",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "cold",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Strikeout",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "warm",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                            ],
                                                        },
                                                    ],
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Strikeout",
                                                                    "c": [
                                                                        {
                                                                            "t": "Str",
                                                                            "c": "sun",
                                                                        }
                                                                    ],
                                                                }
                                                            ],
                                                        }
                                                    ],
                                                ],
                                            ],
                                        },
                                    ],
                                ],
                            },
                        ],
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Strikeout", "c": [{"t": "Str", "c": "The"}]},
                                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                                    {
                                        "t": "Strikeout",
                                        "c": [{"t": "Str", "c": "geology"}],
                                    },
                                ],
                            }
                        ],
                    ],
                ],
            }
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["ordered_list"], indirect=True)
@pytest.mark.insert
def test_complex_insert_ordered_list(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "ordered_list", "ordered_list_inserted_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "OrderedList",
                "c": [
                    [1, {"t": "DefaultStyle"}, {"t": "DefaultDelim"}],
                    [
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "The"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "climate"},
                                    {"t": "Underline", "c": [{"t": "Space"}]},
                                    {
                                        "t": "Underline",
                                        "c": [{"t": "Str", "c": "intensive"}],
                                    },
                                ],
                            },
                            {
                                "t": "BulletList",
                                "c": [
                                    [
                                        {
                                            "t": "Para",
                                            "c": [
                                                {"t": "Str", "c": "Precipitation"},
                                                {
                                                    "t": "Underline",
                                                    "c": [{"t": "Space"}],
                                                },
                                                {
                                                    "t": "Underline",
                                                    "c": [
                                                        {"t": "Str", "c": "important"}
                                                    ],
                                                },
                                            ],
                                        }
                                    ],
                                    [
                                        {
                                            "t": "Para",
                                            "c": [
                                                {"t": "Str", "c": "Temperature"},
                                                {
                                                    "t": "Underline",
                                                    "c": [{"t": "Space"}],
                                                },
                                                {
                                                    "t": "Underline",
                                                    "c": [{"t": "Str", "c": "scales"}],
                                                },
                                            ],
                                        },
                                        {
                                            "t": "OrderedList",
                                            "c": [
                                                [
                                                    1,
                                                    {"t": "DefaultStyle"},
                                                    {"t": "DefaultDelim"},
                                                ],
                                                [
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Str",
                                                                    "c": "degree",
                                                                }
                                                            ],
                                                        },
                                                        {
                                                            "t": "BulletList",
                                                            "c": [
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "hot",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "cold",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "warm",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "really",
                                                                                    }
                                                                                ],
                                                                            },
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Space"
                                                                                    }
                                                                                ],
                                                                            },
                                                                            {
                                                                                "t": "Underline",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "hot",
                                                                                    }
                                                                                ],
                                                                            },
                                                                        ],
                                                                    }
                                                                ],
                                                            ],
                                                        },
                                                    ],
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {"t": "Str", "c": "sun"}
                                                            ],
                                                        }
                                                    ],
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Underline",
                                                                    "c": [
                                                                        {
                                                                            "t": "Str",
                                                                            "c": "cloud",
                                                                        }
                                                                    ],
                                                                }
                                                            ],
                                                        }
                                                    ],
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Underline",
                                                                    "c": [
                                                                        {
                                                                            "t": "Str",
                                                                            "c": "wind",
                                                                        }
                                                                    ],
                                                                }
                                                            ],
                                                        }
                                                    ],
                                                ],
                                            ],
                                        },
                                    ],
                                ],
                            },
                        ],
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "The"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "geology"},
                                ],
                            }
                        ],
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {
                                        "t": "Underline",
                                        "c": [{"t": "Str", "c": "something"}],
                                    },
                                    {"t": "Underline", "c": [{"t": "Space"}]},
                                    {"t": "Underline", "c": [{"t": "Str", "c": "new"}]},
                                ],
                            }
                        ],
                    ],
                ],
            }
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["ordered_list"], indirect=True)
@pytest.mark.mix
def test_complex_mix_ordered_list(setup_files_mix):
    old_version_file, new_version_file, diff_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "ordered_list", "ordered_list_mix_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "OrderedList",
                "c": [
                    [1, {"t": "DefaultStyle"}, {"t": "DefaultDelim"}],
                    [
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "The"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "climate"},
                                ],
                            },
                            {
                                "t": "BulletList",
                                "c": [
                                    [
                                        {
                                            "t": "Para",
                                            "c": [{"t": "Str", "c": "Precipitation"}],
                                        }
                                    ],
                                    [
                                        {
                                            "t": "Para",
                                            "c": [
                                                {"t": "Str", "c": "Temperature"},
                                                {
                                                    "t": "Underline",
                                                    "c": [{"t": "Space"}],
                                                },
                                                {
                                                    "t": "Underline",
                                                    "c": [{"t": "Str", "c": "factors"}],
                                                },
                                            ],
                                        },
                                        {
                                            "t": "OrderedList",
                                            "c": [
                                                [
                                                    1,
                                                    {"t": "DefaultStyle"},
                                                    {"t": "DefaultDelim"},
                                                ],
                                                [
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Str",
                                                                    "c": "degree",
                                                                }
                                                            ],
                                                        },
                                                        {
                                                            "t": "BulletList",
                                                            "c": [
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "hot",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Str",
                                                                                "c": "cold",
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                                [
                                                                    {
                                                                        "t": "Para",
                                                                        "c": [
                                                                            {
                                                                                "t": "Strikeout",
                                                                                "c": [
                                                                                    {
                                                                                        "t": "Str",
                                                                                        "c": "warm",
                                                                                    }
                                                                                ],
                                                                            }
                                                                        ],
                                                                    }
                                                                ],
                                                            ],
                                                        },
                                                    ],
                                                    [
                                                        {
                                                            "t": "Para",
                                                            "c": [
                                                                {
                                                                    "t": "Strikeout",
                                                                    "c": [
                                                                        {
                                                                            "t": "Str",
                                                                            "c": "sun",
                                                                        }
                                                                    ],
                                                                }
                                                            ],
                                                        }
                                                    ],
                                                ],
                                            ],
                                        },
                                    ],
                                ],
                            },
                        ],
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Strikeout", "c": [{"t": "Str", "c": "The"}]},
                                    {
                                        "t": "Underline",
                                        "c": [{"t": "Str", "c": "Something"}],
                                    },
                                    {"t": "Space"},
                                    {
                                        "t": "Strikeout",
                                        "c": [{"t": "Str", "c": "geology"}],
                                    },
                                    {"t": "Underline", "c": [{"t": "Str", "c": "new"}]},
                                ],
                            }
                        ],
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {
                                        "t": "Underline",
                                        "c": [{"t": "Str", "c": "Monkey"}],
                                    }
                                ],
                            }
                        ],
                    ],
                ],
            }
        ],
    }

    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_update", ["text_formats"], indirect=True)
@pytest.mark.update
def test_complex_update_text_formats(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "text_formats", "text_formats_updated_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading1"}]]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Paragraph"},
                    {"t": "Space"},
                    {"t": "Str", "c": "with"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u201cThis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "super"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "26.12.2022"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "26.02.2024"}]},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "Date"},
                    {"t": "Space"},
                    {"t": "Str", "c": "used"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "26.12.2022"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "30.12.2022"}]},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "Infrastructure"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Test"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "High"},
                    {"t": "LineBreak"},
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading3"}]]},
            {"t": "Para", "c": [{"t": "Emph", "c": [{"t": "Str", "c": "emphasis"}]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Some"},
                    {"t": "Space"},
                    {"t": "Str", "c": "normal"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "text"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "TEXT"}]},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "Italic"}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Str", "c": "MY"},
                            {"t": "Underline", "c": [{"t": "Space"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "NEW"}]},
                            {"t": "Space"},
                            {"t": "Str", "c": "TEXT"},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "HIGH"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ALREADY"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://typst.app/"}],
                                    ["https://typst.app/", ""],
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://something.app/"}],
                                    ["https://something.app/", ""],
                                ],
                            }
                        ],
                    },
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading4"}]]},
            {"t": "Para", "c": [{"t": "Str", "c": "abc"}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Link"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph:"},
                    {"t": "Space"},
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://typst.app/"}],
                                    ["https://typst.app/", ""],
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://something.app/"}],
                                    ["https://something.app/", ""],
                                ],
                            }
                        ],
                    },
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading5"}]]},
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_delete", ["text_formats"], indirect=True)
@pytest.mark.delete
def test_complex_delete_text_formats(setup_files_delete):

    old_version_file, new_version_file, diff_file = setup_files_delete
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "text_formats", "text_formats_deleted_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading1"}]]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Paragraph"},
                    {"t": "Space"},
                    {"t": "Str", "c": "with"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes"},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "\u201cThis"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "quotes.\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]}],
                    },
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "26.12.2022"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {"t": "Str", "c": "Date"},
                    {"t": "Space"},
                    {"t": "Str", "c": "used"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]}],
                    },
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Infrastructure"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Test"}]},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "High"},
                    {"t": "LineBreak"},
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading3"}]]},
            {"t": "Para", "c": [{"t": "Emph", "c": [{"t": "Str", "c": "emphasis"}]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Some"},
                    {"t": "Space"},
                    {"t": "Str", "c": "normal"},
                    {"t": "Space"},
                    {"t": "Str", "c": "text"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "Italic"}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Strong",
                                "c": [
                                    {"t": "Str", "c": "MY"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "TEXT"},
                                ],
                            }
                        ],
                    },
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Str", "c": "HIGH"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading4"}]]},
            {"t": "Para", "c": [{"t": "Str", "c": "abc"}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Link"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph:"},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://typst.app/"}],
                                    ["https://typst.app/", ""],
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Header",
                "c": [
                    1,
                    ["", [], []],
                    [{"t": "Strikeout", "c": [{"t": "Str", "c": "Heading5"}]}],
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["text_formats"], indirect=True)
@pytest.mark.insert
def test_complex_insert_text_formats(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "text_formats", "text_formats_inserted_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading1"}]]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Paragraph"},
                    {"t": "Space"},
                    {"t": "Str", "c": "with"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u201cThis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes.\u201d"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cNew"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "quote\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "Date"},
                    {"t": "Space"},
                    {"t": "Str", "c": "used"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]}],
                    },
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Infrastructure"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Test"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "Severity:"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "Date:"}]},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "High"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "30.12.2024"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Infrastructure"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Test"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "High"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading3"}]]},
            {"t": "Para", "c": [{"t": "Emph", "c": [{"t": "Str", "c": "emphasis"}]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Some"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "normal"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "text"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Another"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "normal"},
                    {"t": "Space"},
                    {"t": "Str", "c": "text"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "Italic"}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Str", "c": "MY"},
                            {"t": "Space"},
                            {"t": "Str", "c": "TEXT"},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Str", "c": "HIGH"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading4"}]]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "abc"},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "def"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Link"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "paragraph:"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://typst.app/"}],
                                    ["https://typst.app/", ""],
                                ],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Another"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "link"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph:"},
                    {"t": "Space"},
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    },
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading5"}]]},
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["text_formats"], indirect=True)
@pytest.mark.mix
def test_complex_mix_text_formats(setup_files_mix):
    old_version_file, new_version_file, diff_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "text_formats", "text_formats_mix_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading1"}]]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Paragraph"},
                    {"t": "Space"},
                    {"t": "Str", "c": "with"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u201cThis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes.\u201d"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cNew.\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "Date"},
                    {"t": "Space"},
                    {"t": "Str", "c": "used"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "26.12.2022"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]}],
                    },
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Infrastructure"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "30.12.2022"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Test"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "Severity:"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "Date:"}]},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "High"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "25.02.2022"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Infrastructure"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Test"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "High"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading3"}]]},
            {"t": "Para", "c": [{"t": "Emph", "c": [{"t": "Str", "c": "emphasis"}]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Some"},
                    {"t": "Space"},
                    {"t": "Str", "c": "normal"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "text"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "New"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "text"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "Italic"}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Str", "c": "MY"},
                            {"t": "Space"},
                            {"t": "Str", "c": "TEXT"},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Str", "c": "HIGH"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading4"}]]},
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "abc"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Str", "c": "abc"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Link"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "paragraph:"},
                    {"t": "Space"},
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Link",
                                "c": [
                                    ["", [], []],
                                    [{"t": "Str", "c": "https://another.link/"}],
                                    ["https://another.link/", ""],
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Header",
                "c": [
                    1,
                    ["", [], []],
                    [{"t": "Underline", "c": [{"t": "Str", "c": "Heading5"}]}],
                ],
            },
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading5"}]]},
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_update", ["all_types_working"], indirect=True)
@pytest.mark.update
def test_complex_update_all_types_working(setup_files_update):
    old_version_file, new_version_file, diff_file = setup_files_update
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(
        diff_json, "all_types_working", "all_types_working_updated_result"
    )

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "GNU"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nano"},
                    {"t": "Space"},
                    {"t": "Str", "c": "6.2"},
                    {"t": "Space"},
                    {"t": "Str", "c": "test1.typ"},
                ],
            },
            {
                "t": "Header",
                "c": [
                    1,
                    ["", [], []],
                    [
                        {"t": "Strikeout", "c": [{"t": "Str", "c": "Introduction"}]},
                        {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    ],
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "report,"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED,"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Space"},
                    {
                        "t": "Emph",
                        "c": [
                            {"t": "Str", "c": "fluid"},
                            {"t": "SoftBreak"},
                            {"t": "Str", "c": "dynamics"},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glaciers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "Space"},
                    {"t": "Str", "c": "how"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "contribute"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "formation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "behaviour"},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "these"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "natural"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "SOMETHING"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "structures."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "NEW."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation"},
                    {"t": "Space"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "Q = \\rho Av + C"]},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "defines"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacial"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "rate"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacier"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "defined"},
                    {"t": "Space"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "following"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation:"},
                ],
            },
            {
                "t": "Para",
                "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "Q = \\rho Av + C"]}],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "glacier"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "given"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "following"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation:"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "Q = \\rho Av + \\text{ time offset }",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "Q = \\rho Av + \\text{ time CHANGED }",
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Total"},
                    {"t": "Space"},
                    {"t": "Str", "c": "displaced"},
                    {"t": "Space"},
                    {"t": "Str", "c": "soil"},
                    {"t": "Space"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacial"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow:"},
                    {"t": "SoftBreak"},
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "7.32\\beta + \\sum_{i = 0}^{\\nabla}\\frac{Q_{i}\\left( a_{i} - \\varepsilon \\right)}{2}",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "7.32\\beta + \\sum_{i = 0}^{\\nabla}\\frac{Q_{i}\\left( a_{i} - \\varepsilon \\right)}{3}",
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "v \u2254 \\begin{pmatrix}\nx_{1} \\\\\nx_{2} \\\\\nx_{3}\n\\end{pmatrix}",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "v \u2254 \\begin{pmatrix}\nx_{1} \\\\\nx_{2} \\\\\nx_{2}\n\\end{pmatrix}",
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "DisplayMath"}, "a \\rightsquigarrow b"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Lorem"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ipsum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sit"},
                    {"t": "Space"},
                    {"t": "Str", "c": "amet,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "consectetur"},
                    {"t": "Space"},
                    {"t": "Str", "c": "adipiscing"},
                    {"t": "Space"},
                    {"t": "Str", "c": "elit,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sed"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "eiusmod"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "tempor"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "incididunt"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ut"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "labore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "et"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "dolore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "magna"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "aliqua."}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Ut"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Number:"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "3"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "6"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "- x"]},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "opposite"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "x"]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "let"},
                    {"t": "Space"},
                    {"t": "Str", "c": "name"},
                    {"t": "Space"},
                    {"t": "Str", "c": "="},
                    {"t": "Space"},
                    {"t": "Str", "c": "["},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Underline", "c": [{"t": "Str", "c": "Typst"}]},
                            {"t": "Underline", "c": [{"t": "Space"}]},
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "Typst!"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "NEW!"}]},
                        ],
                    },
                    {"t": "Str", "c": "]"},
                ],
            },
            {"t": "Para", "c": [{"t": "Strong", "c": [{"t": "Str", "c": "strong"}]}]},
            {"t": "Para", "c": [{"t": "Code", "c": [["", [], []], "print(1)"]}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Para", "c": [{"t": "Span", "c": [["intro", [], []], []]}]},
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading"}]]},
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u2018single\u201d"},
                    {"t": "Space"},
                    {"t": "Str", "c": "or"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u201cdouble\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u00a0,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}],
                    },
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{3}"]}],
                    },
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x_{1}"]}],
                    },
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x_{5}"]}],
                    },
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "1 + \\frac{a + b}{5}"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [
                            {"t": "InlineMath"},
                            "\\begin{array}{r}\nx \\\\\ny\n\\end{array}",
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\begin{aligned}\nx & = 2 \\\\\n & = 3\n\\end{aligned}",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\begin{aligned}\nx & = 5 \\\\\n & = 3\n\\end{aligned}",
                                ],
                            }
                        ],
                    },
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "\\pi"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "\\longrightarrow"]},
                    {"t": "LineBreak"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "xy"]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "\\rightarrow , \\neq"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "a\\text{ is natural}"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [{"t": "InlineMath"}, "\\left\\lfloor x \\right\\rfloor"],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Lorem"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ipsum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sit"},
                    {"t": "Space"},
                    {"t": "Str", "c": "amet,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "consectetur"},
                    {"t": "Space"},
                    {"t": "Str", "c": "adipiscing"},
                    {"t": "Space"},
                    {"t": "Str", "c": "elit,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sed"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Space"},
                    {"t": "Str", "c": "eiusmod"},
                    {"t": "Space"},
                    {"t": "Str", "c": "tempor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "incididunt"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ut"},
                    {"t": "Space"},
                    {"t": "Str", "c": "labore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "et"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "magna"},
                    {"t": "Space"},
                    {"t": "Str", "c": "aliqua."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Ut"},
                    {"t": "Space"},
                    {"t": "Str", "c": "enim"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ad"},
                    {"t": "Space"},
                    {"t": "Str", "c": "minim"},
                    {"t": "Space"},
                    {"t": "Str", "c": "veniam,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nostrud"},
                    {"t": "Space"},
                    {"t": "Str", "c": "exercitation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ullamco"},
                    {"t": "Space"},
                    {"t": "Str", "c": "laboris"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nisi"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Emph", "c": [{"t": "Str", "c": "Hello"}]},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "5"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "hello"},
                    {"t": "Space"},
                    {"t": "Str", "c": "from"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "world"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Typst\u2018s"},
                    {"t": "Space"},
                    {"t": "Str", "c": "documentation."},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "explains"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "Typst."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Sum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "5."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "coordinates"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "1,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "2."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "first"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "element"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "1."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "5."}]},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "last"},
                    {"t": "Space"},
                    {"t": "Str", "c": "element"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "4."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Austen"},
                    {"t": "Space"},
                    {"t": "Str", "c": "wrote"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Persuasion."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Homer"},
                    {"t": "Space"},
                    {"t": "Str", "c": "wrote"},
                    {"t": "Space"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Odyssey."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "y"},
                    {"t": "Space"},
                    {"t": "Str", "c": "coordinate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "2."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "(5,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "6,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "11)"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "shown"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "abc"}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Hello"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "Heading"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "3"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "same"},
                    {"t": "Space"},
                    {"t": "Str", "c": "as"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "3"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "4"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "3"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                    {"t": "Space"},
                    {"t": "Str", "c": "b"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                    {"t": "Space"},
                    {"t": "Str", "c": "c"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Dobrze"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "Infrastructure"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Test"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "High"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "abc"},
                    {"t": "LineBreak"},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "my"}]},
                            {"t": "Strikeout", "c": [{"t": "Space"}]},
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "text"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "already"},
                    {"t": "Space"},
                    {"t": "Str", "c": "low"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "ABC"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "LineBreak"},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Str", "c": "MY"},
                            {"t": "Space"},
                            {"t": "Str", "c": "TEXT"},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Str", "c": "HIGH"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cThis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cDas"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ist"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Anf\u00fchrungszeichen.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cC\u2019est"},
                    {"t": "Space"},
                    {"t": "Str", "c": "entre"},
                    {"t": "Space"},
                    {"t": "Str", "c": "guillemets.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "1"},
                    {"t": "Superscript", "c": [{"t": "Str", "c": "st"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "try!"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Italic"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "Oblique"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Underline", "c": [{"t": "Str", "c": "important"}]},
                    {"t": "Str", "c": "."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Take"},
                    {"t": "Space"},
                    {"t": "Underline", "c": [{"t": "Str", "c": "care"}]},
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_insert", ["all_types_working"], indirect=True)
@pytest.mark.insert
def test_complex_insert_all_types_working(setup_files_insert):
    old_version_file, new_version_file, diff_file = setup_files_insert
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(
        diff_json, "all_types_working", "all_types_working_inserted_result"
    )

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "GNU"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "nano"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "6.2"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "test1.typ"}]},
                ],
            },
            {
                "t": "Header",
                "c": [
                    1,
                    ["", [], []],
                    [{"t": "Underline", "c": [{"t": "Str", "c": "Introduction"}]}],
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "In"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "this"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "report,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "we"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "will"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "explore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "various"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "factors"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "that"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "influence"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Emph",
                                "c": [
                                    {"t": "Str", "c": "fluid"},
                                    {"t": "SoftBreak"},
                                    {"t": "Str", "c": "dynamics"},
                                ],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "glaciers"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "and"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "how"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "they"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "contribute"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "to"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "formation"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "and"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "behaviour"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "these"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "natural"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "structures."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "equation"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "InlineMath"}, "Q = \\rho Av + C"],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "defines"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "glacial"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "flow"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "rate."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "flow"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "rate"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "a"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "glacier"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "defined"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "by"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "following"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "equation:"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "DisplayMath"}, "Q = \\rho Av + C"],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "flow"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "rate"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "a"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "glacier"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "given"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "by"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "following"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "equation:"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "Q = \\rho Av + \\text{ time offset }",
                                ],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Total"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "displaced"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "soil"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "by"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "glacial"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "flow:"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "7.32\\beta + \\sum_{i = 0}^{\\nabla}\\frac{Q_{i}\\left( a_{i} - \\varepsilon \\right)}{2}",
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "v \u2254 \\begin{pmatrix}\nx_{1} \\\\\nx_{2} \\\\\nx_{3}\n\\end{pmatrix}",
                                ],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "DisplayMath"}, "a \\rightsquigarrow b"],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Lorem"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ipsum"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "dolor"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "sit"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "amet,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "consectetur"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "adipiscing"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "elit,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "sed"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "do"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Number:"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "3"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "- x"]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "opposite"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x"]}],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "let"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "name"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "="}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "["}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Typst!"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Str", "c": "]"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "strong"}]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Code", "c": [["", [], []], "print(1)"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [
                                {
                                    "t": "Underline",
                                    "c": [{"t": "Str", "c": "https://typst.app/"}],
                                }
                            ],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Para", "c": [{"t": "Span", "c": [["intro", [], []], []]}]},
            {
                "t": "Header",
                "c": [
                    1,
                    ["", [], []],
                    [{"t": "Underline", "c": [{"t": "Str", "c": "Heading"}]}],
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u2018single\u201d"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "or"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cdouble\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u00a0,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u2014"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "x^{2}"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x_{1}"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "InlineMath"}, "1 + \\frac{a + b}{5}"],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\begin{array}{r}\nx \\\\\ny\n\\end{array}",
                                ],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\begin{aligned}\nx & = 2 \\\\\n & = 3\n\\end{aligned}",
                                ],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "\\pi"]}],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "InlineMath"}, "\\longrightarrow"],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "xy"]}],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "InlineMath"}, "\\rightarrow , \\neq"],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "InlineMath"}, "a\\text{ is natural}"],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\left\\lfloor x \\right\\rfloor",
                                ],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Lorem"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ipsum"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "dolor"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "sit"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "amet,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "consectetur"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "adipiscing"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "elit,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "sed"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "do"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "eiusmod"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "tempor"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "incididunt"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ut"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "labore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "et"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "dolore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "magna"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "aliqua."}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Ut"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "enim"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ad"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "minim"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "veniam,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "quis"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "nostrud"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "exercitation"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ullamco"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "laboris"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "nisi"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Emph", "c": [{"t": "Str", "c": "Hello"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "5"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "hello"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "from"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "world"}]}],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "This"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Typst\u2018s"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "documentation."}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "It"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "explains"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Typst."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Sum"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "5."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "coordinates"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "are"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "1,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "2."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "first"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "element"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "1."}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "last"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "element"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "4."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Austen"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "wrote"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Persuasion."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Homer"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "wrote"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Odyssey."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "The"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "y"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "coordinate"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "2."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "(5,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "6,"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "11)"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "This"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "shown"}]},
                ],
            },
            {"t": "Para", "c": [{"t": "Underline", "c": [{"t": "Str", "c": "abc"}]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Hello"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Heading"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "3"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "the"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "same"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "as"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "3"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "4"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "3"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "a"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u2014"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "b"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u2014"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "c"}]},
                ],
            },
            {
                "t": "Para",
                "c": [{"t": "Underline", "c": [{"t": "Str", "c": "Dobrze"}]}],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "26.12.2022"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Infrastructure"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Test"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "High"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "abc"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Strong",
                                "c": [
                                    {"t": "Str", "c": "my"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "text"},
                                ],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "already"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "low"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "ABC"}]},
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Strong",
                                "c": [
                                    {"t": "Str", "c": "MY"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "TEXT"},
                                ],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ALREADY"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "HIGH"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cThis"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "quotes.\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cDas"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ist"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "in"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Str", "c": "Anf\u00fchrungszeichen.\u201d"}],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cC\u2019est"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "entre"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "guillemets.\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "1"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Superscript", "c": [{"t": "Str", "c": "st"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "try!"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Italic"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Oblique"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "This"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [
                            {"t": "Underline", "c": [{"t": "Str", "c": "important"}]}
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "Str", "c": "."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Take"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {
                        "t": "Underline",
                        "c": [{"t": "Underline", "c": [{"t": "Str", "c": "care"}]}],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "GNU"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nano"},
                    {"t": "Space"},
                    {"t": "Str", "c": "6.2"},
                    {"t": "Space"},
                    {"t": "Str", "c": "test1.typ"},
                ],
            },
            {
                "t": "Header",
                "c": [1, ["", [], []], [{"t": "Str", "c": "Introduction"}]],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Str", "c": "report,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Space"},
                    {
                        "t": "Emph",
                        "c": [
                            {"t": "Str", "c": "fluid"},
                            {"t": "SoftBreak"},
                            {"t": "Str", "c": "dynamics"},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glaciers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "Space"},
                    {"t": "Str", "c": "how"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "contribute"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "formation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "behaviour"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "these"},
                    {"t": "Space"},
                    {"t": "Str", "c": "natural"},
                    {"t": "Space"},
                    {"t": "Str", "c": "structures."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation"},
                    {"t": "Space"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "Q = \\rho Av + C"]},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "defines"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacial"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacier"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "defined"},
                    {"t": "Space"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "following"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation:"},
                ],
            },
            {
                "t": "Para",
                "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "Q = \\rho Av + C"]}],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacier"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "given"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "following"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation:"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [
                            {"t": "DisplayMath"},
                            "Q = \\rho Av + \\text{ time offset }",
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Total"},
                    {"t": "Space"},
                    {"t": "Str", "c": "displaced"},
                    {"t": "Space"},
                    {"t": "Str", "c": "soil"},
                    {"t": "Space"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacial"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow:"},
                    {"t": "SoftBreak"},
                    {
                        "t": "Math",
                        "c": [
                            {"t": "DisplayMath"},
                            "7.32\\beta + \\sum_{i = 0}^{\\nabla}\\frac{Q_{i}\\left( a_{i} - \\varepsilon \\right)}{2}",
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [
                            {"t": "DisplayMath"},
                            "v \u2254 \\begin{pmatrix}\nx_{1} \\\\\nx_{2} \\\\\nx_{3}\n\\end{pmatrix}",
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "DisplayMath"}, "a \\rightsquigarrow b"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Lorem"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ipsum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sit"},
                    {"t": "Space"},
                    {"t": "Str", "c": "amet,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "consectetur"},
                    {"t": "Space"},
                    {"t": "Str", "c": "adipiscing"},
                    {"t": "Space"},
                    {"t": "Str", "c": "elit,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sed"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Number:"},
                    {"t": "Space"},
                    {"t": "Str", "c": "3"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "- x"]},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "opposite"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "x"]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "let"},
                    {"t": "Space"},
                    {"t": "Str", "c": "name"},
                    {"t": "Space"},
                    {"t": "Str", "c": "="},
                    {"t": "Space"},
                    {"t": "Str", "c": "["},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Typst!"}]},
                    {"t": "Str", "c": "]"},
                ],
            },
            {"t": "Para", "c": [{"t": "Strong", "c": [{"t": "Str", "c": "strong"}]}]},
            {"t": "Para", "c": [{"t": "Code", "c": [["", [], []], "print(1)"]}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Para", "c": [{"t": "Span", "c": [["intro", [], []], []]}]},
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading"}]]},
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u2018single\u201d"},
                    {"t": "Space"},
                    {"t": "Str", "c": "or"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u201cdouble\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u00a0,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "x^{2}"]}]},
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x_{1}"]}]},
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "1 + \\frac{a + b}{5}"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [
                            {"t": "InlineMath"},
                            "\\begin{array}{r}\nx \\\\\ny\n\\end{array}",
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [
                            {"t": "InlineMath"},
                            "\\begin{aligned}\nx & = 2 \\\\\n & = 3\n\\end{aligned}",
                        ],
                    }
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "\\pi"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "\\longrightarrow"]},
                    {"t": "LineBreak"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "xy"]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "\\rightarrow , \\neq"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "a\\text{ is natural}"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [{"t": "InlineMath"}, "\\left\\lfloor x \\right\\rfloor"],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Lorem"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ipsum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sit"},
                    {"t": "Space"},
                    {"t": "Str", "c": "amet,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "consectetur"},
                    {"t": "Space"},
                    {"t": "Str", "c": "adipiscing"},
                    {"t": "Space"},
                    {"t": "Str", "c": "elit,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sed"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Space"},
                    {"t": "Str", "c": "eiusmod"},
                    {"t": "Space"},
                    {"t": "Str", "c": "tempor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "incididunt"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ut"},
                    {"t": "Space"},
                    {"t": "Str", "c": "labore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "et"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "magna"},
                    {"t": "Space"},
                    {"t": "Str", "c": "aliqua."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Ut"},
                    {"t": "Space"},
                    {"t": "Str", "c": "enim"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ad"},
                    {"t": "Space"},
                    {"t": "Str", "c": "minim"},
                    {"t": "Space"},
                    {"t": "Str", "c": "veniam,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nostrud"},
                    {"t": "Space"},
                    {"t": "Str", "c": "exercitation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ullamco"},
                    {"t": "Space"},
                    {"t": "Str", "c": "laboris"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nisi"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Emph", "c": [{"t": "Str", "c": "Hello"}]},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "5"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "hello"},
                    {"t": "Space"},
                    {"t": "Str", "c": "from"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "world"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Typst\u2018s"},
                    {"t": "Space"},
                    {"t": "Str", "c": "documentation."},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explains"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Typst."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Sum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "5."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "coordinates"},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "1,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "2."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "first"},
                    {"t": "Space"},
                    {"t": "Str", "c": "element"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "1."},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "last"},
                    {"t": "Space"},
                    {"t": "Str", "c": "element"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "4."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Austen"},
                    {"t": "Space"},
                    {"t": "Str", "c": "wrote"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Persuasion."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Homer"},
                    {"t": "Space"},
                    {"t": "Str", "c": "wrote"},
                    {"t": "Space"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Odyssey."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "y"},
                    {"t": "Space"},
                    {"t": "Str", "c": "coordinate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "2."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "(5,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "6,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "11)"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "shown"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "abc"}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Hello"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "Heading"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "3"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "same"},
                    {"t": "Space"},
                    {"t": "Str", "c": "as"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "3"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "4"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "3"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                    {"t": "Space"},
                    {"t": "Str", "c": "b"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                    {"t": "Space"},
                    {"t": "Str", "c": "c"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "Dobrze"}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "Infrastructure"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Test"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "High"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "abc"},
                    {"t": "LineBreak"},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Str", "c": "my"},
                            {"t": "Space"},
                            {"t": "Str", "c": "text"},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "already"},
                    {"t": "Space"},
                    {"t": "Str", "c": "low"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "ABC"},
                    {"t": "LineBreak"},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Str", "c": "MY"},
                            {"t": "Space"},
                            {"t": "Str", "c": "TEXT"},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Str", "c": "HIGH"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cThis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cDas"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ist"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Anf\u00fchrungszeichen.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cC\u2019est"},
                    {"t": "Space"},
                    {"t": "Str", "c": "entre"},
                    {"t": "Space"},
                    {"t": "Str", "c": "guillemets.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "1"},
                    {"t": "Superscript", "c": [{"t": "Str", "c": "st"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "try!"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Italic"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "Oblique"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Underline", "c": [{"t": "Str", "c": "important"}]},
                    {"t": "Str", "c": "."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Take"},
                    {"t": "Space"},
                    {"t": "Underline", "c": [{"t": "Str", "c": "care"}]},
                ],
            },
        ],
    }
    assert diff_json == expected_json


@pytest.mark.parametrize("setup_files_mix", ["all_types_working"], indirect=True)
@pytest.mark.mix
def test_complex_mix_all_types_working(setup_files_mix):
    old_version_file, new_version_file, diff_file = setup_files_mix
    diff_json = perform_jsondiff_on_typst_files(
        old_version_file, new_version_file, diff_file
    )
    create_result_files(diff_json, "all_types_working", "all_types_working_mix_result")

    expected_json = {
        "pandoc-api-version": [1, 23, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "GNU"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nano"},
                    {"t": "Space"},
                    {"t": "Str", "c": "6.2"},
                    {"t": "Space"},
                    {"t": "Str", "c": "test1.typ"},
                ],
            },
            {
                "t": "Header",
                "c": [
                    1,
                    ["", [], []],
                    [
                        {"t": "Strikeout", "c": [{"t": "Str", "c": "Introduction"}]},
                        {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    ],
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "In"},
                    {"t": "Space"},
                    {"t": "Str", "c": "this"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "report,"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED,"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "we"},
                    {"t": "Space"},
                    {"t": "Str", "c": "will"},
                    {"t": "Space"},
                    {"t": "Str", "c": "explore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "various"},
                    {"t": "Space"},
                    {"t": "Str", "c": "factors"},
                    {"t": "Space"},
                    {"t": "Str", "c": "that"},
                    {"t": "Space"},
                    {"t": "Str", "c": "influence"},
                    {"t": "Space"},
                    {
                        "t": "Emph",
                        "c": [
                            {"t": "Str", "c": "fluid"},
                            {"t": "SoftBreak"},
                            {"t": "Str", "c": "dynamics"},
                        ],
                    },
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glaciers"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "Space"},
                    {"t": "Str", "c": "how"},
                    {"t": "Space"},
                    {"t": "Str", "c": "they"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "contribute"},
                    {"t": "Space"},
                    {"t": "Str", "c": "to"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "formation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "and"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "behaviour"},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "of"}]},
                    {"t": "Strikeout", "c": [{"t": "Space"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "these"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "natural"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "SOMETHING"}]},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "structures."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "NEW."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Another"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "one."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation"},
                    {"t": "Space"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "Q = \\rho Av + C"]},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "defines"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacial"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "rate"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacier"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "defined"},
                    {"t": "Space"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "following"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation:"},
                ],
            },
            {
                "t": "Para",
                "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "Q = \\rho Av + C"]}],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow"},
                    {"t": "Space"},
                    {"t": "Str", "c": "rate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "glacier"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "given"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "following"},
                    {"t": "Space"},
                    {"t": "Str", "c": "equation:"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "Q = \\rho Av + \\text{ time offset }",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "Q = \\rho Av + \\text{ time CHANGED }",
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Total"},
                    {"t": "Space"},
                    {"t": "Str", "c": "displaced"},
                    {"t": "Space"},
                    {"t": "Str", "c": "soil"},
                    {"t": "Space"},
                    {"t": "Str", "c": "by"},
                    {"t": "Space"},
                    {"t": "Str", "c": "glacial"},
                    {"t": "Space"},
                    {"t": "Str", "c": "flow:"},
                    {"t": "SoftBreak"},
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "7.32\\beta + \\sum_{i = 0}^{\\nabla}\\frac{Q_{i}\\left( a_{i} - \\varepsilon \\right)}{2}",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "7.32\\beta + \\sum_{i = 0}^{\\nabla}\\frac{Q_{i}\\left( a_{i} - \\varepsilon \\right)}{3}",
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "v \u2254 \\begin{pmatrix}\nx_{1} \\\\\nx_{2} \\\\\nx_{2}\n\\end{pmatrix}",
                                ],
                            }
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "DisplayMath"},
                                    "v \u2254 \\begin{pmatrix}\nx_{1} \\\\\nx_{2} \\\\\nx_{3}\n\\end{pmatrix}",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [{"t": "DisplayMath"}, "a \\rightsquigarrow b"],
                            }
                        ],
                    },
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "DisplayMath"}, "a \\rightsquigarrow b"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Lorem"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ipsum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sit"},
                    {"t": "Space"},
                    {"t": "Str", "c": "amet,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "consectetur"},
                    {"t": "Space"},
                    {"t": "Str", "c": "adipiscing"},
                    {"t": "Space"},
                    {"t": "Str", "c": "elit,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sed"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "eiusmod"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "tempor"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "incididunt"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "ut"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "labore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "et"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "dolore"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "magna"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "aliqua."}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Ut"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Number:"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "3"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "6"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "- x"]},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "opposite"},
                    {"t": "Space"},
                    {"t": "Str", "c": "of"},
                    {"t": "Space"},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "x"]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "let"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "name"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "="}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "["}]},
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Strong",
                                "c": [
                                    {"t": "Str", "c": "Typst"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "NEW!"},
                                ],
                            }
                        ],
                    },
                    {"t": "Underline", "c": [{"t": "Str", "c": "]"}]},
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Str", "c": "let"},
                    {"t": "Space"},
                    {"t": "Str", "c": "name"},
                    {"t": "Space"},
                    {"t": "Str", "c": "="},
                    {"t": "Space"},
                    {"t": "Str", "c": "["},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Underline", "c": [{"t": "Str", "c": "Typst"}]},
                            {"t": "Underline", "c": [{"t": "Space"}]},
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "Typst!"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "NEW!"}]},
                        ],
                    },
                    {"t": "Str", "c": "]"},
                ],
            },
            {"t": "Para", "c": [{"t": "Strong", "c": [{"t": "Str", "c": "strong"}]}]},
            {"t": "Para", "c": [{"t": "Code", "c": [["", [], []], "print(1)"]}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Link",
                        "c": [
                            ["", [], []],
                            [{"t": "Str", "c": "https://typst.app/"}],
                            ["https://typst.app/", ""],
                        ],
                    }
                ],
            },
            {"t": "Para", "c": [{"t": "Span", "c": [["intro", [], []], []]}]},
            {"t": "Header", "c": [1, ["", [], []], [{"t": "Str", "c": "Heading"}]]},
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u2018single\u201d"},
                    {"t": "Space"},
                    {"t": "Str", "c": "or"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u201cdouble\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u00a0,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{3}"]}],
                    },
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}],
                    },
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{3}"]}],
                    },
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "DisplayMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x_{1}"]}],
                    },
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x_{5}"]}],
                    },
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "x^{2}"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "1 + \\frac{a + b}{5}"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [
                            {"t": "InlineMath"},
                            "\\begin{array}{r}\nx \\\\\ny\n\\end{array}",
                        ],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\begin{aligned}\nx & = 2 \\\\\n & = 3\n\\end{aligned}",
                                ],
                            }
                        ],
                    },
                    {
                        "t": "Underline",
                        "c": [
                            {
                                "t": "Math",
                                "c": [
                                    {"t": "InlineMath"},
                                    "\\begin{aligned}\nx & = 5 \\\\\n & = 3\n\\end{aligned}",
                                ],
                            }
                        ],
                    },
                ],
            },
            {"t": "Para", "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "\\pi"]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "\\longrightarrow"]},
                    {"t": "LineBreak"},
                    {
                        "t": "Underline",
                        "c": [{"t": "Math", "c": [{"t": "InlineMath"}, "xy"]}],
                    },
                    {"t": "Underline", "c": [{"t": "SoftBreak"}]},
                    {"t": "Math", "c": [{"t": "InlineMath"}, "xy"]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "\\rightarrow , \\neq"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Math", "c": [{"t": "InlineMath"}, "a\\text{ is natural}"]}
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Math",
                        "c": [{"t": "InlineMath"}, "\\left\\lfloor x \\right\\rfloor"],
                    }
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Lorem"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ipsum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sit"},
                    {"t": "Space"},
                    {"t": "Str", "c": "amet,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "consectetur"},
                    {"t": "Space"},
                    {"t": "Str", "c": "adipiscing"},
                    {"t": "Space"},
                    {"t": "Str", "c": "elit,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "sed"},
                    {"t": "Space"},
                    {"t": "Str", "c": "do"},
                    {"t": "Space"},
                    {"t": "Str", "c": "eiusmod"},
                    {"t": "Space"},
                    {"t": "Str", "c": "tempor"},
                    {"t": "Space"},
                    {"t": "Str", "c": "incididunt"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ut"},
                    {"t": "Space"},
                    {"t": "Str", "c": "labore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "et"},
                    {"t": "Space"},
                    {"t": "Str", "c": "dolore"},
                    {"t": "Space"},
                    {"t": "Str", "c": "magna"},
                    {"t": "Space"},
                    {"t": "Str", "c": "aliqua."},
                    {"t": "Space"},
                    {"t": "Str", "c": "Ut"},
                    {"t": "Space"},
                    {"t": "Str", "c": "enim"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ad"},
                    {"t": "Space"},
                    {"t": "Str", "c": "minim"},
                    {"t": "Space"},
                    {"t": "Str", "c": "veniam,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nostrud"},
                    {"t": "Space"},
                    {"t": "Str", "c": "exercitation"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ullamco"},
                    {"t": "Space"},
                    {"t": "Str", "c": "laboris"},
                    {"t": "Space"},
                    {"t": "Str", "c": "nisi"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Emph", "c": [{"t": "Str", "c": "Hello"}]},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "5"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {
                        "t": "Underline",
                        "c": [{"t": "Emph", "c": [{"t": "Str", "c": "Hello"}]}],
                    },
                    {"t": "Underline", "c": [{"t": "LineBreak"}]},
                    {"t": "Str", "c": "hello"},
                    {"t": "Space"},
                    {"t": "Str", "c": "from"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "world"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Typst\u2018s"},
                    {"t": "Space"},
                    {"t": "Str", "c": "documentation."},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "It"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "explains"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "Typst."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Sum"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "is"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "5."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Sum"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "5."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "coordinates"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "are"},
                    {"t": "Space"},
                    {"t": "Str", "c": "1,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "2."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "first"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "element"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "1."}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "5."}]},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "last"},
                    {"t": "Space"},
                    {"t": "Str", "c": "element"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "4."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "Austen"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "wrote"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "Persuasion."}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Austen"},
                    {"t": "Space"},
                    {"t": "Str", "c": "wrote"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Persuasion."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Homer"},
                    {"t": "Space"},
                    {"t": "Str", "c": "wrote"},
                    {"t": "Space"},
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Odyssey."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "The"},
                    {"t": "Space"},
                    {"t": "Str", "c": "y"},
                    {"t": "Space"},
                    {"t": "Str", "c": "coordinate"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "2."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "(5,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "6,"},
                    {"t": "Space"},
                    {"t": "Str", "c": "11)"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "shown"},
                ],
            },
            {"t": "Para", "c": [{"t": "Str", "c": "abc"}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Hello"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "Heading"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "3"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "the"},
                    {"t": "Space"},
                    {"t": "Str", "c": "same"},
                    {"t": "Space"},
                    {"t": "Str", "c": "as"},
                    {"t": "SoftBreak"},
                    {"t": "Str", "c": "3"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "4"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "3"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "a"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                    {"t": "Space"},
                    {"t": "Str", "c": "b"},
                    {"t": "Space"},
                    {"t": "Str", "c": "\u2014"},
                    {"t": "Space"},
                    {"t": "Str", "c": "c"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Dobrze"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strong", "c": [{"t": "Str", "c": "Date:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "26.12.2022"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Topic:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "Infrastructure"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Test"},
                    {"t": "LineBreak"},
                    {"t": "Strong", "c": [{"t": "Str", "c": "Severity:"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "High"},
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "abc"},
                    {"t": "LineBreak"},
                    {
                        "t": "Strong",
                        "c": [
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "my"}]},
                            {"t": "Strikeout", "c": [{"t": "Space"}]},
                            {"t": "Strikeout", "c": [{"t": "Str", "c": "text"}]},
                            {"t": "Underline", "c": [{"t": "Str", "c": "changed"}]},
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "already"},
                    {"t": "Space"},
                    {"t": "Str", "c": "low"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "ABC"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Strikeout", "c": [{"t": "LineBreak"}]},
                    {
                        "t": "Strikeout",
                        "c": [
                            {
                                "t": "Strong",
                                "c": [
                                    {"t": "Str", "c": "MY"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "TEXT"},
                                ],
                            }
                        ],
                    },
                    {"t": "LineBreak"},
                    {"t": "Str", "c": "ALREADY"},
                    {"t": "Space"},
                    {"t": "Str", "c": "HIGH"},
                ],
            },
            {"t": "Para", "c": [{"t": "Underline", "c": [{"t": "Str", "c": "NEW"}]}]},
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cThis"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "quotes.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cDas"},
                    {"t": "Space"},
                    {"t": "Str", "c": "ist"},
                    {"t": "Space"},
                    {"t": "Str", "c": "in"},
                    {"t": "Space"},
                    {"t": "Str", "c": "Anf\u00fchrungszeichen.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Underline", "c": [{"t": "Str", "c": "\u201cC\u2019est"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Underline", "c": [{"t": "Space"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "guillemets.\u201d"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "\u201cC\u2019est"},
                    {"t": "Space"},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "entre"}]},
                    {"t": "Underline", "c": [{"t": "Str", "c": "CHANGED"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "guillemets.\u201d"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "1"},
                    {"t": "Superscript", "c": [{"t": "Str", "c": "st"}]},
                    {"t": "Space"},
                    {"t": "Str", "c": "try!"},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Italic"},
                    {"t": "Strikeout", "c": [{"t": "SoftBreak"}]},
                    {"t": "Strikeout", "c": [{"t": "Str", "c": "Oblique"}]},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "This"},
                    {"t": "Space"},
                    {"t": "Str", "c": "is"},
                    {"t": "Space"},
                    {"t": "Underline", "c": [{"t": "Str", "c": "important"}]},
                    {"t": "Str", "c": "."},
                ],
            },
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Take"},
                    {"t": "Space"},
                    {"t": "Underline", "c": [{"t": "Str", "c": "care"}]},
                ],
            },
        ],
    }
    assert diff_json == expected_json
