import pytest # <-- New code
from lib.reading_time import *

def test_added_contents():
    p = Present()
    p.wrap("word")
    result = p.unwrap()
    assert result == "word"

def test_contents():
    p = Present()
    with pytest.raises(Exception) as e:
        p.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_already_wrapped():
    p =  Present()
    p.wrap("word")
    with pytest.raises(Exception) as e:
        p.wrap("another word")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."