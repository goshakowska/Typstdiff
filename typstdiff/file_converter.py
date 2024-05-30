import subprocess
import json


class FileConverter:

    def write_to_json_file(
        self, json_data, output_file="comparison_new.json", indent=4
    ):
        with open(output_file, "w") as updated_file:
            json_to_string = json.dump(json_data, updated_file, indent=indent)
        return json_to_string

    def convert_with_pandoc(self, from_format, to_format, input_file, output_file):
        with open(output_file, "w") as output_new_file:
            subprocess.run(
                ["pandoc", "-f", from_format, "-t", to_format, input_file],
                stdout=output_new_file,
            )
        output_new_file.close()

    def write_lines(self, lines: list, file_path):
        with open(file_path, "r+") as file:
            content = file.read()
            file.seek(0, 0)
            for line in lines:
                file.write(line + "\n")
            file.write(content)
        file.close()

    def compile_to_pdf(self, input_file):
        subprocess.run(["typst", "compile", input_file])
