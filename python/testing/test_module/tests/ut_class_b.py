import os
import unittest

from test_module.class_b import ClassB


def suite():
    """Create test suite from ClassBTestCase unit test class and return"""
    return unittest.TestLoader().loadTestsFromTestCase(ClassBTestCase)


class ClassBTestCase(unittest.TestCase):

    def setUp(self):
        self.orig_dir = os.getcwd()
        self.test_path = os.path.join('helpers', 'artifactory', 'test')
        self.instance = ClassB()

    def tearDown(self):
        del self.instance
        self.instance = None
        self.func_dict = None

    def test_init(self):
        self.assertEqual(self.instance._a, 2)
        self.assertEqual(self.instance._b, 'bar')
        self.assertEqual(self.instance._c, True)
        self.assertEqual(self.instance._d, {'a': 'foo', 'b': 'bar'})

    def test_property_getter(self):
        self.assertEqual(self.instance.a, 2)

    def test_property_setter(self):
        self.assertEqual(self.instance.a, 2)
        self.instance.a = 21
        self.assertEqual(self.instance.a, 21)
        with self.assertRaises(TypeError):
            self.instance.a = 'foobar'


if __name__ == '__main__':
    print("You muh-muh-make me hah-pay.")
