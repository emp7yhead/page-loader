import os
import pytest

from page-loader.cli import cli


def test_help_command():
    exit_status = os.system('page-loader -h')
    assert exit_status == 0


def test_cli_without_arg():
    with pytest.raises(SystemExit):
        cli.parse_arguments()
        pytest.fail()