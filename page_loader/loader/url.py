"""Functions to work with url."""

import os
import re
from urllib.parse import urlparse
from xmlrpc.client import Boolean

FILE_NAME_TEMPLATE = '{0}.html'


def get_file_path(dir_path: str, url: str) -> str:
    """Get path to save file.

    Args:
        dir_path: path to local existing directory.
        url: url to download.

    Returns:
        str
    """
    file_name = get_file_name(url)
    return os.path.join(dir_path, file_name)


def get_file_name(url: str) -> str:
    """Get file name for downloading.

    Args:
        url: url to parse.

    Returns:
            str
    """
    parsed_url = urlparse(url)
    if parsed_url.hostname:
        url_without_scheme = parsed_url.hostname + parsed_url.path
    else:
        url_without_scheme = parsed_url.path
    file_name_wihtout_symbols = re.split(r'\.|/|_', url_without_scheme)
    return FILE_NAME_TEMPLATE.format('-'.join(file_name_wihtout_symbols))


def check_dir(path: str) -> Boolean:
    """Check directory existence.

    # noqa: DAR401 Exeption

    Args:
        path: path to directory.

    Returns:
        boolean

    Raises:
        Exeption: if directory does not exist. # noqa: DAR402
    """
    if os.path.isdir(path):
        return True
    raise Exception('Chosen directory does not exist.')  # noqa: WPS454
