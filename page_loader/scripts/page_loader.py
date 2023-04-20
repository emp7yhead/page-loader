import asyncio
import logging
import sys
from time import time
from page_loader.runner import run_script


def main() -> None:
    t0 = time()
    logging.basicConfig(level=logging.INFO)

    try:
        path = asyncio.run(run_script())
        logging.info(f'successfully downloaded in {path}')
    except Exception as e:
        logging.error(e)
        sys.exit(1)
    print(time() - t0)


if __name__ == '__main__':
    main()
