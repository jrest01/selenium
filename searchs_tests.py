import unittest
# from pyunitreport import HTMLTestRunner
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

class SearchsTests(unittest.TestCase):
     

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(14)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        """
            Search an element named 'q'.
            .clear() clears the text area content
            .send_keys() writes to an element
            .submit() send a form or confirmation (enter)
        """
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        """
            Search an element named 'q'.
            .send_keys() writes to an element
            .submit() send a form or confirmation (enter)
        """
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(len(products), 1)


    def tearDown(self):
        """
            Driver exit
        """
        self.driver.quit()