# coding: utf-8

####################################################
# 7. Advanced
####################################################

import unittest

class TestAdvanced(unittest.TestCase):

    def test_generator(self):
        # Generators
        # A generator "generates" values as they are requested instead of storing
        # everything up front
        
        # The following method (*NOT* a generator) will double all values and store it
        # in `double_arr`. For large size of iterables, that might get huge!
        def double_numbers(iterable):
            double_arr = []
            for i in iterable:
                double_arr.append(i * 2)
            return double_arr
        
        input = [1,2,3]
        result = double_numbers(input)
        self.assertEqual(len(result), ) # length is fixed
        
        # Running the following would mean we'll double all values first and return all
        # of them back to be checked by our condition
        result = []
        for value in double_numbers(range(1000000)):  # `test_non_generator`
            if value > 5:
                break
            result.append(value)
            # 0, 2, 4
        self.assertEqual(len(result), ) # We wasted 1000K memory block and CPU time to fill it
        
        # We could instead use a generator to "generate" the doubled value as the item
        # is being requested
        def double_numbers_generator(iterable):
            for i in iterable:
                yield i + i
        
        # Running the same code as before, but with a generator, now allows us to iterate
        # over the values and doubling them one by one as they are being consumed by
        # our logic. Hence as soon as we see a value > 5, we break out of the
        # loop and don't need to double most of the values sent in (MUCH FASTER!)
        result = []
        for value in double_numbers_generator(xrange(1000000)):  # `test_generator`
            if value > 5:
                break
            result.append(value)
        self.assertEqual(len(result), )
        
        # BTW: did you notice the use of `range` in `test_non_generator` and `xrange` in `test_generator`?
        # Just as `double_numbers_generator` is the generator version of `double_numbers`
        # We have `xrange` as the generator version of `range`
        # `range` would return back and array with 1000000 values for us to use
        # `xrange` would generate 1000000 values for us as we request / iterate over those items
        
    def test_list_comprehension(self):
        # Just as you can create a list comprehension, you can create generator
        # comprehensions as well.
        values = [-x for x in [1, 2, 3, 4, 5]]
        self.assertEqual(values, )
        
        values = (-x for x in [1, 2, 3, 4, 5])
        self.assertNotEqual(values, (-1,-2,-3,-4,-5)) # values is a generator object <generator object <genexpr> at 0x10be7cc30>
        
        from types import GeneratorType
        self.assertEqual(type(values), GeneratorType)
        
        # You can also cast a generator comprehension directly to a list.
        values = (-x for x in [1, 2, 3, 4, 5])
        # duck typing - anything that can be converted into a list will be the list
        gen_to_list = list(values)
        from types import ListType
        self.assertEqual(type(gen_to_list), ListType)

    def test_decorator(self):
        # Decorators
        # A decorator is a higher order function, which accepts and returns a function.
        # Simple usage example – add_apples decorator will add 'Apple' element into
        # fruits list returned by get_fruits target function.
        def add_apples(func):
            def wrapper():
                fruits = func()
                fruits.append('Apple')
                return fruits
            return wrapper
        
        @add_apples
        def get_fruits():
            return ['Banana', 'Mango', 'Orange']
        
        # Prints out the list of fruits with 'Apple' element in it:
        # Banana, Mango, Orange, Apple
        result = ', '.join(get_fruits())
        self.assertEqual(result, )

if __name__ == '__main__':
    unittest.main()