#!/usr/bin/python3
'''Rectangle Class unit tests'''
import unittest
from io import StringIO
import sys
from unittest.mock import patch
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    '''basice Rectangle Class unit tests'''
    def test_no_arg(self):
        self.assertRaises(TypeError, Rectangle)

    def test_one_arg(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_two_arg(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(1, r1.width)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r2.width)
        self.assertEqual(4, r2.height)
        self.assertEqual(0, r1.x)
        self.assertEqual(0, r1.y)
        self.assertEqual(0, r2.x)
        self.assertEqual(0, r2.y)

    def test_3to4_arg(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5, 6)
        self.assertEqual(1, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r2.width)
        self.assertEqual(4, r2.height)
        self.assertEqual(3, r1.x)
        self.assertEqual(0, r1.y)
        self.assertEqual(5, r2.x)
        self.assertEqual(6, r2.y)

    def test_5_args(self):
        self.assertEqual(99, Rectangle(1, 2, 3, 4, 99).id)

    def test_more_args(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 99, 6)

    def test_private_attwh(self):
        r1 = Rectangle(3, 4, 5, 6)
        with self.assertRaises(AttributeError):
            r1.__width
            r1.__height

    def test_private_attxy(self):
        r1 = Rectangle(3, 4, 5, 6)
        with self.assertRaises(AttributeError):
            r1.__x
            r1.__y

    def test_type_wh(self):
        with self.assertRaises(TypeError):
            Rectangle('a', 4)
            Rectangle(3.5, 4)
            Rectangle(5, 'a')
            Rectangle(3, 4.5)

    def test_type_errormsg_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('a', 4)
            Rectangle(3.5, 4)
            Rectangle([4, 5], 4)
            Rectangle({'asd': 5}, 4)
            Rectangle((2, 4), 4)

    def test_type_errormsg_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 'a')
            Rectangle(4, 5,)
            Rectangle(4, [4, 5])
            Rectangle(4, {'asd': 5})
            Rectangle(2, (4, 4))

    def test_type_xy(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 'a', 6)
            Rectangle(3, 4, 5.5, 6)
            Rectangle(3, 4, 5, 'b')
            Rectangle(3, 4, 5, 6.5)

    def test_type_errormsg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, 'a', 6)

    def test_type_errormsg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 6, 'b')

    def test_value_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4, 5, 6)
            Rectangle(-5, 4, 5, 6)

    def test_value_errormsg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4, 5, 6)
            Rectangle(-5, 4, 5, 6)

    def test_value_height(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0, 5, 6)
            Rectangle(3, -6, 5, 6)

    def test_value_errormsg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 5, 6)
            Rectangle(3, -6, 5, 6)

    def test_value_x(self):
        self.assertEqual(0, Rectangle(3, 4, 0, 6).x)
        with self.assertRaises(ValueError):
            Rectangle(5, 4, -5, 6)

    def test_value_errormsg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 4, -5, 6)

    def test_value_y(self):
        self.assertEqual(0, Rectangle(3, 4, 5, 0).y)
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 5, -6)

    def test_value_errormsg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 4, 5, -6)


class Test_Rectangle_area(unittest.TestCase):
    '''area unittests'''
    def test_rectangle_area(self):
        self.assertEqual(12, Rectangle(3, 4, 5, 0).area())

    def test_rectangle_XLsize_area(self):
        r1 = Rectangle(9999999999999, 9999999999999)
        self.assertEqual(99999999999980000000000001,
                         Rectangle(9999999999999, 9999999999999, 0).area())

    def test_rectangle_afterchange_area(self):
        r1 = Rectangle(3, 4, 5, 0)
        r1.width = 5
        r1.height = 6
        self.assertEqual(30, r1.area())

    def test_rectangle_areawarguments(self):
        r1 = Rectangle(3, 4, 5, 0)
        with self.assertRaises(TypeError):
            r1.area(3, 4)


class Test_Rectangle_display(unittest.TestCase):
    '''display unittests'''
    @staticmethod
    def output_cap(r, m):
        c, b = StringIO(), sys.stdout
        sys.stdout = c
        if m == 'display':
            r.display()
        else:
            print(r)
        sys.stdout = b
        return c

    def test_rectangle_display(self):
        r1 = Rectangle(4, 6)
        c = Test_Rectangle_display.output_cap(r1, 'display')
        self.assertEqual('####\n####\n####\n####\n####\n####\n', c.getvalue())

    def test_rectangle_display2(self):
        r1 = Rectangle(1, 1)
        c = Test_Rectangle_display.output_cap(r1, 'display')
        self.assertEqual('#\n', c.getvalue())

    def test_rectangle_display2_with_arg(self):
        r1 = Rectangle(4, 6)
        self.assertRaises(TypeError, r1.display, 1)

    def test_rectangle_display_withx(self):
        r1 = Rectangle(4, 6, 2, 0)
        c = Test_Rectangle_display.output_cap(r1, 'display')
        self.assertEqual('  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n',
                         c.getvalue())

    def test_rectangle_display_withy(self):
        r1 = Rectangle(4, 6, 0, 2)
        c = Test_Rectangle_display.output_cap(r1, 'display')
        self.assertEqual('\n\n####\n####\n####\n####\n####\n####\n',
                         c.getvalue())

    def test_rectangle_display_withxy(self):
        r1 = Rectangle(4, 6, 2, 2)
        c = Test_Rectangle_display.output_cap(r1, 'display')
        expected = '\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n'
        self.assertEqual(expected, c.getvalue())


class Test_Rectangle_str(unittest.TestCase):
    '''test string representation of rectangle class'''
    def test_rectangle_str(self):
        r1 = Rectangle(4, 6)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_str_withx(self):
        r1 = Rectangle(4, 6, 3)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 3/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_str_withy(self):
        r1 = Rectangle(4, 6, 0, 3)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/3 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_str_withxy(self):
        r1 = Rectangle(4, 6, 1, 3)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 1/3 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())


class Test_Rectangle_update_args(unittest.TestCase):
    '''update function Unit tests'''
    def test_rectangle_update_onearg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update()
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_oneNone(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(None)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_onearg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(1)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 0/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_twoearg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(1, 2)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 0/0 - 2/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_threearg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(1, 2, 3)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 0/0 - 2/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_fourarg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(1, 2, 3, 4)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 4/0 - 2/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_fivearg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(1, 2, 3, 4, 5)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 4/5 - 2/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_morearg(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(1, 2, 3, 4, 5, 6)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 4/5 - 2/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_invalid_width_type(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(1, 'string')

    def test_rectangle_update_invalid_width_value(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, 0)

    def test_rectangle_update_invalid_height_type(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, 'string')

    def test_rectangle_update_invalid_height_value(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(1, 2, 0)

    def test_rectangle_update_invalid_x_type(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 2, 3, 'string')

    def test_rectangle_update_invalid_x_value(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(1, 2, 3, -4)

    def test_rectangle_update_invalid_y_type(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 2, 3, 4, 'string')

    def test_rectangle_update_invalid_y_value(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(1, 2, 3, 4, -5)


class Test_Rectangle_update_kwargs(unittest.TestCase):
    '''update function Unit tests'''
    def test_rectangle_update_kwNone(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(id=None)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_id(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(id=1)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 0/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_width(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(width=2)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/0 - 2/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_height(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(height=3)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/0 - 4/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_x(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(x=4)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 4/0 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_y(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(y=5)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = f'[Rectangle] ({r1.id}) 0/5 - 4/6'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_threekw(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(height=3, id=1, y=5)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 0/5 - 4/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_allkw(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(x=4, height=3, id=1, y=5, width=2)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 4/5 - 2/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_allkw(self):
        r1 = Rectangle(4, 6, 0, 0)
        r1.update(x=4, height=3, id=1, y=5, width=2)
        c = Test_Rectangle_display.output_cap(r1, 'print')
        expected = '[Rectangle] (1) 4/5 - 2/3'
        self.assertEqual(expected, c.getvalue().strip())

    def test_rectangle_update_invalid_kwwidth_value(self):
        r1 = Rectangle(4, 6, 0, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(width=0)


class TestRectangle_to_dictionary(unittest.TestCase):
    '''to dictionary function unit tests'''
    def test_rectangle_dict(self):
        r1 = Rectangle(2, 3, 4, 5, 1)
        expected = {'x': 4, 'y': 5, 'id': 1, 'height': 3, 'width': 2}
        self.assertDictEqual(expected, r1.to_dictionary())

    def test_rectangle_dict_copy(self):
        r1 = Rectangle(2, 3, 4, 5, 1)
        r2 = Rectangle(4, 5, 1, 2, 3)
        r2.update(r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_rectangle_dict_witharg(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.to_dictionary(1)
