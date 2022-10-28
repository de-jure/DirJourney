from config import FILENAME_MAX_LEN

def filename_formatter(file_name: str, max_size: int = FILENAME_MAX_LEN) -> str:
    file_name = file_name.ljust(max_size)
    if len(file_name) > max_size:
        return file_name[:max_size-3] + '...'
    else:
        return file_name
