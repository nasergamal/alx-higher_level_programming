#!/usr/bin/python3
'''unit tests for scare class'''
import unittest
from io import StringIO
import sys
from unittest.mock import patch
from models.square import Square


class test_Square(unittest.TestCase):
    '''square class basics unit tests'''
    def test_no_arg(self):
        self.assertRaises(TypeError, Square)

    def test_two_arg(self):
        s1 = Square(1)
        s2 = Square(3)
        self.assertEqual(1, s1.size)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(3, s2.size)
        self.assertEqual(0, s1.x)
        self.assertEqual(0, s1.y)
        self.assertEqual(0, s2.x)
        self.assertEqual(0, s2.y)

    def test_square_size_setter(self):
        s1 = Square(1)
        s1.size = 5
        self.assertEqual(5, s1.size)

    def test_square_x_setter(self):
        s1 = Square(1)
        s1.x = 5
        self.assertEqual(5, s1.x)

    def test_square_y_setter(self):
        s1 = Square(1)
        s1.y = 5
        self.assertEqual(5, s1.y)

    def test_3to4_arg(self):
        s1 = Square(1, 3)
        s2 = Square(3, 5, 6)
        self.assertEqual(1, s1.size)
        self.assertEqual(3, s2.size)
        self.assertEqual(3, s1.x)
        self.assertEqual(0, s1.y)
        self.assertEqual(5, s2.x)
        self.assertEqual(6, s2.y)

    def test_5_args(self):
        self.assertEqual(99, Square(1, 3, 4, 99).id)

    def test_more_args(self):
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 99, 6)

    def test_private_atts(self):
        s1 = Square(3, 4, 5, 6)
        with self.assertRaises(AttributeError):
            s1.__size

    def test_private_attxy(self):
        s1 = Square(3, 4, 5, 6)
        with self.assertRaises(AttributeError):
            s1.__x
            s1.__y

    def test_type_s(self):
        with self.assertRaises(TypeError):
            Square('a', 4)
            Square(3.5, 4)
            Square(5, 'a')
            Square(3, 4.5)

    def test_type_errormsg_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('a', 4)

    def test_type_xy(self):
        with self.assertRaises(TypeError):
            Square(3, 4, 'a', 6)
            Square(3, 4, 5.5, 6)
            Square(3, 4, 5, 'b')
            Square(3, 4, 5, 6.5)

    def test_type_errormsg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, 'a', 6)

    def test_type_errormsg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 6, 'b')

    def test_value_size(self):
        with self.assertRaises(ValueError):
            Square(0, 4, 5, 6)
            Square(-5, 4, 5, 6)

    def test_value_errormsg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 4, 5, 6)
            Square(-5, 4, 5, 6)

    def test_value_x(self):
        self.assertEqual(4, Square(3, 4).x)
        with self.assertRaises(ValueError):
            Square(5, 4, -5, 6)

    def test_value_errormsg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -5, 6)

    def test_value_y(self):
        self.assertEqual(5, Square(3, 4, 5).y)
        with self.assertRaises(ValueError):
            Square(3, 5, -6)

    def test_value_errormsg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -6)


class Test_Square_area(unittest.TestCase):
    '''area unittests'''
    def test_square_area(self):
        self.assertEqual(9, Square(3, 5, 0).area())

    def test_square_XLsize_area(self):
        self.assertEqual(99999999999980000000000001,
                         Square(9999999999999, 9999999999999).area())

    def test_square_afterchange_area(self):
        s1 = Square(3, 4, 5)
        s1.size = 5
        self.assertEqual(25, s1.area())

    def test_square_areawarguments(self):
        s1 = Square(3, 4, 5, 0)
        with self.assertRaises(TypeError):
            s1.area(3, 4)


class Test_Square_display(unittest.TestCase):
    '''display unittests'''
    @staticmethod
    def output_cap(s, m):
        c, b = StringIO(), sys.stdout
        sys.stdout = c
        if m == 'display':
            s.display()
        else:
            print(s)
        sys.stdout = b
        return c

    def test_square_display(self):
        s1 = Square(4)
        c = Test_Square_display.output_cap(s1, 'display')
        self.assertEqual('####\n####\n####\n####\n', c.getvalue())

    def test_square_display2(self):
        s1 = Square(1)
        c = Test_Square_display.output_cap(s1, 'display')
        self.assertEqual('#\n', c.getvalue())

    def test_square_display2_with_arg(self):
        s1 = Square(4)
        self.assertRaises(TypeError, s1.display, 1)

    def test_square_display_withx(self):
        s1 = Square(4, 2, 0)
        c = Test_Square_display.output_cap(s1, 'display')
        self.assertEqual('  ####\n  ####\n  ####\n  ####\n', c.getvalue())

    def test_square_display_withy(self):
        s1 = Square(4, 0, 2)
        c = Test_Square_display.output_cap(s1, 'display')
        self.assertEqual('\n\n####\n####\n####\n####\n', c.getvalue())

    def test_square_display_withxy(self):
        s1 = Square(4, 2, 2)
        c = Test_Square_display.output_cap(s1, 'display')
        self.assertEqual('\n\n  ####\n  ####\n  ####\n  ####\n', c.getvalue())


class Test_Square_str(unittest.TestCase):
    '''test string representation of square class'''
    def test_square_str(self):
        s1 = Square(4)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_str_withx(self):
        s1 = Square(4, 3)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 3/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_str_withy(self):
        s1 = Square(4, 0, 3)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/3 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_str_withxy(self):
        s1 = Square(4, 1, 3)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 1/3 - 4'
        self.assertEqual(expected, c.getvalue().strip())


class Test_Square_update_args(unittest.TestCase):
    '''update function Unittests'''
    def test_square_update_onearg(self):
        s1 = Square(4, 0, 0)
        s1.update()
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_oneNone(self):
        s1 = Square(4, 0, 0)
        s1.update(None)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_onearg(self):
        s1 = Square(4, 0, 0)
        s1.update(1)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 0/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_twoearg(self):
        s1 = Square(4, 0, 0)
        s1.update(1, 2)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 0/0 - 2'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_threearg(self):
        s1 = Square(4, 0, 0)
        s1.update(1, 2, 3)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 3/0 - 2'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_fourarg(self):
        s1 = Square(4, 0, 0)
        s1.update(1, 2, 3, 4)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 3/4 - 2'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_fivearg(self):
        s1 = Square(4, 0, 0)
        s1.update(1, 2, 3, 4, 5)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 3/4 - 2'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_invalid_size_type(self):
        s1 = Square(4, 6, 0, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(1, 'string')

    def test_square_update_invalid_size_value(self):
        s1 = Square(4, 6, 0, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(1, 0)

    def test_square_update_invalid_x_type(self):
        s1 = Square(4, 0, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(1, 2, 'string')

    def test_square_update_invalid_x_value(self):
        s1 = Square(4, 0, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(1, 2, -3)

    def test_square_update_invalid_y_type(self):
        s1 = Square(4, 0, 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(1, 2, 3, 'string')

    def test_square_update_invalid_y_value(self):
        s1 = Square(4, 0, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(1, 2, 3, -4)


class Test_Square_update_kwargs(unittest.TestCase):
    '''update function Unittests'''
    def test_square_update_kwNone(self):
        s1 = Square(4)
        s1.update(id=None)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_id(self):
        s1 = Square(4, 0, 0)
        s1.update(id=1)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 0/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_size(self):
        s1 = Square(4, 0, 0)
        s1.update(size=2)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/0 - 2'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_x(self):
        s1 = Square(4, 0, 0)
        s1.update(x=4)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 4/0 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_y(self):
        s1 = Square(4, 0, 0)
        s1.update(y=5)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = f'[Square] ({s1.id}) 0/5 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_twokw(self):
        s1 = Square(4, 0, 0)
        s1.update(id=1, y=5)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 0/5 - 4'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_allkw(self):
        s1 = Square(4, 0, 0)
        s1.update(x=4, id=1, y=5, size=2)
        c = Test_Square_display.output_cap(s1, 'print')
        expected = '[Square] (1) 4/5 - 2'
        self.assertEqual(expected, c.getvalue().strip())

    def test_square_update_invalid_kwsize_value(self):
        s1 = Square(4, 0, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(size=0)


class TestSquare_to_dictionary(unittest.TestCase):
    '''to dictionary function unittests'''
    def test_square_dict(self):
        s1 = Square(2, 3, 4, 1)
        expected = {'x': 3, 'y': 4, 'id': 1, 'size': 2}
        self.assertDictEqual(expected, s1.to_dictionary())

    def test_square_dict_copy(self):
        s1 = Square(2, 3, 4, 1)
        s2 = Square(4, 1, 2, 3)
        s2.update(s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_square_dict_witharg(self):
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s1.to_dictionary(1)
