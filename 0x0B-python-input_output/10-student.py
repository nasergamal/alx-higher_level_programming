#!/usr/bin/python3
'''Student class'''


class Student:
    '''defining Student class'''

    def __init__(self, first_name, last_name, age):
        '''initializing student instance

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=''):
        '''return all instance for student as dictionary'''
        if not attrs or not any(hasattr(self, attr) for attr in attrs):
            return self.__dict__
        return {key: self.__dict__[key] for key in attrs if hasattr(self, key)}
