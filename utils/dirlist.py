import os


def get_dir_list(dir: str) -> list:
    listdir = os.listdir(dir)
    if len(listdir) > 30:
        listdir = listdir[:30]
    result = []

    for entity in listdir:
        if os.path.isdir(dir + entity):
            entity += '/'
        result.append(entity)

    return result
