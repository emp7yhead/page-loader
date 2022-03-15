"""Test for parser."""

import pytest
from page_loader.loader import parser

TEST_CASES = [
    ('https://ru.test.com/test.js', 'https://ru.test.com', True),
    ('https://cdn.test.com/test.js', 'https://ru.test.com', False),
]


@pytest.mark.parametrize('full_url, url, expected_result', TEST_CASES)
def test_is_local(full_url, url, expected_result):
    """Test fo local and non-local urls.

    Args:
        full_url: full_url to file.
        url: url to file.
        expected_result: expected result of test.
    """
    test_result = parser.is_local(full_url, url)
    assert test_result == expected_result
