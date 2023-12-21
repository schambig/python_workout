#!/usr/bin/python3
from node import PatientNode
from pprint import pprint


''' This module works in conjunction with `node.py` module '''


class PatientList:
    def __init__(self, max_beds):
        self.max_beds = max_beds
        self.available_beds = set(range(1, max_beds + 1))
        self.patients = []


    def add_patient(self, name, age):
        bed_number = self.available_beds.pop()
        new_patient = PatientNode(name, age, bed_number)
        if new_patient:
            self.patients.append(new_patient)
        else:
            raise Exception('No beds available')


lista = PatientList(3)
pprint(lista.max_beds)  # 3
pprint(lista.available_beds)  # {1, 2, 3}
pprint(lista.patients)  # []


lista.add_patient('Patient1', 20)
pprint(lista.__dict__)
# Output
# {'available_beds': {2, 3},
#  'max_beds': 3,
#  'patients': [<node.PatientNode object at 0x7ff23f0bebe0>]}
