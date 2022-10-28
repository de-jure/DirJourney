"""_summary_

Returns:
    _type_: _description_
"""
from config import FORMATS


def get_file_editor(file_path: str) -> str:
    """_summary_

    Args:
        file_path (str): path to file

    Returns:
        str: editor for file (according to FORMATS in config.py)
    """
    return FORMATS.get(file_path.split('.')[-1]) or FORMATS["else"]
