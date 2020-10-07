import pytest

from linvie.adapters.flix_repository import FlixRepository

repo = FlixRepository("../linvie/data/Data1000Movies.csv")
def test_ss():
    iron,els=repo.find("iron man")
    iron=iron[0]
    print(iron.name)