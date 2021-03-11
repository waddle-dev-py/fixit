from tempfile import TemporaryDirectory
from pathlib import Path
import logging
import datetime

import pytest

import fixit.util


@pytest.fixture(scope='function')
def setup_get_logger():
    temp_directory = TemporaryDirectory()
    yield Path(temp_directory.name)
    logging.shutdown()
    temp_directory.cleanup()


@pytest.mark.parametrize('args, kwargs', [
    ([], dict(name='test')),
])
def test_get_logger(args, kwargs, setup_get_logger):
    path_folder = setup_get_logger

    logger = fixit.util.get_logger(*args, path_folder=path_folder, **kwargs)

    path_log = path_folder.joinpath(f'{kwargs["name"]}.log')

    assert path_log.exists()

    logger.info('test_message')

    logged = path_log.read_text()

    assert 'test_message' in logged


@pytest.mark.parametrize('args, kwargs, expected', [
    (
        [],
        dict(datetime=datetime.datetime(
            year=2020,
            month=1,
            day=1,
            hour=1,
            minute=1,
            second=1,
            microsecond=1000,
        )),
        '20200101-01:01:01.001',
    ),
])
def test_get_timestamp_fix(args, kwargs, expected):
    timestamp_fix = fixit.util.get_timestamp_fix(*args, **kwargs)
    assert timestamp_fix == expected
