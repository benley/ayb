import config

test_constants = config.load_configs('config/tests/test_constants.py', 'config/tests/test_constants2.py')
assert test_constants.test == 1
assert test_constants.test2 == 2
#assert test_constants.test3 == 3
print test_constants._vars()
