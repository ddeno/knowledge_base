# Python Unit-Testing

## Overview

This setup utilizes the Python unittest module to provide a unit testing
framework. It was originally inspried by JUnit and has a similar flavor as major
unit testing frameworks in other languages. Python's unittest module supports
test automation, sharing of setup and shutdown code for tests, aggregation of
tests into collections and independence of the tests from the reporting
framework.

For more detailed information, visit the
[unittest](https://docs.python.org/3.7/library/unittest.html) module
documentation page.

For a quick link to the available types of assertions that can be made in tests,
you can view all assertions
[here](https://docs.python.org/3.7/library/unittest.html#assert-methods).

## Setup

This example scenario organized as the following:

```
testing
├── run_tests.py
├── test_module
│   ├── __init__.py
│   ├── class_a.py
│   ├── class_b.py
│   └── class_c.py
└── tests
    ├── __init__.py
    ├── test.py
    ├── ut_class_a.py
    ├── ut_class_b.py
    └── ut_class_c.py

4 directories, 21 files
```

provides an example setup that can be used across Python projects.

### Assumptions

1. Python 3.7.6
2. `test_module` can be viewed as an application, package for module directory

### Recommendations

1. Tests should be separated from source code as they should be able to live on
   their own and execute with requirement of being placed amongst the source code.
2. Tests require source code that is to be tested but not the other way around.
3. Tests should be part of a CI/CD pipeline to continually run against all
   changes going into a project.
4. Developers shoudl always run tests prior to committing to ensure changes have
   not affected other sections of the code base unknowingly.
5. Anytime a error, bug or issues is found, a test should be developed to handle
   that use-case moving forward, only further stabalizing the code base and project.

### How To Run

In order to run this specific example provided, the following commands will need
to be executed:

1. Install `coverage` module.
   ```
   pip3 install -r requirements.txt
   ```
2. Execute the tests
   ```
   python3 run_tests.py -v 2
   ```

## Usage
