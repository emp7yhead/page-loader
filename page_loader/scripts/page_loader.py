import asyncio
import logging
import sys

from page_loader.runner import run_script


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    try:
        path = asyncio.run(run_script())
        logging.info(f'successfully downloaded in {path}')
    except Exception as e:
        logging.error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
