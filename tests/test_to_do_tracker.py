from lib.to_do_tracker import *

def test_add_one_task():
    task = ToDoTracker()
    task.add("walk the dog")
    result = task.all()
    assert result == "1: walk the dog\n"

def test_add_multiple_tasks():
    pass

# def test_add_not_string():
#     pass

def test_mark_tasks_complete():
    pass

# def test_mark_complete_not_found():
#     pass

def test_return_all_tasks():
    pass
