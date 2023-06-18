#!/usr/bin/python3
'''Unit tests for base model'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import remove


class test_Base (unittest.TestCase):
    '''Base class unit tests'''
    def test_no_argument(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_argument(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_argument(self):
        b1 = Base(40)
        b2 = Base(-50)
        self.assertEqual(b1.id, 40)
        self.assertEqual(b2.id, -50)

    def test_mixed_argument(self):
        b1 = Base(40)
        b2 = Base()
        b3 = Base(-50)
        b4 = Base()
        self.assertEqual(b1.id, 40)
        self.assertEqual(b3.id, -50)
        self.assertEqual(b2.id, b4.id - 1)


class Test_Base_JSON(unittest.TestCase):
    '''Json unit tests'''
    def test_to_json_string_conv_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)

    def test_to_json_string_conv_form_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4)
        dictionary = Base.to_json_string([dict(sorted(
                     r1.to_dictionary().items()))])
        self.assertIsInstance(dictionary, str)
        json_d = f'[{{"height": 2, "id": {r1.id},'\
                 ' "width": 1, "x": 3, "y": 4}]'
        self.assertEqual(json_d, dictionary)

    def test_to_json_string_conv_square(self):
        s1 = Square(1, 2, 3)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)

    def test_to_json_string_conv_form_square(self):
        s1 = Square(1, 2, 3, 4)
        dictionary = Base.to_json_string([dict(sorted(
                     s1.to_dictionary().items()))])
        self.assertIsInstance(dictionary, str)
        json_d = f'[{{"id": {s1.id}, "size": 1, "x": 2, "y": 3}}]'
        self.assertEqual(json_d, dictionary)

    def test_to_json_string_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_arg(self):
        self.assertRaises(TypeError, Base.to_json_string)

    def test_to_json_string_more_args(self):
        self.assertRaises(TypeError, Base.to_json_string, [], 1)


class Test_Base_save_to_file_json(unittest.TestCase):
    '''save_to_file function unit tests'''
    @classmethod
    def tearDown(self):
        """remove created files."""
        try:
            remove("Rectangle.json")
        except IOError:
            pass
        try:
            remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_normal_1rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(f.read()), 52)

    def test_save_to_file_normal_2rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 8, 12, 16, 22)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(f.read()), 107)

    def test_save_to_file_normal_1square(self):
        s1 = Square(1, 2, 3, 4)
        Square.save_to_file([s1])
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), 38)

    def test_save_to_file_normal_2square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 8, 12, 16)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), 78)

    def test_save_to_file_empty_list_rectangle(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_None_rectangle(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_empty_rectangle(self):
        self.assertRaises(TypeError, Rectangle.save_to_file)

    def test_save_to_file_multiple_input_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 8, 12, 16, 22)
        self.assertRaises(TypeError, Rectangle.save_to_file, [r1], [r2])

    def test_save_to_file_empty_list_square(self):
        Square.save_to_file([])
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_None_square(self):
        Square.save_to_file(None)
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_empty_square(self):
        self.assertRaises(TypeError, Square.save_to_file)

    def test_save_to_file_nonlist_Square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 8, 12, 16)
        self.assertRaises(TypeError, Square.save_to_file, [s1], [s2])

    def test_save_to_file_overwrite_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        r1.update(4, 8, 12, 16, 22)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(f.read()), 55)


class Test_Base_from_json_string(unittest.TestCase):
    '''from json functtion unit tests'''
    def test_from_json_string_emptylist_rectangle(self):
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        from_json = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)
        self.assertEqual(from_json, [])

    def test_from_json_string_None_1rectangle(self):
        json_list_input = Rectangle.to_json_string(None)
        from_json = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)
        self.assertEqual(from_json, [])

    def test_from_json_string_normal_1rectangle(self):
        list_input = [{'id': 2, 'width': 4, 'height': 8}]
        json_list_input = Rectangle.to_json_string(list_input)
        from_json = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)

    def test_from_json_string_normal_2rectangle(self):
        list_input = [{'id': 2, 'width': 4, 'height': 8},
                      {'id': 1, 'width': 2, 'height': 3}]
        json_list_input = Rectangle.to_json_string(list_input)
        from_json = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)

    def test_from_json_string_empty_rectangle(self):
        self.assertRaises(TypeError, Rectangle.from_json_string)

    def test_from_json_string_multiple_input_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 8, 12, 16, 22)
        self.assertRaises(TypeError, Rectangle.save_to_file, [r1], [r2])

    def test_from_json_string_emptylist_square(self):
        list_input = []
        json_list_input = Square.to_json_string(list_input)
        from_json = Square.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)
        self.assertEqual(from_json, [])

    def test_from_json_string_None_1square(self):
        json_list_input = Square.to_json_string(None)
        from_json = Square.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)
        self.assertEqual(from_json, [])

    def test_from_json_string_normal_1square(self):
        list_input = [{'id': 2, 'size': 3}]
        json_list_input = Square.to_json_string(list_input)
        from_json = Square.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)

    def test_from_json_string_normal_2square(self):
        list_input = [{'id': 2, 'size': 4},
                      {'id': 1, 'size': 2}]
        json_list_input = Square.to_json_string(list_input)
        from_json = Square.from_json_string(json_list_input)
        self.assertIsInstance(from_json, list)

    def test_from_json_string_empty_square(self):
        self.assertRaises(TypeError, Square.from_json_string)

    def test_from_json_string_multiple_input_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 8, 12, 16)
        self.assertRaises(TypeError, Square.save_to_file, [s1], [s2])


class Test_create(unittest.TestCase):
    '''create function unit tests'''
    def test_create_normal_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')

    def test_create_cmp_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_normal_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')

    def test_create_cmp_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


class Test_Base_load_from_file_json(unittest.TestCase):
    '''load form file function unit tests'''
    def tearDown(self):
        """remove created files."""
        try:
            remove("Rectangle.json")
        except IOError:
            pass
        try:
            remove("Square.json")
        except IOError:
            pass

    def test_no_file_rectangle(self):
        r1 = Rectangle.load_from_file()
        self.assertIsInstance(r1, list)
        self.assertEqual(r1, [])

    def test_empty_file_rectangle(self):
        with open('Rectangle.json', 'w', encoding='utf-8') as f:
            f.write("")
        self.assertIsInstance(Rectangle.load_from_file(), list)

    def test_load_from_file_normal_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(2, 4, 8, 16, 32)
        Rectangle.save_to_file([r1, r2])
        file_content = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(file_content[0]))
        self.assertEqual(str(r2), str(file_content[1]))

    def test_no_file_square(self):
        s1 = Square.load_from_file()
        self.assertIsInstance(s1, list)
        self.assertEqual(s1, [])

    def test_empty_file_square(self):
        with open('Square.json', 'w', encoding='utf-8') as f:
            f.write("")
        self.assertIsInstance(Square.load_from_file(), list)

    def test_load_from_file_normal_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(2, 4, 8, 16)
        Square.save_to_file([s1, s2])
        file_content = Square.load_from_file()
        self.assertEqual(str(s1), str(file_content[0]))
        self.assertEqual(str(s2), str(file_content[1]))


class Test_Base_load_from_file_csv(unittest.TestCase):
    '''load form file function unit tests'''
    def tearDown(self):
        """remove created files."""
        try:
            remove("Rectangle.csv")
        except IOError:
            pass
        try:
            remove("Square.csv")
        except IOError:
            pass

    def test_no_file_csv_rectangle(self):
        r1 = Rectangle.load_from_file_csv()
        self.assertIsInstance(r1, list)
        self.assertEqual(r1, [])

    def test_empty_file_csv_rectangle(self):
        with open('Rectangle.csv', 'w', encoding='utf-8') as f:
            f.write("")
        self.assertIsInstance(Rectangle.load_from_file_csv(), list)

    def test_load_from_file_csv_normal_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(2, 4, 8, 16, 32)
        Rectangle.save_to_file_csv([r1, r2])
        file_content = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(file_content[0]))
        self.assertEqual(str(r2), str(file_content[1]))

    def test_no_file_csv_square(self):
        s1 = Square.load_from_file_csv()
        self.assertIsInstance(s1, list)
        self.assertEqual(s1, [])

    def test_empty_file_csv_square(self):
        with open('Square.csv', 'w', encoding='utf-8') as f:
            f.write("")
        self.assertIsInstance(Square.load_from_file_csv(), list)

    def test_load_from_file_csv_normal_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(2, 4, 8, 16)
        Square.save_to_file_csv([s1, s2])
        file_content = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(file_content[0]))
        self.assertEqual(str(s2), str(file_content[1]))


class Test_Base_save_to_file_csv(unittest.TestCase):
    '''save_to_file function unit tests'''
    @classmethod
    def tearDown(self):
        """remove created files."""
        try:
            remove("Rectangle.csv")
        except IOError:
            pass
        try:
            remove("Square.csv")
        except IOError:
            pass

    def test_save_to_file_csv_normal_1rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r1])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '5,1,2,3,4\n')

    def test_save_to_file_csv_normal_2rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 8, 12, 16, 22)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '5,1,2,3,4\n22,4,8,12,16\n')

    def test_save_to_file_csv_normal_1square(self):
        s1 = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s1])
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '4,1,2,3\n')

    def test_save_to_file_csv_normal_2square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 8, 12, 16)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '4,1,2,3\n16,4,8,12\n')

    def test_save_to_file_csv_empty_list_rectangle(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_csv_None_rectangle(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_csv_empty_rectangle(self):
        self.assertRaises(TypeError, Rectangle.save_to_file_csv)

    def test_save_to_file_csv_multiple_input_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 8, 12, 16, 22)
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, [r1], [r2])

    def test_save_to_file_csv_empty_list_square(self):
        Square.save_to_file_csv([])
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_csv_None_square(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_csv_empty_square(self):
        self.assertRaises(TypeError, Square.save_to_file_csv)

    def test_save_to_file_csv_nonlist_Square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 8, 12, 16)
        self.assertRaises(TypeError, Square.save_to_file_csv, [s1], [s2])

    def test_save_to_file_csv_overwrite_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r1])
        r1.update(4, 8, 12, 16, 22)
        Rectangle.save_to_file_csv([r1])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '4,8,12,16,22\n')
