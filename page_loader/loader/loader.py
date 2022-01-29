"""Function for downloading web-page."""
import requests
from page_loader.loader.url import get_file_path

CHUNK_SIZE = 128
SUCCESS_MSG = 'Page was successfully downloaded into {0}'


def download(url: str, dir_path: str) -> str:
    """Save web-page as file.

    Args:
        url: url to download.
        dir_path: path to save file.

    Returns:
        str.

    Raises:
        IsADirectoryError: if path is directory.
    """
    response = requests.get(url, stream=True)
    path = get_file_path(dir_path, url)
    try:
        with open(path, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                fd.write(chunk)
            print(SUCCESS_MSG.format(path))  # noqa: WPS421
    except FileNotFoundError as error:
        raise IsADirectoryError from error
    return path
