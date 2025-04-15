import os
import unittest
import importlib.util

class TestDataStructures(unittest.TestCase):
    def test_01_retrieve_the_first_and_last_element(self):
        the_first_and_last_element = ans.retrieve_the_first_and_last_element([2, 3, 5, 7, 11])
        self.assertEqual(the_first_and_last_element["first"], 2)
        self.assertEqual(the_first_and_last_element["last"], 11)
        the_first_and_last_element = ans.retrieve_the_first_and_last_element([2, 3, 5])
        self.assertEqual(the_first_and_last_element["first"], 2)
        self.assertEqual(the_first_and_last_element["last"], 5)
        the_first_and_last_element = ans.retrieve_the_first_and_last_element(["Python", "Reticulate", "Anaconda"])
        self.assertEqual(the_first_and_last_element["first"], "Python")
        self.assertEqual(the_first_and_last_element["last"], "Anaconda")
        the_first_and_last_element = ans.retrieve_the_first_and_last_element(["Python", "Reticulate", "Anaconda", "Skywalker"])
        self.assertEqual(the_first_and_last_element["first"], "Python")
        self.assertEqual(the_first_and_last_element["last"], "Skywalker")
    def test_02_retrieve_the_first_three_characters(self):
        self.assertEqual(ans.retrieve_the_first_three_characters("Python"), "Pyt")
        self.assertEqual(ans.retrieve_the_first_three_characters("Reticulate"), "Ret")
        self.assertEqual(ans.retrieve_the_first_three_characters("Anaconda"), "Ana")
        self.assertEqual(ans.retrieve_the_first_three_characters("Skywalker"), "Sky")
        self.assertEqual(ans.retrieve_the_first_three_characters("Anakin"), "Ana")
    def test_03_remove_the_first_and_last_element(self):
        self.assertEqual(ans.remove_the_first_and_last_element([2, 3, 5, 7, 11]), [3, 5, 7])
        self.assertEqual(ans.remove_the_first_and_last_element(["Python", "Reticulate", "Anaconda"]), ["Reticulate"])
    def test_04_retrieve_the_middle_element(self):
        self.assertEqual(ans.retrieve_the_middle_element([2, 3, 5]), 3)
        self.assertEqual(ans.retrieve_the_middle_element([2, 3, 5, 7, 11]), 5)
        self.assertEqual(ans.retrieve_the_middle_element([2, 3, 5, 7, 11, 13, 17]), 7)
        self.assertEqual(ans.retrieve_the_middle_element([1, 2, 3]), 2)
        self.assertEqual(ans.retrieve_the_middle_element([-1, 0, 1]), 0)
    def test_05_retrieve_the_middle_three_characters(self):
        self.assertEqual(ans.retrieve_the_middle_three_characters("Steve"), "tev")
        self.assertEqual(ans.retrieve_the_middle_three_characters("Stark"), "tar")
        self.assertEqual(ans.retrieve_the_middle_three_characters("Natasha"), "tas")
        self.assertEqual(ans.retrieve_the_middle_three_characters("Skywalker"), "wal")
        self.assertEqual(ans.retrieve_the_middle_three_characters("Hawkeye"), "wke")

current_directory = os.getcwd()
module_path = f"{current_directory}/answers.py"
spec = importlib.util.spec_from_file_location("answers", module_path)
ans = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ans)
suite = unittest.TestLoader().loadTestsFromTestCase(TestDataStructures)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")