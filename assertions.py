import unittest
# from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTests(unittest.TestCase):
    """
        Assertion: Methods that allow check an expected value at the test execution. 
        If it's True the test continues. If it's False 'fail' and ends.
    """

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(14)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        """
            Use is_element_present to seacr name == 'q'
        """
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        """
            Use is_element_present to seacr id == 'select-language'
        """
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))        

    def tearDown(self):
        """
            Driver exit
        """
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


