"""Tests for loader."""

import os
import tempfile

import pytest
import requests
import requests_mock
from page_loader.loader.loader import download, get_content, save

TEST_URL = 'http://test.com'


@pytest.fixture
def page_without_resources():
    return '<html>\n</html>'


def test_download(requests_mock, page_without_resources):
    requests_mock.get(TEST_URL, text=page_without_resources)
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        page_path = download(TEST_URL, path)
        expected_path = os.path.join(path, 'test-com.html')
        with open(page_path, 'r') as test_file:
            assert test_file.read() == requests.get(TEST_URL).text
    assert expected_path == page_path


def test_save():
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_path = os.path.join(tmpdirname, 'test')
        result_test_path = save(test_path, 'hello')
        with open(result_test_path, 'r') as test_file:
            assert test_file.read() == 'hello'
    assert result_test_path == test_path


def test_get_content():
    with requests_mock.Mocker() as mock:
        test_content = 'bytestring'.encode()
        mock.get(TEST_URL, content=test_content)
        assert get_content(TEST_URL) == test_content
