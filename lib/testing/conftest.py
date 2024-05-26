from lib.anagram import Anagram
import pytest

@pytest.fixture
def anagram():
    return Anagram("listen")

@pytest.fixture
def words():
    return ["enlists", "google", "inlets", "banana"]