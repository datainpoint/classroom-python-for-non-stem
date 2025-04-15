import os
import unittest
import importlib.util

class TestDataTypes(unittest.TestCase):
    def test_01_convert_km_to_mile(self):
        self.assertTrue(ans.convert_km_to_mile(42.195) > 26)
        self.assertTrue(ans.convert_km_to_mile(42.195) < 27)
        self.assertTrue(ans.convert_km_to_mile(21.095) > 13)
        self.assertTrue(ans.convert_km_to_mile(21.095) < 14)
    def test_02_convert_fahrenheit_to_celsius(self):
        self.assertTrue(ans.convert_fahrenheit_to_celsius(212) >= 100.0)
        self.assertTrue(ans.convert_fahrenheit_to_celsius(32) >= 0.0)
    def test_03_calculate_bmi(self):
        self.assertTrue(ans.calculate_bmi(206, 113) >= 26)
        self.assertTrue(ans.calculate_bmi(206, 113) < 27)
        self.assertTrue(ans.calculate_bmi(211, 110) >= 24)
        self.assertTrue(ans.calculate_bmi(211, 110) < 25)
        self.assertTrue(ans.calculate_bmi(201, 104) >= 25)
        self.assertTrue(ans.calculate_bmi(201, 104) < 26)
    def test_04_show_integer_with_commas_and_digits(self):
        self.assertEqual(ans.show_integer_with_commas_and_digits(1000), "1,000.00")
        self.assertEqual(ans.show_integer_with_commas_and_digits(10000), "10,000.00")
        self.assertEqual(ans.show_integer_with_commas_and_digits(100000), "100,000.00")
        self.assertEqual(ans.show_integer_with_commas_and_digits(1000000), "1,000,000.00")
        self.assertEqual(ans.show_integer_with_commas_and_digits(10000000), "10,000,000.00")
    def test_05_convert_one_usd_to_another_currency(self):
        self.assertEqual(ans.convert_one_usd_to_another_currency("NTD", 28), "1.00 USD = 28.00 NTD")
        self.assertEqual(ans.convert_one_usd_to_another_currency("KRW", 1196), "1.00 USD = 1,196.00 KRW")
        self.assertEqual(ans.convert_one_usd_to_another_currency("JPY", 112), "1.00 USD = 112.00 JPY")

current_directory = os.getcwd()
module_path = f"{current_directory}/answers.py"
spec = importlib.util.spec_from_file_location("answers", module_path)
ans = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ans)
suite = unittest.TestLoader().loadTestsFromTestCase(TestDataTypes)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")