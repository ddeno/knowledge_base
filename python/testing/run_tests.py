import argparse
import coverage
import os
import sys
import unittest
import logging

from io import StringIO

def run_tests(args):
    my_dir = os.path.abspath(os.path.dirname(__file__))

    loader = unittest.TestLoader()

    suites = loader.discover(start_dir=os.path.join(my_dir, 'tests'), pattern='test.py', top_level_dir=my_dir)
    overall_suite = unittest.TestSuite()
    for test_suite in suites:
        if test_suite._tests:
            overall_suite.addTests(test_suite)

    logger = logging.getLogger()
    logger.handlers = []
    logger.disabled = True
    my_test_stream = StringIO()
    runner = unittest.TextTestRunner(verbosity=args.verbosity, buffer=True)
    results = runner.run(overall_suite)


# Main execution block
if __name__ == '__main__':
    # Create our Argument Parser
    parser = argparse.ArgumentParser(description="Dictate custom arguments for the unit tests.")
    parser.add_argument("-c", "--color", action="store_true", help="Toggles color output reporting")
    parser.add_argument("-v", "--verbosity", type=int, help="Reporting level when running from the console.",
                        choices=[1, 2, 3, 4, 5], default=1)

    # Parse the arguments
    args = parser.parse_args()

    # Create code coverage object
    cov = coverage.Coverage(
        source=[os.path.abspath(os.path.dirname(__file__))]
    )

    # Start tracking code coverage
    cov.start()

    # Execute our tests
    run_tests(args)

    # Stop tracking code coverage and save results
    cov.stop()
    cov.save()

    # Create code coverage report based on environment being run in
    cov.html_report()
