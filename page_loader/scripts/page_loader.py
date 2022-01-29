"""Page-loader main script."""

from page_loader.cli import cli
from page_loader.loader import loader


def main() -> None:
    """Run page-loader."""
    dir_path, url = cli.parse_arguments()
    loader.download(url, dir_path)


if __name__ == '__main__':
    main()
