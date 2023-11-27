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
        #     'completed': False, # create a key-value element with False even if you pass True
        # })
        # tasks.append(task)

        # # create a new dictionary with new values and append to the list
        # update_task = {
        #     'id': task['id'],
        #     'name': task['name'],
        #     'priority': task['priority'],
        #     'tags': task['tags'],
        #     # 'completed': True if task['completed'] == True else False, # look for completed key, throws a key error if 'complete' key is not present
        #     # 'completed': task['completed'] if 'completed' in task else False, # same result as below
        #     'completed': task.get('completed', False),  # TAKE A LOOK AT THE END, get() function definition
        # }
        # tasks.append(update_task)

        # since we are passing the dict we just need to set/create the 'completed' key 
        task['completed'] = task.get('completed', False)   # TAKE A LOOK AT THE END, get() function definition
        tasks.append(task)

    # remove/delete dictionary based on 'id' or 'name' keys
    def removeTask(value):
      for item in tasks:
        if item['id'] == value or item['name'] == value:
          tasks.remove(item)
    
    # get the list of tasks
    def getTasks():
        return tasks
    
    # get all pendings tasks
    def getPendingTasks():
        # return list(filter((lambda item: item['completed'] == False), tasks))  # same as below
        return [item for item in tasks if not item['completed']]
    
    # get all completed tasks
    def getCompletedTasks():
        # return list(filter((lambda item: item['completed'] == True), tasks))  # same as below
        return [item for item in tasks if item['completed']]

    # receive 'id' or 'name' and mark the task as completed
    def markTaskAsCompleted(value):
        for item in tasks:
            if item['id'] == value or item['name'] == value:
                item['completed'] = True

    # get tasks sorted by its priority: 3: not very urgent, 2: urgent, 1: very urgent
    def getSortedTasksByPriority():
        return sorted(tasks, key=lambda item: item['priority'])

    return {
        'addTask': addTask,
        'removeTask': removeTask,
        'tasks': tasks,  # deprecated by `getTasks`
        'getTasks': getTasks,
        'getPendingTasks': getPendingTasks,
        'getCompletedTasks': getCompletedTasks,
        'markTaskAsCompleted': markTaskAsCompleted,
        'getSortedTasksByPriority': getSortedTasksByPriority,
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

planner['addTask']({
    'id': 3,
    'name': 'Test3',
    'priority': 3,
    'tags': ['coding', 'napping']
})

# planner['removeTask']('Buy milk')

# pprint(planner['getTasks']())

# pprint(planner['tasks'])  # deprecated by `getTasks`

# pprint(planner['getPendingTasks']())

# pprint(planner['getCompletedTasks']())

# planner['markTaskAsCompleted']('Test3')

pprint(planner['getSortedTasksByPriority']())

# pprint(planner['getTasks']())

'''get() method:

`get()` is a dictionary method in Python that is used to retrieve the value of a specified key.
It allows you to access the value associated with a key in a dictionary while providing
a default value if the key is not found.

The syntax for get() is as follows:
    value = dictionary.get(key, default_value)

Here's a more detailed breakdown of how it works in the context of the closure `addTask()` (see at the top):
    update_task = {
        'id': task['id'],
        'name': task['name'],
        'priority': task['priority'],
        'tags': task['tags'],
        'completed': task.get('completed', False),
    }

  - task.get('completed', False): This line attempts to retrieve the value associated with
    the key 'completed' from the task dictionary.
    If the key exists in the task dictionary, it returns the corresponding value.
    If the key is not found, it returns the default value provided as the second argument
    (in this case, False).
  - In this specific case, it means that if the input `task` dictionary has a key 'completed',
    its value will be used for the 'completed' key in the `update_task` dictionary.
    If the 'completed' key is not present in the input task,
    the default value False will be used.
'''
