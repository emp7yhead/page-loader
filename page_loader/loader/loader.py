"""Function for downloading web-page."""
import os
from typing import Dict, Union

import requests
from page_loader.loader.parser import update_page_and_files
from page_loader.loader.url import get_name

SUCCESS_MSG = 'Page was successfully downloaded into {0}'
FOLDER_NAME = '_files'
DEFAULT_DIR = os.getcwd()


def download(url: str, dir_path: str) -> str:  # noqa: WPS210
    """Save web-page as file.

    Args:
        url: url to download.
        dir_path: path to save file.

    Returns:
        str.
    """
    page = get_content(url)
    local_page_name = get_name(url)
    local_page_path = os.path.join(dir_path, local_page_name)
    local_files_path = get_name(url, extension=FOLDER_NAME)
    updated_page, upd_files_paths = update_page_and_files(
        page,
        url,
        local_files_path,
    )
    local_page_path = save(local_page_path, updated_page)

    if upd_files_paths:
        download_updated_files(local_files_path, upd_files_paths)

    return local_page_path


def save(local_path: str, resource: Union[bytes, str], mode='w') -> str:
    """Save file in local directory.

    Args:
        local_path: path to save file.
        resource: content to save.
        mode: the mode in which the file is opened.

    Returns:
        str
    """
    with open(local_path, mode=mode) as out:
        out.write(resource)
    print(SUCCESS_MSG.format(local_path))  # noqa: WPS421
    return local_path


def download_resources(files_path: Dict, dir_path: str) -> None:
    """Download content in local path.

    Args:
        files_path: path to download files
        dir_path: path to save content
    """
    for url, local_name in files_path.items():
        resource = get_content(url)
        local_path = os.path.join(dir_path, local_name)
        save(local_path, resource, 'wb')


def download_updated_files(
    local_files_path: str,
    upd_files_paths: Dict,
) -> None:
    """Download updated files to local directory.

    Args:
        local_files_path: local path to files.
        upd_files_paths: updated path to files.
    """
    dir_path = os.path.join(DEFAULT_DIR, local_files_path)
    os.makedirs(dir_path, exist_ok=True)
    download_resources(upd_files_paths, dir_path)


def get_content(url: str) -> bytes:
    """Get content of response.

    Args:
        url: url with content

    Returns:
        bytes
    """
    response = requests.get(url)
    return response.content
