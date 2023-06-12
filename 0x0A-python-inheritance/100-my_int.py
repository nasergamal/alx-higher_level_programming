#!/usr/bin/python3
'''the inheritor of int MyInt'''


class MyInt(int):
    '''revolution on math'''
    def __eq__(self, other):
        '''check for !equallness'''
        return self.real != other

    def __ne__(self, other):
        '''check for !inequality'''
        return self.real == other
