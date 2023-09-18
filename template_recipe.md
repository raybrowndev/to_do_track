# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

class ClassName:
    def __init__(self, name, list):
        self._name = name
        self._list = []
class ClassName:

    def method_name(text):
        """
        Method description:

        >>Parameters: (list all parameters and their types)
            text: 
            integer: 

        >>Returns: (state the return value and its type)

        >>Side effects: (state any side effects)
        """

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

from lib.file_name import *
from lib.file_name import ClassName
import pytest 


# """
# EXAMPLE 
# """
# def test_show_upcase():
#     result = extract_uppercase("hello WORLD")
#     assert result == ["WORLD"]

"""
TEST 1: No value 
"""
with pytest.raises(Exception) as e:
        task.view_text(None) 
    error_message = str(e.value)

"""
TEST 2: 
"""
method_name("string") => []

"""
TEST 3: 
"""
def test_show_upcase():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

"""
TEST 4: 
"""

"""
TEST 5: 
"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

# """
# Given a lower and an uppercase word
# It returns a list with the uppercase word
# """
    

"""
METHOD 1
"""

def method_name()
pass 

"""
METHOD 2
"""

def method_name()
pass 


"""
METHOD 3
"""

def method_name()
pass 


"""
METHOD 4
"""

def method_name()
pass 
```

Ensure all test function names are unique, otherwise pytest will ignore them!