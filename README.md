# LancasterAQ Package

Python package developed for the Lancaster Air Quality project.

Included are tools to:

* Import the dataset
* Convert the dataset to different formats

## Installation Instructions

### Manual Installation

#### Local install

```bash
# clone from github
$ git clone https://github.com/lgouldsbrough/LancasterAQ.git
# change directory into project root
$ cd LancasterAQ

# regular install
$ pip install .
# or 
# development install 
# $ pip install -e .
```

#### Directly install from GitHub

```bash
# pip install from github
pip install git+https://github.com/lgouldsbrough/LancasterAQ.git
# or `python -m pip ...` for environment safety 
```

### PyPi Installation
#### TODO

```bash
$ pip install LancasterAQ
```

## Loading in the Lancaster AQ dataset
```python
import LancasterAQ as laq

# load tabular data
data = laq.TabularObject()

# OR load the graph object
data = laq.GraphObject()
```
A helper function is also available:
```python
import LancasterAQ as laq
# load tabular data
data = laq.dataset('TabularObject')
# OR load the graph object
data = laq.dataset('GraphObject')

```

## Convert the tabular data to different formats
To avoid implicit data copies replace the `data` object with the dataset function call.

For example: replace `data.to_numpy()` with `laq.TabularObject().to_numpy()`
### Convert to a pandas dataframe

``` python
data = data.to_pandas()
```

### Convert to a numpy array

``` python
data = data.to_numpy()
```

## Convert the graph object to different formats

To avoid implicit data copies replace the `data` object with the dataset function call.

For example: replace `data.to_numpy()` with `laq.GraphObject().to_numpy()`

#### Convert to a numpy sparse array

``` python
# returns the graph adjacency matrix as a numpy array
numpy_array = data.to_numpy()
```

#### Convert to a dictionary of dictionaries

``` python
# returns adjacency representation of graph as a dictionary of dictionaries
dict_of_dicts = data.to_dict()
```

#### Convert to an edge list

``` python
# returns a list of edges in the graph
edge_list = data.to_edgelist()
```

#### Convert to a dictionary of lists

``` python
# returns adjacency representation of graph as a dictionary of lists
dict_of_lists = data.to_dict_of_lists()
```

#### Convert to a scipy sparse array

``` python
# returns the graph adjacency matrix as a scipy sparse array
scipy_sparse_array = data.to_scipy()
```

#### Convert to JSON

``` python
# returns json object of graph
data_json = data.to_json()
```

## Example notebook

An introductory notebook can be found within the [examples folder](examples/introduction.ipynb).

<sub>Note: requires [Matplotlib](https://matplotlib.org/stable/users/getting_started/index.html#installation-quick-start) 
and [Seaborn](https://seaborn.pydata.org/installing.html)
packages.</sub>

