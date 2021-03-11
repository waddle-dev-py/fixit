from tempfile import TemporaryDirectory
from pathlib import Path
import logging

import pytest

import fix.util


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

    logger = fix.util.get_logger(*args, path_folder=path_folder, **kwargs)

    path_log = path_folder.joinpath(f'{kwargs["name"]}.log')

    assert path_log.exists()

    logger.info('test_message')

    logged = path_log.read_text()

    assert 'test_message' in logged
