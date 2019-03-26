import unittest
import os
# import myAPI


class TestStringMethods(unittest.TestCase):

    def test_test1(self):
        cwd = os.getcwd()
        path = cwd + '/ml-tests/'
        input_data = open(path + 'test1.txt').readlines()
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)

    def test_test2(self):
        cwd = os.getcwd()
        path = cwd + '/ml-tests/'
        input_data = open(path + 'test2.txt').readlines()
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)

    def test_test3(self):
        cwd = os.getcwd()
        path = cwd + '/ml-tests/'
        input_data = open(path + 'test3.txt').readlines()
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)

    def test_test4(self):
        cwd = os.getcwd()
        path = cwd + '/ml-tests/'
        input_data = open(path + 'test4.txt').readlines()
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)

    def test_test5(self):
        cwd = os.getcwd()
        path = cwd + '/ml-tests/'
        input_data = open(path + 'test5.txt').readlines()
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)

    def test_test6(self):
        cwd = os.getcwd()
        path = cwd + '/ml-tests/'
        input_data = open(path + 'test6.txt').readlines()
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)

    # This test case is for testing the pipeline when given no model
    # def test_test7(self):
        # with self.assertRaises(Exception) as context:
        #     api_function(input_data)
        #
        # self.assertTrue('This is broken' in context.exception)


if __name__ == '__main__':
    unittest.main()


# def broken_function():
#     raise Exception('This is broken')
#
# class MyTestCase(unittest.TestCase):
#     def test(self):
#         with self.assertRaises(Exception) as context:
#             broken_function()
#
#         self.assertTrue('This is broken' in context.exception)
#
# if __name__ == '__main__':
#     unittest.main()
