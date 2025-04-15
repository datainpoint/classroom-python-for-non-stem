import os
import unittest
import importlib.util

class TestControlFlows(unittest.TestCase):
    def test_01_find_bmi_category(self):
        self.assertEqual(ans.find_bmi_category(32.90), 'Obese')
        self.assertEqual(ans.find_bmi_category(26.63), 'Overweight')
        self.assertEqual(ans.find_bmi_category(24.83), 'Normal weight')
        self.assertEqual(ans.find_bmi_category(17.58), 'Underweight')
    def test_02_check_data_type(self):
        self.assertEqual(ans.check_data_type(0), 'int')
        self.assertEqual(ans.check_data_type(1.0), 'float')
        self.assertEqual(ans.check_data_type(False), 'bool')
        self.assertEqual(ans.check_data_type(True), 'bool')
        self.assertEqual(ans.check_data_type('5566'), 'str')
        self.assertEqual(ans.check_data_type(None), 'NoneType')
    def test_03_check_data_structure_type(self):
        self.assertEqual(ans.check_data_structure_type([5, 5, 6, 6]), 'list')
        self.assertEqual(ans.check_data_structure_type((5, 5, 6, 6)), 'tuple')
        self.assertEqual(ans.check_data_structure_type({5, 6}), 'set')
        self.assertEqual(ans.check_data_structure_type({'title': 'The Shawshank Redemption', 'year': 1994}), 'dict')
    def test_04_retrieve_middle_elements(self):
        self.assertEqual(ans.retrieve_middle_elements([2, 3, 5]), 3)
        self.assertEqual(ans.retrieve_middle_elements([2, 3, 5, 7]), (3, 5))
        self.assertEqual(ans.retrieve_middle_elements([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ans.retrieve_middle_elements([2, 3, 5, 7, 11, 13]), (5, 7))
        self.assertEqual(ans.retrieve_middle_elements([2, 3, 5, 7, 11, 13, 17]), 7)
    def test_05_calculate_median(self):
        self.assertEqual(ans.calculate_median([9, 8, 3, 6, 7, 3, 1]), 6)
        self.assertAlmostEqual(ans.calculate_median([1, 3, 2, 5, 4, 9, 8, 6]), 4.5)
        self.assertEqual(ans.calculate_median([5, 6, 7]), 6)
        self.assertAlmostEqual(ans.calculate_median([3, 4, 5, 6]), 4.5)

current_directory = os.getcwd()
module_path = f"{current_directory}/answers.py"
spec = importlib.util.spec_from_file_location("answers", module_path)
ans = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ans)
suite = unittest.TestLoader().loadTestsFromTestCase(TestControlFlows)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")