import pickle
from pathlib import Path
import json

import numpy as np
from shapely import geometry

__all__ = ['read_pickle', 'GraphEncoder']


class GraphEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, geometry.linestring.LineString):
            return np.array(obj.coords).tolist()
        return super().default(obj)


def read_pickle(file_path):
    """Read python pickle format for opening `.gpickle` and `.pickle` files
    :param file_path: file or string
    :returns:
    """
    file_path = Path(file_path)
    # maybe: check for file extension?
    with file_path.open('rb') as f:
        data = pickle.load(f)
    return data
