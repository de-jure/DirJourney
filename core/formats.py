from config import FORMATS


def get_file_editor(file_path: str) -> str:
    return FORMATS.get(file_path.split('.')[-1]) or FORMATS["else"]
