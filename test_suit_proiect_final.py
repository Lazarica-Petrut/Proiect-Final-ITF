import unittest

from HTMLTestRunner.runner import HTMLTestRunner
from sauce_demo_test import SauceDemoTestCase
from selenium_site_test import SeleniumEasyTest


class TestingClass(unittest.TestCase):

    def test_suit(self):
        my_test_suit = unittest.TestSuite()
        my_test_suit.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SauceDemoTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(SeleniumEasyTest)
        ])

        my_test_runnner = HTMLTestRunner(
            output = "report",
            title = "Test report",
            report_name = "report",
            tested_by = "Lazarica Petrut"
        )

        my_test_runnner.run(my_test_suit)