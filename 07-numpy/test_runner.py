import os
import unittest
import importlib.util
import numpy as np

class TestNumpy(unittest.TestCase):
    def test_01_create_first_ten_primes_array(self):
        first_ten_primes_array = ans.create_first_ten_primes_array()
        np.testing.assert_equal(first_ten_primes_array, np.array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 29]))
        self.assertIsInstance(first_ten_primes_array, np.ndarray)
        self.assertEqual(first_ten_primes_array.shape, (10,))
    def test_02_create_first_ten_evens_array(self):
        first_ten_evens_array = ans.create_first_ten_evens_array()
        np.testing.assert_array_equal(first_ten_evens_array,
                                     np.array([0,  2,  4,  6,  8, 10, 12, 14, 16, 18]))
        self.assertIsInstance(first_ten_evens_array, np.ndarray)
        self.assertEqual(first_ten_evens_array.shape, (10,))
    def test_03_create_a_square_matrix(self):
        a_square_matrix = ans.create_a_square_matrix(2, 5566)
        self.assertEqual(a_square_matrix.shape, (2, 2))
        self.assertEqual(a_square_matrix.sum(), 5566 * 2**2)
        a_square_matrix = ans.create_a_square_matrix(3, 55)
        self.assertEqual(a_square_matrix.shape, (3, 3))
        self.assertEqual(a_square_matrix.sum(), 55 * 3**2)
        a_square_matrix = ans.create_a_square_matrix(4, 66)
        self.assertEqual(a_square_matrix.shape, (4, 4))
        self.assertEqual(a_square_matrix.sum(), 66 * 4**2)
    def test_04_convert_kilometers_to_miles(self):
        result_array = ans.convert_kilometers_to_miles(np.array([1.6, 3, 5, 10, 21.095, 42.195]))
        self.assertTrue(result_array[0] >= 0.9)
        self.assertTrue(result_array[1] >= 1.8)
        self.assertTrue(result_array[2] >= 3)
        self.assertTrue(result_array[3] >= 6)
        self.assertTrue(result_array[4] >= 13)
        self.assertTrue(result_array[5] >= 26)
    def test_05_create_a_diagonal_matrix(self):
        a_diagonal_matrix = ans.create_a_diagonal_matrix(2, 5566)
        self.assertEqual(a_diagonal_matrix.shape, (2, 2))
        self.assertEqual(a_diagonal_matrix.sum(), 5566 * 2)
        a_diagonal_matrix = ans.create_a_diagonal_matrix(3, 55)
        self.assertEqual(a_diagonal_matrix.shape, (3, 3))
        self.assertEqual(a_diagonal_matrix.sum(), 55 * 3)
        a_diagonal_matrix = ans.create_a_diagonal_matrix(4, 66)
        self.assertEqual(a_diagonal_matrix.shape, (4, 4))
        self.assertEqual(a_diagonal_matrix.sum(), 66 * 4)

current_directory = os.getcwd()
module_path = f"{current_directory}/answers.py"
spec = importlib.util.spec_from_file_location("answers", module_path)
ans = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ans)
suite = unittest.TestLoader().loadTestsFromTestCase(TestNumpy)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")