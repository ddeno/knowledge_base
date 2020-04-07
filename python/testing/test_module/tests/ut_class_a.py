import os
import unittest

from test_module.class_a import ClassA


def suite():
    """Create test suite from ClassATestCase unit test class and return"""
    return unittest.TestLoader().loadTestsFromTestCase(ClassATestCase)


class ClassATestCase(unittest.TestCase):

    def setUp(self):
        self.orig_dir = os.getcwd()
        self.instance = ClassA()

    def tearDown(self):
        del self.instance
        self.instance = None
        self.func_dict = None

    def test_init(self):
        self.assertEqual(self.instance._a, 1)
        self.assertEqual(self.instance._b, 'foo')
        self.assertEqual(self.instance._c, False)
        self.assertEqual(self.instance._d, {'a': 'bar', 'b': 'foo'})

    def test_property_getter(self):
        self.assertEqual(self.instance.b, 'foo')

    def test_property_setter(self):
        self.assertEqual(self.instance.b, 'foo')
        self.instance.b = 'bar'
        self.assertEqual(self.instance.b, 'bar')
        with self.assertRaises(TypeError):
            self.instance.b = 21


if __name__ == '__main__':
    print("You muh-muh-make me hah-pay.")
