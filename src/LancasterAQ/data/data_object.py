import json
from logging import warning
from typing import TYPE_CHECKING, List, Dict, Any
from importlib.resources import files, as_file

import networkx as nx
from networkx.readwrite import json_graph
import pandas as pd
import warnings
import numpy as np
import abc
import geopandas as gpd
import os
import osmnx as ox
import pickle

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

    def to_geopandas(self) -> gpd.GeoDataFrame:
        """Convert to a :class:`geopandas.GeoDataFrame` object."""
        gdf = gpd.GeoDataFrame(
            self.data, geometry=gpd.points_from_xy(self.data.lon, self.data.lat))
        gdf = gdf.set_crs('EPSG:4326')
        gdf = ox.projection.project_gdf(gdf)
        return gdf

    def to_geopandas_with_metadata(self) -> gpd.GeoDataFrame:
        """Convert to a :class:`geopandas.GeoDataFrame` object, with open street map metadata from edges."""
        gdf_path = files("LancasterAQ.data").joinpath("gdf_with_metadata.pkl")
        if os.path.exists(gdf_path):
            warnings.warn("Using pre-cached geodataframe with metadata")
            gdf = pickle.load(open(gdf_path, 'rb'))
        else:
            warnings.warn("This method takes up to two minutes to retrieve all the metadata. You could save the gdf if you wanted.")
            gdf = self.to_geopandas()

            G = ox.graph_from_bbox(gdf.lat.max(), gdf.lat.min(), gdf.lon.max(), gdf.lon.min(), network_type='all')
            # Project the graph to UTM
            P = ox.projection.project_graph(G)

            # Get projected node coordinates
            x = gdf.geometry.x
            y = gdf.geometry.y

            # We first need to find the edges on the graph that are closest to the points
            edges = ox.distance.nearest_edges(P, x, y)
            edge_info = pd.DataFrame([P.get_edge_data(edge[0], edge[1])[0] for edge in edges])

            for col in edge_info.columns:
                gdf[col] = edge_info[col] 

            pickle.dump(gdf, open(gdf_path, 'wb'))

        return gdf


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
