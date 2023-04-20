"""Function for downloading web-page."""
import logging
from pathlib import Path

import httpx
from page_loader.parser import download_assets, prepare_assets
from page_loader.url import to_dir_name, to_file_name

logger = logging.getLogger(__name__)


async def download(target_url: str, output_path: str) -> str:
    """Save web-page as file.

    Args:
        url: url to download.
        dir_path: path to save file.

    Returns:
        str.
    """
    cwd = Path().cwd()
    full_output_path = cwd.joinpath(output_path)
    html_file_name = to_file_name(target_url)
    html_file_path = cwd.joinpath(full_output_path, html_file_name)
    assets_dir_name = to_dir_name(target_url)
    assets_path = cwd.joinpath(full_output_path, assets_dir_name)

    logging.info(f'output path: {full_output_path}')

    async with httpx.AsyncClient() as client:
        response = await client.get(target_url)

    response.raise_for_status()

    html, assets = prepare_assets(
        response.text,
        target_url,
        assets_dir_name
    )

    write_page(html.encode(), html_file_path)

    if assets:
        if not Path(assets_path).exists():
            logging.info(f'create directory for assets: {assets_path}')
            Path(assets_path).mkdir()

        await download_assets(assets_path, assets)

    return html_file_path.as_posix()


def write_page(data: bytes, path: Path) -> None:
    with path.open('wb') as file:
        logging.info(f'write html file: {path}')
        file.write(data)
