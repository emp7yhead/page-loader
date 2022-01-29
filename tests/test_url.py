"""Test for downloader."""

import tempfile

import pytest
from page_loader.loader import url

TEST_TEMPLATE = (
    (
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'en-wikipedia-org-wiki-Python-(programming-language).html',
    ),
    (
        'www.wikipedia.org/wiki/Python_(programming_language)',
        'www-wikipedia-org-wiki-Python-(programming-language).html',
    ),
)


def test_check_dir():
    """Test with existing directory."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        assert url.check_dir(path) is True


@pytest.mark.xfail
def test_check_dir_error():
    """Test for non-existent directory."""
    path = '/there/no/dir'
    assert url.check_dir(path) is True


@pytest.mark.parametrize('test_case, expected_result', TEST_TEMPLATE)
def test_get_file_name(test_case, expected_result):
    """Test for url with and without scheme.

    Args:
        test_case: test url with/without scheme.
        expected_result: corect function result.
    """
    test_result = url.get_file_name(test_case)
    assert test_result == expected_result
