#!/usr/bin/env python3

"""Unit test script to test local modules."""

import unittest

from . import ut_class_a
from . import ut_class_b
from . import ut_class_c


# Define load_tests function for dynamic loading using Nose2
def load_tests(*args):
    passed_args = locals()
    suite = unittest.TestSuite()
    suite.addTests(ut_class_a.suite())
    suite.addTests(ut_class_b.suite())
    suite.addTests(ut_class_c.suite())

    return suite


# Local module level execution only
if __name__ == '__main__':
    suites = unittest.TestSuite()
    suites.addTests(ut_class_a.suite())
    suites.addTests(ut_class_b.suite())
    suites.addTests(ut_class_c.suite())

    unittest.TextTestRunner(verbosity=2).run(suites)
