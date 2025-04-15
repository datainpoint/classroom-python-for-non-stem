import os
import unittest
import importlib.util

class TestFunctions(unittest.TestCase):
    def test_01_calculate_circle_area(self):
        self.assertGreater(ans.calculate_circle_area(5), 78)
        self.assertGreater(ans.calculate_circle_area(6), 113)
        self.assertGreater(ans.calculate_circle_area(7), 153)
    def test_02_calculate_cylinder_volume(self):
        self.assertGreater(ans.calculate_cylinder_volume(5, 6), 470)
        self.assertGreater(ans.calculate_cylinder_volume(6, 5), 565)
        self.assertGreater(ans.calculate_cylinder_volume(7, 8), 1230)
    def test_03_count_number_of_divisors(self):
        self.assertEqual(ans.count_number_of_divisors(1), 1)
        self.assertEqual(ans.count_number_of_divisors(2), 2)
        self.assertEqual(ans.count_number_of_divisors(3), 2)
        self.assertEqual(ans.count_number_of_divisors(4), 3)
        self.assertEqual(ans.count_number_of_divisors(5), 2)
        self.assertEqual(ans.count_number_of_divisors(6), 4)
    def test_04_is_prime(self):
        self.assertFalse(ans.is_prime(1))
        self.assertTrue(ans.is_prime(2))
        self.assertTrue(ans.is_prime(3))
        self.assertFalse(ans.is_prime(4))
        self.assertTrue(ans.is_prime(5))
    def test_05_is_args_prime(self):
        self.assertEqual(ans.is_args_prime(1, 2, 3), [False, True, True])
        self.assertEqual(ans.is_args_prime(4, 5, 6), [False, True, False])
        self.assertEqual(ans.is_args_prime(7, 11, 13, 17, 19), [True, True, True, True, True])
        self.assertEqual(ans.is_args_prime(20, 21, 22, 24, 25, 26, 27), [False, False, False, False, False, False, False])

current_directory = os.getcwd()
module_path = f"{current_directory}/answers.py"
spec = importlib.util.spec_from_file_location("answers", module_path)
ans = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ans)
suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")