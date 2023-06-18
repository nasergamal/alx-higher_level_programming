#!/usr/bin/python3
'''square calculations class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return printable detail of rectangle'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''Return size'''
        return self.width

    @size.setter
    def size(self, size):
        '''Set size'''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''update attributes'''
        if args and len(args) != 0:
            for num, arg in enumerate(args):
                if num == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                        continue
                    self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                        continue
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        '''Return dictionary representation of the Square'''
        square_dict = {'id': self.id, 'x': self.x,
                       'size': self.size, 'y': self.y}
        return square_dict
