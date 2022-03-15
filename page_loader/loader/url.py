"""Functions to work with url."""

import os
import re
from typing import Tuple
from urllib.parse import urlparse

FILE_NAME_TEMPLATE = '{0}{1}'


def get_name(url: str, extension: str = '.html') -> str:
    """Get file name for downloading.

    Args:
        url: url to parse.
        extension: extension of object.

    Returns:
            str
    """
    url_without_scheme, ext = get_url_without_scheme_and_ext(url)
    if ext:
        extension = ext
    file_name = re.sub(r'[^\w]', '-', url_without_scheme.rstrip('/'))
    return FILE_NAME_TEMPLATE.format(file_name, extension)


def get_url_without_scheme_and_ext(url: str) -> Tuple:
    """Get url without scheme and extension.

    Args:
        url: url for file or page.

    Returns:
        tuple
    """
    parsed_url = urlparse(url)
    root, ext = os.path.splitext(parsed_url.path)
    url_without_scheme = os.path.join(parsed_url.netloc + root)
    return url_without_scheme, ext
