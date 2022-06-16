# LancasterAQ Package

Python package developed for the Lancaster Air Quality project.

Included are tools to:

* Convert the graph object to different formats
* Produce exploratory plots of the data
* Fit simple models on the data

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

<details>
<summary><strike>PyPi Installation</strike> WIP </summary>

### PyPi Installation

```bash
$ pip install LancasterAQ
```

</details>

## Loading in the Lancaster AQ dataset

```python
import LancasterAQ as laq

# load the data
data = laq.dataset()
```

## Convert the data to different formats
> note: to avoid implicit data copies replace the `data` object with the dataset function call.
> For example:`data.to_numpy()` to `laq.dataset().to_numpy()` 

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

#### Convert to geopandas

``` python
# 
```

## Data exploration

``` python
#
```

## Examples of model fitting

``` python
#
```

## Further information

Measurements taken around Lancaster on the ... Measurement equipment ...
