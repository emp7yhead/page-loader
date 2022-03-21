"""Setup logging."""
import json
import logging
import logging.config
import os


def setup_logging(
    default_path: str = 'logging_config.json',
    default_level: int = logging.INFO,
) -> None:
    """Confugurate logging.

    Args:
        default_path: path to configuration JSON file.
        default_level: setup default logging level.
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as setup_file:
            config = json.load(setup_file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
