formats = {
    # "format": "editor",
    "py": "cat",
    "else": "cat", # default editor for another formats
}

def get_file_editor(file_path: str) -> str:
    return formats.get(file_path.split('.')[-1]) or formats["else"]
