# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

class ToDoTracker():
    def __init__(self):
        self.to_do_list = []
    
    def add(self, task:str):
        if type(task) != str:
            raise Exception("Incorrect input type") 
        else:
            self.to_do_list.append(task)
            print("Test added")
    
    def all(self):
        all = ""
        for task in self.to_do_list:
            all += f"{self.to_do_list.index(task) + 1}: {task}\n"
        return all 

        
    def complete(self, task):
        if task not in self.to_do_list:
            raise Exception("Task not found") 
        for item in self.to_do_list:
            if task == item:
                self.to_do_list.remove(task)

    def complete2(self, task_num: int):
        if task_num > len(self.to_do_list):
            raise Exception("Task not found")
        for item in self.to_do_list:
            if (task_num-1) == self.to_do_list.index(item):
                self.to_do_list.remove(item)

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.