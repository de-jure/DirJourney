"""_summary_

Returns:
    _type_: _description_
"""
import os


def get_dir_list(path: str) -> list:
    """get_dir_list

    Args:
        path (str): path to directory

    Returns:
        list: list of files in directory
    """
    listdir = os.listdir(path)
    if len(listdir) > 30:
        listdir = listdir[:30]
    result = []

    for entity in listdir:
        if os.path.isdir(path + entity):
            entity += '/'
        result.append(entity)

    return result
