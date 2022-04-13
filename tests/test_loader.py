"""Tests for loader."""

import os
import tempfile

import pytest
import requests
import requests_mock
from page_loader.loader.loader import download, get_content, save

TEST_URL = 'http://test.com'
TEST_PAGE = os.path.join(os.getcwd(), 'tests/fixtures/test_page.html')
TEST_IMG = os.path.join(os.getcwd(), 'tests/fixtures/content/test_img.png')
TEST_CSS = os.path.join(os.getcwd(), 'tests/fixtures/content/test_style.css')
TEST_JS = os.path.join(os.getcwd(), 'tests/fixtures/content/test_script.js')
EXPECTED_PAGE = os.path.join(os.getcwd(), 'tests/fixtures/expected_result.html')


@pytest.fixture
def page_without_res(requests_mock):
    requests_mock.get(TEST_URL, text='<html>\n</html>')


@pytest.fixture
def page_with_test(requests_mock):
    requests_mock.get(TEST_URL, text=open(TEST_PAGE).read())
    requests_mock.get(
        'http://test.com/content/test_style.css',
        body=open(TEST_CSS, 'rb')
    )
    requests_mock.get(
        'http://test.com/content/test_img.png',
        body=open(TEST_IMG, 'rb')
    )
    requests_mock.get(
        'http://test.com/content/test_script.js',
        body=open(TEST_JS, 'rb')
    )


@pytest.fixture
def expected_page_with_res(requests_mock):
    requests_mock.get(
        'http://expected.html',
        text=open(EXPECTED_PAGE).read()
    )


def test_download_without_res(page_without_res):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        page_path = download(TEST_URL, path)
        expected_path = os.path.join(path, 'test-com.html')
        with open(page_path, 'r') as test_file:
            assert test_file.read() == requests.get(TEST_URL).text
    assert expected_path == page_path


def test_download_with_res(page_with_test, expected_page_with_res):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        page_path = download(TEST_URL, path)
        with open(page_path, 'r') as test_file:
            test_folder = os.path.join(path, 'test-com_files')
            assert len(os.listdir(test_folder)) == 3
            assert open(EXPECTED_PAGE).read() == test_file.read()


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
