#!/usr/bin/python3
from pprint import pprint


class TaskManager:
    def __init__(self):
        self.tasks = {}


    def add_task(self, task, tags):
        # Convert the task name to lowercase for case-insensitive comparison
        task = task.lower()
        # Convert the tags to a set to ensure uniqueness
        tags = set(tags)
        # Check if the task already exists in the dictionary
        if task in self.tasks:
             # If the task exists, update the set of tags for that task
            self.tasks[task].update(tags)
        else:
            # If the task does not exist, create a new entry with the given tags
            self.tasks[task] = tags

        # # All lines above could be replaced by this one, using the setdefault() function.
        # self.tasks.setdefault(task.lower(), set()).update(tags)


my_task_manager = TaskManager()
print(my_task_manager.tasks)  # {}


my_task_manager.add_task('Buy Milk', ['shopping', 'urgent'])
my_task_manager.add_task('Walk the Dog', ['pets'])
my_task_manager.add_task('Workout', ['health'])
print(my_task_manager.tasks)
# Output
# {'buy milk': {'shopping', 'urgent'}, 'walk the dog': {'pets'}, 'workout': {'health'}}
