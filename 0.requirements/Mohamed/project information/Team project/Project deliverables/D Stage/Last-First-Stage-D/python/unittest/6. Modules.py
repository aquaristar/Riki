####################################################
# 6. Modules
####################################################

# You can import modules
import math
import unittest

class TestModule(unittest.TestCase):

    def test_math(self):
        self.assertEqual(math.sqrt(16), )
    
    def test_import(self):
        # You can get specific functions from a module
        from math import ceil, floor
    
        self.assertEqual(ceil(3.7), )
        self.assertEqual(floor(3.7), )
    
    def test_import2(self):
        # You can shorten module names
        import math as m
        self.assertTrue(math.sqrt(16) == m.sqrt(16))  # => True
        # you can also test that the functions are equivalent
        from math import sqrt
        self.assertTrue(math.sqrt == m.sqrt == sqrt)
    
    # Python modules are just ordinary python files. You
    # can write your own, and import them. The name of the
    # module is the same as the name of the file.
    
    # You can find out which functions and attributes
    # defines a module.
    def test_dir(self):
        res = dir(math)
        self.assertTrue(len(res) == )


# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.
if __name__ == '__main__':
    unittest.main()
