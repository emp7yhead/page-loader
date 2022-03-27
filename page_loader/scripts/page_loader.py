"""Page-loader main script."""

import logging
import sys

from page_loader.cli.cli import parse_arguments
from page_loader.loader.loader import download
from page_loader.logger.logger_setup import setup_logging
from page_loader.logger.exceptions import NetworkError, FileSystemError

logger = logging.getLogger(__name__)
setup_logging()


def main() -> None:
    """Run page-loader."""
    url, dir_path = parse_arguments()
    try:
        download(url, dir_path)
    except (NetworkError, FileSystemError):
        sys.exit(1)
    logger.info('Page was successfully downloaded into {0}'. format(dir_path))


if __name__ == '__main__':
    main()
