#!/usr/bin/python3

# update dictionary with `update()` function
def createTaskPlanner():
  tasks = []
  def addTask(task):
    task.update({
      'id': task['id'],
      'name': task['name'],
      'priority': task['priority'],
      'tags': task['tags'],
      'completed': False, # create a key-value element
    })
    tasks.append(task)

  return {
    'addTask': addTask,
    'tasks': tasks,
  }

# create a closure
planner = createTaskPlanner()

# use the closure to add a task
planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

print(planner['tasks'])
