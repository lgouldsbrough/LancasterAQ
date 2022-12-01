import numpy as np
import pandas as pd
import pytest
import LancasterAQ as laq

@pytest.fixture
def graph_object():
    return laq.GraphObject()

@pytest.fixture
def tabular_object():
    return laq.TabularObject()

def test_dataset_graph():
    dataset = laq.dataset('GraphObject')
    assert dataset
    assert isinstance(dataset, laq.GraphObject)

def test_dataset_tabular():
    dataset = laq.dataset('TabularObject')
    assert dataset
    assert isinstance(dataset, laq.TabularObject)

class TestGraphObject:
    def test_graph_object(self, graph_object):
        assert graph_object

    def test_to_numpy(self, graph_object):
        data_to_numpy = graph_object.to_numpy()
        assert isinstance(data_to_numpy, np.ndarray)

    def test_to_dict(self, graph_object):
        data_to_dict = graph_object.to_dict()

    def test_to_edgelist(self, graph_object):
        data_to_edgelist = graph_object.to_edgelist()

    def test_to_dict_of_lists(self, graph_object):
        data_to_dict_of_lists = graph_object.to_dict_of_lists()

    def test_to_scipy(self, graph_object):
        data_to_scipy = graph_object.to_scipy()

    def test_to_json(self, graph_object):
        data_to_json = graph_object.to_json()


class TestTabularObject:
    def test_tabular_object(self, tabular_object):
        assert tabular_object

    def test_to_numpy(self, tabular_object):
        assert isinstance(tabular_object.to_numpy(), np.ndarray)
