"""Tests for loader."""

import os
import tempfile

import requests
from page_loader.loader.loader import download

TEST_URL = 'http://test.com'


def test_loader(requests_mock):
    """Test for correct output and content.

    Args:
        requests_mock: for mocking test url.
    """
    requests_mock.get(TEST_URL, text='<html>\n</html>')
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        page_path = download(TEST_URL, path)
        expected_path = os.path.join(path, 'test-com.html')
        with open(page_path, 'r') as test_file:
            assert test_file.read() == requests.get(TEST_URL).text
    assert expected_path == page_path
