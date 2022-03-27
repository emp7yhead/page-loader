"""Tests for loader."""

import os
import tempfile
import pytest
import requests
import requests_mock
from page_loader.loader.loader import download
from page_loader.logger.exceptions import FileSystemError, NetworkError

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


def test_download_io_error(requests_mock):
    """Test raising FileSystemError.

    Args:
        requests_mock: for mocking test url.
    """
    requests_mock.get(TEST_URL, text='<html>\n</html>')
    with pytest.raises(FileSystemError):
        download(TEST_URL, '/directory/doesnt/exist')


def test_download_network_error():
    """Test raising NetworkError.

    Args:
        requests_mock: for mocking test url.
    """
    with requests_mock.Mocker() as mock:
        mock.get(TEST_URL, status_code=404)
        with tempfile.TemporaryDirectory() as tmpdirname:
            with pytest.raises(NetworkError):
                download(TEST_URL, tmpdirname)
