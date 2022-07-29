import json
from typing import TYPE_CHECKING
from importlib.resources import files, as_file

import networkx as nx
from networkx.readwrite import json_graph
import pandas as pd
import warnings
import numpy as np
import abc

from ..readwrite import read_pickle, GraphEncoder

# lazy import for type checking
if TYPE_CHECKING:
    from networkx.classes.multigraph import MultiGraph

__all__ = ["DataObject"]


class DataObject:
    def __repr__(self):
        return "Lancaster Air Quality Dataset"

    @abc.abstractmethod
    def to_numpy(self):
        raise NotImplementedError


class TabularObject(DataObject):
    def __init__(self):
        data_path = files("LancasterAQ.data").joinpath("processed_data.csv")
        self.data = pd.read_csv(data_path)

    def to_numpy(self) -> np.ndarray:
        return self.data.values

    def to_pandas(self) -> pd.DataFrame:
        return self.data


class GraphObject(DataObject):
    def __init__(self):
        data_path = files("LancasterAQ.data").joinpath("lancaster.gpickle")
        with as_file(data_path) as lancaster_data_path:
            self.graph: MultiGraph = read_pickle(lancaster_data_path)
            """The `nextworkx` multigraph object"""

    def to_numpy(self, **kwargs):
        g = nx.to_numpy_array(self.graph, **kwargs)
        return g

    def to_dict(self, **kwargs):
        g = nx.to_dict_of_dicts(self.graph, **kwargs)
        return g

    def to_edgelist(self, **kwargs):
        g = nx.to_edgelist(self.graph, **kwargs)
        return g

    def to_dict_of_lists(self, **kwargs):
        g = nx.to_dict_of_lists(self.graph, **kwargs)
        return g

    def to_scipy(self, **kwargs):
        """Returns a SciPy Sparse array.

        Hint: Scipy sparse matrices are faster matrices comprised
        of mostly zeros.
        """
        g = nx.to_scipy_sparse_array(self.graph, **kwargs)
        return g

    def to_json(self) -> str:
        j = json_graph.adjacency_data(self.graph)
        # dump as string using class GraphEncoder from readwrite.gpickle
        return json.dumps(j, cls=GraphEncoder)
