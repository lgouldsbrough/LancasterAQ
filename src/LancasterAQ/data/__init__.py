""" The AQ data for Lancaster"""
from typing import Union

from .data_object import __all__ as options
__all__ = ["dataset"]


def dataset(arg: str='GraphObject') -> options:
    """Helper function for loading dataset

    :param arg: The type of dataset options:['GraphObject', 'TabularObject']
    :return: a dataset object instance
    """
    if arg == options[0]:
        from .data_object import GraphObject as data_object
    elif arg == options[1]:
        from .data_object import TabularObject as data_object
    else:
        raise RuntimeError(f'No dataset of type {arg} available.')

    return data_object()
