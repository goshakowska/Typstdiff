class CouldNotParseFiles(Exception):
    def __init__(self, e):
        super().__init__(f"Used type unsupported by pandoc: [{e}]")


class InvalidJsonDiffOutput(Exception):
    def __init__(self, e):
        super().__init__(f"Could not parse jsondiff output: [{e}]")


class CouldNotOpenFile(Exception):
    def __init__(self, e):
        super().__init__(f"Could not file: [{e}]")


class UnsupportedParaType(Exception):
    def __init__(self, para):
        super().__init__(f"Unsupported type for para: {type(para)}")
