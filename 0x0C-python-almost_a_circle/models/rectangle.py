#!/usr/bin/python3
'''Rectangle calculation class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize shape
        Args:
            width (int): width
            heiht (int): height
            x (int): x dimension
            y (int): y dimension
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''return printable detail of rectangle'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        '''Return width'''
        return (self.__width)

    @property
    def height(self):
        '''Return height'''
        return (self.__height)

    @property
    def x(self):
        '''Return x'''
        return (self.__x)

    @property
    def y(self):
        '''Return y'''
        return (self.__y)

    @width.setter
    def width(self, width):
        '''Set width'''
        if type(width) != int:
            raise TypeError(f"width must be an integer")
        if width <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        '''Set height'''
        if type(height) != int:
            raise TypeError(f"height must be an integer")
        if height <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        '''Set x'''
        if type(x) != int:
            raise TypeError(f"x must be an integer")
        if x < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        '''Set y'''
        if type(y) != int:
            raise TypeError(f"y must be an integer")
        if y < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = y

    def area(self):
        '''Return area'''
        return ((self.__width) * (self.__height))

    def display(self):
        '''print representation of the rectangle as #'''
        x = ""
        x += "\n" * self.__y
        for h in range(self.__height):
            x += " " * self.__x
            for w in range(self.__width):
                x += "#"
            x += "\n"
        print(x, end="")

    def update(self, *args, **kwargs):
        '''update attributes'''
        if args and len(args) != 0:
            for num, arg in enumerate(args):
                if num == 0:
                    super().__init__(arg)
                elif num == 1:
                    self.width = arg
                elif num == 2:
                    self.height = arg
                elif num == 3:
                    self.x = arg
                elif num == 4:
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    super().__init__(v)
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        '''Return dictionary representation of the Rectangle'''
        rectangle_dict = {'x': self.x, 'y': self.y, 'id': self.id,
                          'height': self.height, 'width': self.width}
        return rectangle_dict
