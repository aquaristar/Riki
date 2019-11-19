####################################################
# 4. Functions
####################################################

import unittest

# This is a global variable
x = 5 
class TestFunctions(unittest.TestCase):

    def test_function(self):
        # Use "def" to create new functions
        def add(x, y):
            return x + y  # Return values with a return statement

        # Calling functions with parameters
        self.assertEqual(add(5, 6), )
    
        # Another way to call functions is with keyword arguments
        self.assertEqual(add(y=, x=), 11)  # Keyword arguments can arrive in any order.
    
    def test_varargs(self):
        # You can define functions that take a variable number of
        # positional args, which will be interpreted as a tuple by using *
        def varargs(*args):
            return args
        def varargs_one(*args):
            return args[0]
            
        # returns a tuple from three variables
        self.assertEqual(varargs(1, 2, 3), )
        self.assertEqual(varargs_one(1, 2, 3), )
    
        def varargs2(*args): # *args means it collects all the arguments
            args2 = args + (-1,) # This is the way to append tuples
            return varargs(*args2) # break down the array into individual values
    
        self.assertEqual(varargs2(100,200,300), )
    
        # You can define functions that take a variable number of
        # keyword args, as well, which will be interpreted as a dict by using **
        def keyword_args(**kwargs):
            return kwargs

        # Let's call it to see what happens
        self.assertEqual(keyword_args(big="foot", loch="ness"), )
    
        # You can do both at once, if you like
        def all_the_args(*args, **kwargs):
            return str(args) + str(kwargs)
    
        # When calling functions, you can do the opposite of args/kwargs!
        # Use * to expand positional args and use ** to expand keyword args.
        args = (1, 2, 3, 4)
        kwargs = {"a": 3, "b": 4}
        self.assertEqual(all_the_args(*args), "(1, 2, 3, 4){}")
        self.assertEqual(all_the_args(1, 2, 3, 4), "(1, 2, 3, 4){}")
        self.assertEqual(all_the_args(**kwargs), ("(){'a': 3, 'b': 4}"))
        self.assertEqual(all_the_args(a = 3, b = 4),"(){'a': 3, 'b': 4}")
        self.assertEqual(all_the_args(*args, **kwargs), "(1, 2, 3, 4){'a': 3, 'b': 4}")
        self.assertEqual(all_the_args(1, 2, 3, 4, a = 3, b = 4), )
    
   
    def test_function_scope(self):
        def set_x(num):
            #Local var x not the same as global variable x
            x = num  # => 43
            return x  # => 43
        self.assertEqual(set_x(43), 43)
        self.assertEqual(x, 5)

        def set_global_x(num):
            global x
            x = num  # global var x is now set to 6
            return x  # => 6
        
        self.assertEqual(set_global_x(6), 6)
        self.assertEqual(x, 6)
    
    def test_first_class_functions(self):
        # Python has first class functions
        def create_adder(x):
            def adder(y):
                return x + y
            return adder

        add_10 = create_adder(10)
        self.assertEqual(add_10(3), 13)
        
    def test_lambda(self):
        # There are also anonymous functions
        self.assertEqual((lambda x: x > 2)(3), True)
        self.assertEqual((lambda x, y: x ** 2 + y ** 2)(2, 1), 2 ** 2 + 1 ** 2)
        #
        # There are built-in higher order functions
        def add10(x): return (x + 10)
        self.assertEqual(map(add10, [1, 2, 3]), [11, 12, 13])
        self.assertEqual(map(max, [1, 2, 3], [4, 2, 1]), [4, 2, 3])
        #
        self.assertEqual(filter(lambda x: x > 5, [3, 4, 5, 6, 7]), [6, 7])
        #
        # We can use list comprehensions for nice maps and filters
        self.assertEqual([add10(i) for i in [1, 2, 3]], [11, 12, 13])
        self.assertEqual([x for x in [3, 4, 5, 6, 7] if x > 5], [6, 7])
        #
        # You can construct set and dict comprehensions as well.
        self.assertEqual({x for x in 'abcddeef' if x in 'abc'}, {'a', 'b', 'c'})
        self.assertEqual({x: x ** 2 for x in range(5)}, {0: 0, 1: 1, 2: 4, 3: 9, 4: 16})

if __name__ == '__main__':
    unittest.main()
