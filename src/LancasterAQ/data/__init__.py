""" The AQ data for Lancaster"""

__all__ = ['dataset']


def dataset():
    from .data_class import DataClass
    return DataClass()
