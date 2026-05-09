import pytest
from pydsa.data_structures import DisjointSet

@pytest.fixture
def ds():
    return DisjointSet()

def test_ds_initialization(ds):
    assert ds.count == 0
    assert ds.item_count == 0

def test_ds_make_set(ds):
    ds.make_set("A")
    ds.make_set("B")
    ds.make_set("C")
    assert ds.count == 3
    assert ds.item_count == 3

def test_ds_find(ds):
    ds.make_set("A")
    ds.make_set("B")
    ds.make_set("C")
    assert ds.find("A") == 0
    assert ds.find("B") == 1
    assert ds.find("C") == 2

    with pytest.raises(ValueError):
        ds.find("D")  # D does not exist

def test_ds_union(ds):
    ds.make_set("A")
    ds.make_set("B")
    ds.make_set("C")
    ds.union("A", "B")
    assert ds.find("A") == ds.find("B")
    assert ds.find("C") != ds.find("A")
    ds.union("B", "C")
    assert ds.find("A") == ds.find("C")

    with pytest.raises(ValueError):
        ds.union("A", "D")  # D does not exist
    
    with pytest.raises(ValueError):
        ds.union("D", "E")  # D and E do not exist