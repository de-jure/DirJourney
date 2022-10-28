"""_summary_

Returns:
    _type_: _description_
"""
from config import FILENAME_MAX_LEN

def filename_formatter(file_name: str, max_size: int = FILENAME_MAX_LEN) -> str:
    """_summary_

    Args:
        file_name (str)
        max_size (int, optional): filename max lenght. Defaults to FILENAME_MAX_LEN.

    Returns:
        str: filename
    """
    file_name = file_name.ljust(max_size)
    if len(file_name) > max_size:
        return file_name[:max_size-3] + '...'
    return file_name
