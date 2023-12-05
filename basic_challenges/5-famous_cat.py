#!/usr/bin/python3

# Shorter version
def find_famous_cat(cats):
  mayor = 0  
  for c in cats:
    fans = sum(c['followers'])
    if fans > mayor:
      mayor = fans
  cat = []
  for c in cats:
    if sum(c['followers']) == mayor:
      cat.append(c['name'])
  return cat

# Larger version
def find_famous_cat2(cats):
  fans = []
  for d in cats:
    fans.append(sum(d['followers']))
  mayor = fans[0]
  for n in fans:
    if n > mayor:
      mayor = n
  cat = []  
  for c in cats:
    if sum(c['followers']) == mayor:
      cat.append(c['name'])
  return cat

print(find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
]))

print(find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
]))
