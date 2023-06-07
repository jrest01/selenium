from unittest import TestLoader, TestSuite
# from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchs_tests import SearchsTests
from HtmlTestRunner import HTMLTestRunner

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_tests = TestLoader().loadTestsFromTestCase(SearchsTests)

#Build the suite test
smoke_test = TestSuite([assertions_test, search_tests])


# Kwargs to generate the reports
kwargs = {
    "output": "reports/reportes/",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": True
    }


runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test) 
