#!/usr/bin/python3
from pprint import pprint # pretty-print module


def createTaskPlanner():
    tasks = []

    def addTask(task):
        # # update dictionary with `update()` function
        # task.update({
        #     'id': task['id'],
        #     'name': task['name'],
        #     'priority': task['priority'],
        #     'tags': task['tags'],
        #     'completed': False, # create a key-value element
        # })
        # tasks.append(task)

        # create a new dictionary with new values and append to the list
        update_task = {
            'id': task['id'],
            'name': task['name'],
            'priority': task['priority'],
            'tags': task['tags'],
            # 'completed': True if task['completed'] == True else False, # look for completed key, throws a key error if 'complete' key is not present
            # 'completed': task['completed'] if 'completed' in task else False, # same result as below
            'completed': task.get('completed', False),
        }
        tasks.append(update_task)

    return {
      'addTask': addTask,
      'tasks': tasks,
    }

# create a closure
planner = createTaskPlanner()

# use the closure to add a task
planner['addTask']({
    'id': 1,
    'name': 'Buy milk',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Test2',
    'priority': 2,
    'tags': ['growing', 'jumping'],
    'completed': True,
})

pprint(planner['tasks'])
