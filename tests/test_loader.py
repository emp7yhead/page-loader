"""Tests for loader."""
from pathlib import Path
import tempfile
from urllib.parse import urljoin
import httpx

import pytest
from page_loader.loader import download

TEST_URL = 'http://test.com'
TEST_PAGE = '/page.html'
TEST_PAGE_URL = urljoin(TEST_URL, TEST_PAGE)
TEST_FILE_NAME = 'test-com-page.html'
ASSETS_DIR_NAME = 'test-com-page_files'
EXPECTED_PAGE = 'expected_result.html'


def get_fixture_path(file_name):
    current_dir = Path().cwd()
    return current_dir.joinpath(current_dir, 'tests/fixtures', file_name)


def read(file_path):
    with Path.open(file_path) as f:
        result = f.read()
    return result


def get_fixture_data(file_name):
    return read(get_fixture_path(file_name))


@pytest.mark.asyncio
async def test_connection_error(respx_mock):
    invalid_url = 'https://badsite.com'
    expected_exception = httpx.ConnectError
    respx_mock.get(invalid_url).mock(side_effect=expected_exception)

    with tempfile.TemporaryDirectory() as tmpdirname:

        with pytest.raises(expected_exception):
            assert await download(invalid_url, tmpdirname)


@pytest.mark.parametrize('code', [404, 500])
@pytest.mark.asyncio
async def test_response_with_error(respx_mock, code):
    url = urljoin(TEST_URL, str(code))
    respx_mock.get(url).mock(return_value=httpx.Response(code))

    with tempfile.TemporaryDirectory() as tmpdirname:
        with pytest.raises(httpx.HTTPError):
            assert await download(url, tmpdirname)


@pytest.mark.asyncio
async def test_storage_errors(respx_mock):
    respx_mock.get(TEST_URL)

    root_dir_path = Path('/sys')
    with pytest.raises(OSError):
        assert await download(TEST_URL, root_dir_path)

    file_path = get_fixture_path(TEST_FILE_NAME)
    with pytest.raises(NotADirectoryError):
        assert await download(TEST_URL, file_path)

    not_exists_path = get_fixture_path('notExistsPath')
    with pytest.raises(FileNotFoundError):
        assert await download(TEST_URL, not_exists_path)


@pytest.mark.asyncio
async def test_download_without_res(respx_mock):
    respx_mock.get(TEST_URL).respond(content='<html>\n</html>\n')
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        page_path = await download(TEST_URL, path)
        expected_path = Path().joinpath(path, 'test-com.html')
        with Path(page_path).open() as test_file:
            assert test_file.read() == httpx.get(TEST_URL).text
    assert expected_path.as_posix() == page_path


@pytest.mark.asyncio
async def test_download_with_res(respx_mock):
    content = get_fixture_data(TEST_FILE_NAME)
    respx_mock.get(TEST_URL).respond(text=content)

    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname
        page_path = await download(TEST_URL, path)
        with Path(page_path).open('r') as test_file:
            test_folder = Path().joinpath(path, 'test-com_files')
            assert len(list(test_folder.iterdir())) == 3
            assert get_fixture_data(EXPECTED_PAGE) == test_file.read()
