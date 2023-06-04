import unittest

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# We use this file to run all tests

loader = unittest.TestLoader()
start_dir = 'tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
