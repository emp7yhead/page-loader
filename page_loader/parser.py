"""Functions to parse data in html."""
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup
from page_loader import url
from progress.bar import IncrementalBar

attribute_mapping = {
    'link': 'href',
    'script': 'src',
    'img': 'src',
}


def prepare_assets(
    html: str,
    target_url: str,
    assets_dir_name: str
) -> tuple[str, list[Any]]:
    page = BeautifulSoup(html, 'html.parser')

    tags = [*page('script'), *page('link'), *page('img')]

    assets = []
    for tag in tags:
        attr_name = attribute_mapping[tag.name]
        asset_url = tag.get(attr_name)

        if not asset_url:
            continue

        full_asset_url = urljoin(target_url + '/', asset_url)

        if urlparse(full_asset_url).netloc != urlparse(target_url).netloc:
            continue

        file_name = url.to_file_name(full_asset_url)
        assets.append((full_asset_url, file_name))
        tag[attr_name] = Path(assets_dir_name, file_name)

    return (page.prettify(), assets)


async def download_assets(assets_path: Path, assets: list[Any]) -> None:
    bar_width = len(assets)
    with IncrementalBar('Downloading:', max=bar_width) as bar:
        bar.suffix = '%(percent).1f%% (eta: %(eta)s)'

        client = httpx.AsyncClient()
        for assett_url, file_name in assets:
            response = await client.get(assett_url)
            with Path(assets_path, file_name).open('wb') as asset_file:
                asset_file.write(response.content)

                bar.next()
