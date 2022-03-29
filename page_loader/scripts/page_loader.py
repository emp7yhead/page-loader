"""Page-loader main script."""
import sys

from page_loader.cli.cli import parse_arguments
from page_loader.loader.loader import download
from page_loader.logger.exceptions import FileSystemError, NetworkError
from page_loader.logger.logger_setup import setup_logging

setup_logging()


def main() -> str:
    """Run page-loader.

    Returns:
        str.
    """
    url, dir_path = parse_arguments()
    try:
        local_page_path = download(url, dir_path)
    except (NetworkError, FileSystemError):
        sys.exit(1)
    return local_page_path


if __name__ == '__main__':
    main()
