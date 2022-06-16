""" The AQ data for Lancaster"""

__all__ = ['dataset']


def dataset():
    from .data_object import DataObject
    return DataObject()
