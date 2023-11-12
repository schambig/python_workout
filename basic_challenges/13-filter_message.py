#!/usr/bin/python3

# Using lambda function.
def filter_user_messages(messages, user):
  return  list(filter(lambda x: x['sender'] == user, messages))

# Using list comprehension.
def filter_user_messages2(messages, user):
  return [m for m in messages if m['sender'] == user]

# Using loop and conditional.
def filter_user_messages3(messages, user):
  lista = []
  for m in messages:
    if m['sender'] == user:
      lista.append(m)
  return lista


messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
print(filter_user_messages(messages, user))

user = 'Charlie'
print(filter_user_messages(messages, user))

user = 'Bob'
print(filter_user_messages(messages, user))
