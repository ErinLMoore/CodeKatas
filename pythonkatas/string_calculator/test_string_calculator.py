import unittest
import mock
import string_calculator
from string_calculator import add
from log import log

class testStringCalculator(unittest.TestCase):

    def test_returns_zero_for_an_empty_string(self):
        expected = "0"
        actual = add("")
        self.assertEqual(expected, actual)

    def test_if_given_a_two_returns_a_two(self):
        expected = "2"
        actual = add("2")
        self.assertEqual(expected, actual)

    def test_if_given_a_four_returns_a_four(self):
        expected = "4"
        actual = add("4")
        self.assertEqual(expected, actual)

    def test_adds_one_and_one_and_returns_two(self):
        expected = "2"
        actual = add("1,1")
        self.assertEqual(expected,actual)

    def test_adds_two_strings_returns_sum(self):
        expected = "807"
        actual = add("747,60")
        self.assertEqual(expected,actual)

    def test_adds_three_strings_returns_sum(self):
        expected = "809"
        actual = add("747,60,2")
        self.assertEqual(expected,actual)

    def test_can_use_newlines_to_delimit(self):
        expected = "2"
        actual = add("1\n1")
        self.assertEqual(expected,actual)

    def test_can_use_custom_chars_to_delimit(self):
        expected = "2"
        actual = add("\\@\n1@1")
        self.assertEqual(expected,actual)

    def test_using_negatives_returns_exception_string(self):
        expected = "negatives not allowed: -2"
        actual = add("-2")
        self.assertEqual(expected,actual)

    def test_negatives_and_positive_mix_returns_negatives(self):
        expected = "negatives not allowed: -2"
        actual = add("1,-2")
        self.assertEqual(expected,actual)

    def test_numbers_larger_than_1000_are_ignored(self):
        expected = "2"
        actual = add("2,1001")
        self.assertEqual(expected,actual)

    def mocklog(results):
        print "a mocked log" + ' ' +results

    @mock.patch('string_calculator.log', side_effect=mocklog)
    def test_when_add_is_called_logger_is_called_with_add_result(self, log_function):
        add("1,1")
        string_calculator.log.assert_called_with("2")

    def mockwrite(results):
        pass

    @mock.patch('__builtin__.open')
    def test_log_writes_to_file(self, open_mock):
        log("2")
        assert open_mock.called
