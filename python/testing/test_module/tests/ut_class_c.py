import os
import unittest

from test_module.class_c import ClassC


def suite():
    """Create test suite from ClassCTestCase unit test class and return"""
    return unittest.TestLoader().loadTestsFromTestCase(ClassCTestCase)


class ClassCTestCase(unittest.TestCase):

    def setUp(self):
        self.orig_dir = os.getcwd()
        self.instance = ClassC()

    def tearDown(self):
        del self.instance
        self.instance = None
        self.func_dict = None

    def test_init(self):
        self.assertEqual(self.instance._a, 3)
        self.assertEqual(self.instance._b, 'foobar')
        self.assertEqual(self.instance._c, None)
        self.assertDictEqual(self.instance._d, {'a': True, 'b': 123})

    def test_property_getter(self):
        self.assertDictEqual(self.instance.d, {'a': True, 'b': 123})

    def test_property_setter(self):
        self.assertDictEqual(self.instance.d, {'a': True, 'b': 123})
        self.instance.d = {'a': False, 'b': 321}
        self.assertDictEqual(self.instance.d, {'a': False, 'b': 321})
        with self.assertRaises(TypeError):
            self.instance.d = 'foobar'


if __name__ == '__main__':
    print("You muh-muh-make me hah-pay.")
