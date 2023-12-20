#!/usr/bin/python3
from node import PatientNode
from pprint import pprint


''' This module works in conjunction with `node.py` module '''


class PatientList:
  def __init__(self, max_beds):
    self.max_beds = max_beds
    self.available_beds = set(range(1, max_beds + 1))
    self.patients = []


lista = PatientList(3)
pprint(lista.max_beds)  # 3
pprint(lista.available_beds)  # {1, 2, 3}
pprint(lista.patients)  # []
