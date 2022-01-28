"""Parse arguments for page-loader."""

import argparse
import os


def parse_arguments():
    """
    Parse options flags and url for downloading.

    Returns:
        Namespace
    """
    parser = argparse.ArgumentParser(
        prog='page-loader',
        usage='page-loader [options] <url>',
        description='Downloading web-page to local directory',
        add_help=False,
    )
    options_group = parser.add_argument_group('options')
    options_group.add_argument(
        '-o',
        '--output',
        action='store',
        default=os.getcwd(),
        help='output dir (default: "/app")',
        type=str,
    )
    options_group.add_argument(
        '-v',
        '--version',
        action='version',
        version='page-loader 0.1.0',
    )
    options_group.add_argument(
        '-h',
        '--help',
        action='help',
        help='dispaly help for command',
    )

    parser.add_argument('url')

    return parser.parse_args()
