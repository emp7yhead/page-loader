import asyncio

from page_loader.cli import parse_arguments
from page_loader.loader import download


async def run_script() -> str:
    # url, path = parse_arguments()
    url = 'https://doka.guide/'
    path = '/Users/empty_head/projects/async-page-loader/temp'
    task = asyncio.create_task(download(url, path))
    result_path = await asyncio.gather(task)
    return result_path[0]
