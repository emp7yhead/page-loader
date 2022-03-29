"""Tests for loader."""

import os
import tempfile
import pytest
import requests
import requests_mock
from page_loader.loader.loader import download
from page_loader.logger.exceptions import FileSystemError, NetworkError

TEST_URL = 'http://test.com'

STATUS_CODES = [
    pytest.param(
        102,
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        200,
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        303,
        marks=pytest.mark.xfail,
    ),
    404,
    503,
]


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


@pytest.mark.parametrize('test_code', STATUS_CODES)
def test_download_network_error(test_code):
    """Test raising NetworkError.

    Args:
        test_code: error status codes.
    """
    with requests_mock.Mocker() as mock:
        mock.get(TEST_URL, status_code=test_code)
        with tempfile.TemporaryDirectory() as tmpdirname:
            with pytest.raises(NetworkError):
                download(TEST_URL, tmpdirname)
