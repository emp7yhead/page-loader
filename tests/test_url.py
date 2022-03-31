"""Test for downloader."""

import pytest
from page_loader.loader import url

TEST_TEMPLATE = [
    ['https://en.wikipedia.org/Python', 'en-wikipedia-org-Python.html'],
    ['https://en.wikipedia.org/Python.js', 'en-wikipedia-org-Python.js'],
]


@pytest.mark.parametrize('test_case, expected_result', TEST_TEMPLATE)
def test_get_name(test_case, expected_result):
    """Test for url with and without scheme.

    Args:
        test_case: test url with/without scheme.
        expected_result: corect function result.
    """
    test_result = url.get_name(test_case)
    assert test_result == expected_result
