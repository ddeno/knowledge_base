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

Using this example setup of the Python unittest framework can be easily updated
to fit others needs. Below details about each import file is described in order
to make use of them.

### `run_tests.py`

`run_tests.py` is intended to be located at the top-level directory of a
project. This script utilizes two key features that need to be discusses:

1. `coverage` Python Module
2. Unit Test automatic discovery

#### `coverage` Python Module

The `coverage` module allows unit tests to have code coverage tracked during
their execution. Not only are the unit test classes themselves tracked, but all
code being tested, the actual Python modules you have written will be covered.
By default, the setup will generate a HTML report. All of these artifacts can be
updated to allow for ingestion into CI/CD tools and plugins such as Jenkins and
XUnit and Cobertura Code Coverage.

#### Unit Test Automatic Discovery

In order to make `run_tests.py` as easy as possible, it utilizes the feature
within the Python `unittest` framework that can search for unit tests
automatically. This setup searchs for the diretory `tests` at the top-level
of the project. It is recommended to have tests separated from code. If that
does not fit the architecture for your project, you can update the following
line:

```
suites = loader.discover(start_dir=os.path.join(my_dir, 'tests'), pattern='test.py', top_level_dir=my_dir)
```

to something like this:

```
suites = loader.discover(start_dir=os.path.join(my_dir), pattern='test.py', top_level_dir=my_dir)
OR
suites = loader.discover(start_dir=os.path.join(my_dir, app_dir), pattern='test.py', top_level_dir=my_dir)
```

in order to search the entire module, application or project for directories
with a `test.py` script.

### `tests` Directory

The `tests` directory contains all unit test classes that are _available_ to be
executed. Typically, unit test classes are in the naming scheme of
`ut_<class-name>.py`. It is key to note that the tests directory needs to be
importable by the `unittest` moduule which simply means you must have a
`__init__.py` file. If it is wished to have a further nested directory structure
within `tests`, each folder will need its own `test.py` and `__init__.py`.

#### `test.py`

`test.py` is where one can add unit test suites to be executed. This can be
seen in the `load_tests` and `__main__` function and logic blocks respectively.
The `load_tests` function is used when auto discovery is untilized by the
`unittest` module. Those suites are returned back as a collection and aggregated
with any other potential unit test suites that have been discovered. If you
wanted to execute the `test.py` script explicity, you can do so and test suites
will be run by what is defined in the `if __name__ == '__main__':` logic block.

In short, `test.py` is where you add suites to be tested.

#### `ut_class_a.py`

Unit test case classes are intended to test actual project code. Here are the
keys features needed in each `ut_<class-name>.py` file.

1. `def suite():`
   Function that simply returns a test suite based on the class you are writing.
2. Your unit test class inherits from `unittest.TestCase`
3. `def setUp(self):`
   Test setup function that runs prior to each test. Allows one to configure
initial setup for each test the exact same way each time.
4. `def tearDown(self):`
   Test tear down or shutdown function that runs after each test. Allows one to
ensure proper destruction of instances and clean up after each test the exact
same way each time.
5. Test functions in the naming format of `test_<whatever you wish here>(self):`
6. Logic block that does not allow direct exeuction of this class file.
