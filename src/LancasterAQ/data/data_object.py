import json
from typing import TYPE_CHECKING, List, Dict, Any
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

__all__ = ['TabularObject', 'GraphObject']


class DataObject:
    """Base class for Lancaster Air Quality Dataset"""

    def __repr__(self):
        return "Lancaster Air Quality Dataset"

    @abc.abstractmethod
    def to_numpy(self):
        raise NotImplementedError


class TabularObject(DataObject):
    """Tabular dataset for Lancaster Air Quality Dataset"""

    def __init__(self):
        data_path = files("LancasterAQ.data").joinpath("processed_data.csv")
        self.data: pd.DataFrame = pd.read_csv(data_path)
        """The :class:`pandas.DataFrame` object"""

    def to_numpy(self, **kwargs) -> np.ndarray:
        """Convert to a NumPy array.

        Alias for :class:`pandas.Dataframe.to_numpy()`,
        see `Pandas documentation
        <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html>`_
        for further details.
        """
        return self.data.to_numpy(**kwargs)

    def to_pandas(self) -> pd.DataFrame:
        """Returns the internal :class:`pandas.Dataframe` object."""
        return self.data


class GraphObject(DataObject):
    """Graph dataset for Lancaster Air Quality Dataset"""

    def __init__(self):
        data_path = files("LancasterAQ.data").joinpath("lancaster.gpickle")
        with as_file(data_path) as lancaster_data_path:
            self.graph: MultiGraph = read_pickle(lancaster_data_path)
            """The :class:`nextworkx.MultiGraph` object"""

    def to_numpy(self, **kwargs) -> np.ndarray:
        """Returns graph object as :class:`numpy.ndarray`

        Alias for :func:`networkx.convert_matrix.to_numpy_array()`
        """
        g = nx.to_numpy_array(self.graph, **kwargs)
        return g

    def to_dict(self, **kwargs) -> Dict:
        """Returns adjacency representation of graph as a dictionary of dictionaries.

        Alias for :func:`networkx.to_dict_of_dicts()`
        """
        g = nx.to_dict_of_dicts(self.graph, **kwargs)
        return g

    def to_edgelist(self, **kwargs) -> List:
        """Returns a list of edges in the graph

        Alias for :func:`nx.to_edgelist()`
        """
        g = nx.to_edgelist(self.graph, **kwargs)
        return g

    def to_dict_of_lists(self, **kwargs) -> Dict[Any, List]:
        """Returns adjacency representation of graph as a dictionary of lists.

        Alias for :func:`networkx.to_dict_of_lists()`
        """
        g = nx.to_dict_of_lists(self.graph, **kwargs)
        return g

    def to_scipy(self, **kwargs):
        """Returns a `SciPy Sparse array <https://docs.scipy.org/doc/scipy/reference/sparse.html>`_.

        Hint: Scipy sparse matrices are faster for matrices comprised
        of mostly zeros.

        Alias for :func:`networkx.to_scipy_sparse_array()`.
        """
        g = nx.to_scipy_sparse_array(self.graph, **kwargs)
        return g

    def to_json(self) -> str:
        """Returns a JSON string using :class:`readwrite.gpickle.GraphEncoder`"""
        j = json_graph.adjacency_data(self.graph)
        return json.dumps(j, cls=GraphEncoder)
