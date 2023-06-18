#!/bin/python3
'''Base class for shapes calculation'''
import json
import csv
import turtle


class Base:
    '''Bass Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization
        Args:
            id (int): object id
        '''
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of input'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''write the JSON string representation of
        given lists into <class name>.json file'''
        li = []
        [li.append(cls.to_dictionary(obj)) for obj in (list_objs or [])]
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as f:
            return f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        '''return a list from the given JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                ls = cls(1, 1)
            else:
                ls = cls(1)
        ls.update(**dictionary)
        return ls

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        try:
            with open(f'{cls.__name__}.json', 'r', encoding='utf-8') as f:
                json_lists = Base.from_json_string(f.read())
                return [cls.create(**clist) for clist in json_lists]
        except Exception as e:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save instances info to csv file'''
        if cls.__name__ == 'Rectangle':
            instance_list = ['id', 'width', 'height', 'x', 'y']
        else:
            instance_list = ['id', 'size', 'x', 'y']
        with open(f'{cls.__name__}.csv', 'w', newline='') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write('[]')
            else:
                file = csv.DictWriter(f, fieldnames=instance_list)
                dlist = []
                for i in list_objs:
                    file.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Load from csv file and create instances from it'''
        try:
            with open(f'{cls.__name__}.csv', 'r', newline='') as f:
                if cls.__name__ == 'Rectangle':
                    instance_list = ['id', 'width', 'height', 'x', 'y']
                else:
                    instance_list = ['id', 'size', 'x', 'y']
                file = csv.DictReader(f, fieldnames=instance_list)
                li = []
                for di in file:
                    li.append(dict((k, int(v)) for k, v in di.items()))
                return [cls.create(**di) for di in li]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draw based on parameters'''
        m = turtle.Turtle()
        m.screen.bgcolor("#A8A8A8")
        m.shape('turtle')
        m.pensize(4)
        for i in list_rectangles:
            m.showturtle()
            m.up()
            m.setpos(i.x, i.y)
            m.down()
            m.color("#221e80", 'black')
            m.fd(i.width)
            m.left(90)
            m.fd(i.height)
            m.left(90)
            m.fd(i.width)
            m.left(90)
            m.fd(i.height)
            m.hideturtle()
        for i in list_squares:
            m.showturtle()
            m.up()
            m.setpos(i.x, i.y)
            m.down()
            m.color("#80221e", 'green')
            m.fd(i.size)
            m.left(90)
            m.fd(i.size)
            m.left(90)
            m.fd(i.size)
            m.left(90)
            m.fd(i.size)
            m.hideturtle()
        turtle.exitonclick()
