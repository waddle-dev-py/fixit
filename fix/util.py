from typing import Optional, Union
from pathlib import Path
import os
import logging

TypePath = Union[Path, str, bytes, os.PathLike]


def get_logger(
        name: str,
        level: Optional[str] = None,
        path_folder: Optional[TypePath] = None,
):

    if level is None:
        level = logging.INFO

    if path_folder is None:
        path_folder = Path('../logs')

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s : %(message)s')

    file_handler = logging.FileHandler(path_folder.joinpath(f'{name}.log'), mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
