import unittest

class TestPrimitiveDataTypesAndOperators(unittest.TestCase):

####################################################
# 1. Primitive Datatypes and Operators
####################################################
    def test_number(self):
        # You have numbers
        self.assertEqual(3, 3)  # => 3

        # Math is what you would expect
        self.assertEqual(1 + 1, )
        self.assertEqual(8 - 1, )
        self.assertEqual(10 * 2, )
        self.assertEqual(35 / 5, )

        # Division is a bit tricky. It is integer division and floors the results
        # automatically.
        self.assertEqual(5 / 2, )

        # # To fix division we need to learn about floats.
        self.assertEqual(2.0, )  # This is a float
        self.assertEqual(11.0 / 4.0, )

        # # Result of integer division truncated down both for positive and negative.
        self.assertEqual(5 // 3, )
        self.assertEqual(5.0 // 3.0, )
        self.assertEqual(-5.0 // 3.0, )
        
        #
        # # Note that we can also import division module(Section 6 Modules)
        # # to carry out normal division with just one '/'.
        #
        self.assertEqual(divmod(11, 4), ) 
        self.assertEqual(11 / 4, )
        self.assertEqual(11 % 4, )
        
        #
        # # Modulo operation
        self.assertEqual(7 % 3, )
        #
        # # Exponentiation (x to the yth power)
        self.assertEqual(2 ** 4, )
        #
        # # Enforce precedence with parentheses
        self.assertEqual((1 + 3) * 2, )

    def test_string(self):
        # # Strings are created with " or '
        self.assertEqual("This is a string.", 'This is a string.')
        self.assertEqual('This is also a string.', "This is also a string.")
        self.assertNotEqual('Hello, "World"', "Hello, 'World'")
        self.assertEqual('\n', "\n")
        self.assertNotEqual(r'\n', '\n') # => No interpretation of \n
        #
        # # Strings can be added too!
        self.assertEqual("Hello " + "world!", )
        # # Strings can be added without using '+'
        self.assertEqual("Hello " "world!", )
        #
        # # ... or multiplied
        self.assertEqual("Hello" * 3, 
        #
        # # A string can be treated like a list of characters
        self.assertEqual("This is a string"[0],
        #
        # # You can find the length of a string
        self.assertEqual(len("This is a string"), 
        self.assertEqual("This is a string".__len__(), 
        
    def test_string_format(self):
        #
        # # String formatting with %
        # # Even though the % string operator will be deprecated on Python 3.1 and removed
        # # later at some time, it may still be good to know how it works.
        x = 'apple'
        y = 'lemon'
        z = "The items in the basket are %s and %s" % (x, y)
        self.assertEqual(z, )
        #
        # # A newer way to format strings is the format method.
        # # This method is the preferred way
        self.assertEqual("{} is a {}".format("This", "placeholder"), )
        self.assertEqual("{0} can be {1}".format("strings", "formatted"), )
        #
        # # You can use keywords if you don't want to count.
        self.assertEqual("{name} wants to eat {food}".format(name="Bob", food="lasagna"), )
        n = {'name': "Bob", 'food':"lasagna"}
        # # ** breaks the dictionary into arguments
        self.assertEqual("{name} wants to eat {food}".format(**n), )
        
    def test_boolean_operators(self):
        #
        # # Boolean Operators
        # # Note "and" and "or" are case-sensitive
        self.assertEqual(True and False, )
        self.assertEqual(False or True, )
        #
        # # Note using Bool operators with ints
        self.assertEqual(0 and 2, )
        self.assertEqual(-5 or 0, )
        self.assertEqual(0 == False, )  # => True
        self.assertEqual(2 == True, )  # => False
        self.assertEqual(1 == True, )  # => True
        #
        # # negate with not
        self.assertEqual(not True, )  # => False
        self.assertEqual(not False, )  # => True
        #
        # # Equality is ==
        # 1 == 1  # => True
        # 2 == 1  # => False
        #
        # # Inequality is !=
        # 1 != 1  # => False
        # 2 != 1  # => True
        
    def test_comparisons(self):
        #
        # # More comparisons
        self.assertEqual(1 < 10, )
        # 1 > 10  # => False
        # 2 <= 2  # => True
        # 2 >= 2  # => True
        #
        # # Comparisons can be chained!
        # 1 < 2 < 3  # => True
        self.assertEqual(2 < 3 < 2, )  # => False
        #
    def test_none(self):
        # # None is an object
        # None  # => None
        #
        # # Don't use the equality "==" symbol to compare objects to None
        # # Use "is" instead
        # assertFalse(X) is the same as assertEqual(X, False)
        self.assertEqual("etc" is None, )
        self.assertEqual(id("etc") == id(None), )
        self.assertEqual(None is None, )
        self.assertEqual(id(None) == id(None), )
        #
        # # The 'is' operator tests for object identity. This isn't
        # # very useful when dealing with primitive values, but is
        # # very useful when dealing with objects.
        #
        # # Any object can be used in a Boolean context.
        # # The following values are considered falsey:
        # #    - None
        self.assertFalse(None)
        # #    - zero of any numeric type (e.g., 0, 0L, 0.0, 0j)
        self.assertFalse(0)
        self.assertFalse(0L)
        self.assertFalse(0.0)
        self.assertFalse(0 + 0j) # complex number
        self.assertFalse('')
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(set())

    def test_bool(self):
        self.assertEqual(bool(0), )
        self.assertEqual(bool(""), )
        self.assertEqual(bool(None), )
        self.assertEqual(bool([]), )
        self.assertEqual(bool({}), )
        self.assertEqual(bool(()), )
        self.assertEqual(bool(set()), )

if __name__ == '__main__':
    unittest.main()