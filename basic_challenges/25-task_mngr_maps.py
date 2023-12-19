#!/usr/bin/python3
from pprint import pprint


class TaskManager:
    def __init__(self):
        self.tasks = {}


    def add_task(self, task, tags):
        task = task.lower()
        tags = set(tags)
        if task in self.tasks:
            self.tasks[task].update(tags)
        else:
            self.tasks[task] = tags


my_task_manager = TaskManager()
print(my_task_manager.tasks)


my_task_manager.add_task('Buy Milk', ['shopping', 'urgent'])
my_task_manager.add_task('Walk the Dog', ['pets'])
my_task_manager.add_task('Workout', ['health'])
print(my_task_manager.tasks)
