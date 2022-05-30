import LancasterAQ as laq


def test_to_numpy():
    data = laq.dataset()
    data_to_numpy = data.to_numpy()


def test_to_dict():
    data = laq.dataset()
    data_to_dict = data.to_dict()


def test_to_edgelist():
    data = laq.dataset()
    data_to_edgelist = data.to_edgelist()


def test_to_dict_of_lists():
    data = laq.dataset()
    data_to_dict_of_lists = data.to_dict_of_lists()


def test_to_scipy():
    data = laq.dataset()
    data_to_scipy = data.to_scipy()


def test_to_json():
    data = laq.dataset()
    data_to_json = data.to_json()
