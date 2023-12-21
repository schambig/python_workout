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


    def remove_patient(self, name):
        found_patient = None
        for patient in self.patients:
            if patient.name == name:
                found_patient = patient
                break
        if found_patient:
            self.available_beds.add(found_patient.bed_number)
            self.patients.remove(found_patient)
        else:
            raise Exception('Patient not found')


    def get_patient(self, name):
        found_patient = None
        for patient in self.patients:
            if patient.name == name:
                found_patient = patient
                break
        if found_patient:
            return {'name': found_patient.name,
                     'age': found_patient.age,
                     'bed_number': found_patient.bed_number}
        else:
            raise Exception('Patient not found')


    def get_patient_list(self):
        return [{'name': patient.name, 'age': patient.age, 'bed_number': patient.name} \
                for patient in self.patients]
    

    def get_available_beds(self):
        return self.available_beds


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


lista.add_patient('Patient2', 30)
pprint(lista.get_patient_list())
# Output
# [{'age': 20, 'bed_number': 'Patient1', 'name': 'Patient1'},
#  {'age': 30, 'bed_number': 'Patient2', 'name': 'Patient2'}]


lista.remove_patient('Patient2')
pprint(lista.get_patient_list())
# Output
# [{'age': 20, 'bed_number': 'Patient1', 'name': 'Patient1'}]


pprint(lista.get_patient('Patient1'))  # {'age': 20, 'bed_number': 1, 'name': 'Patient1'}


pprint(lista.get_available_beds())  # {2, 3}
