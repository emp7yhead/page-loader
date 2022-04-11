"""Functions to parse data in html."""
import os
from typing import Any, Dict, Tuple
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from page_loader.loader.url import get_file_name

TAGS = (
    'img',
    'link',
    'script',
)

ATTRIBUTES = {  # noqa: WPS407
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def prepare_resourses(  # noqa: WPS210
    page: Any,
    url: str,
    files_dir: str,
) -> Tuple[str, Dict]:
    """Update HTML page and files.

    Args:
        page: content of page to update
        url: url to update
        files_dir: directory for files

    Returns:
        updated_page: str
        upd_files_paths: dict
    """
    upd_files_paths = {}
    soup = BeautifulSoup(page, 'html.parser')
    tags = soup.find_all(TAGS)

    for tag in tags:
        name = ATTRIBUTES[tag.name]
        url_to_media = tag.get(name)
        full_url = urljoin(url, url_to_media)

        if is_local(full_url, url):
            local_file_name = get_file_name(full_url)
            upd_files_paths[full_url] = local_file_name
            tag[name] = os.path.join(files_dir, local_file_name)

    updated_page = soup.prettify()
    return updated_page, upd_files_paths


def is_local(full_url: str, url: str) -> bool:
    """Check location of file.

    Args:
        full_url: full url to file.
        url: url to file.

    Returns:
        bool
    """
    return urlparse(full_url).netloc == urlparse(url).netloc
