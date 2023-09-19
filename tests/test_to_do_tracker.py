from lib.to_do_tracker import *
import pytest


def test_add_one_task():
    task = ToDoTracker()
    task.add("walk the dog")
    result = task.all()
    assert result == "1: walk the dog\n"

def test_add_multiple_tasks():
    task = ToDoTracker()
    task.add("walk the dog")
    task.add("buy groceries")
    task.add("take out trash")
    result = task.all()
    assert result == '''1: walk the dog
2: buy groceries
3: take out trash
'''

def test_add_not_string():
    task = ToDoTracker()
    with pytest.raises(Exception) as e:
        task.add(889627)
    error_message = str(e.value)
    assert error_message == "Incorrect input type"



def test_mark_tasks_complete():
    task = ToDoTracker()
    task.add("walk the dog")
    task.add("buy groceries")
    task.add("take out trash")
    task.complete("walk the dog")
    result = task.all()
    assert result == '''1: buy groceries
2: take out trash
'''


def test_mark_tasks_complete2():
    task = ToDoTracker()
    task.add("walk the dog")
    task.add("buy groceries")
    task.add("take out trash")
    task.complete2(1)
    result = task.all()
    assert result == '''1: buy groceries
2: take out trash
'''
    

def test_mark_complete_not_found():
    task = ToDoTracker()
    with pytest.raises(Exception) as e:
        task.complete("water the plants")
    error_message = str(e.value)
    assert error_message == "Task not found"


def test_mark_complete2_not_found():
    task = ToDoTracker()
    with pytest.raises(Exception) as e:
        task.complete2(1)
    error_message = str(e.value)
    assert error_message == "Task not found"
