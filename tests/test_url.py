"""Test for downloader."""

import pytest
from page_loader.loader import url

TEST_TEMPLATE = (
    (
        'https://en.wikipedia.org/wiki/Python',
        'en-wikipedia-org-wiki-Python.html',
    ),
    (
        'www.wikipedia.org/wiki/Python',
        'www-wikipedia-org-wiki-Python.html',
    ),
)


@pytest.mark.parametrize('test_case, expected_result', TEST_TEMPLATE)
def test_get_name(test_case, expected_result):
    """Test for url with and without scheme.

    Args:
        test_case: test url with/without scheme.
        expected_result: corect function result.
    """
    test_result = url.get_name(test_case)
    assert test_result == expected_result
