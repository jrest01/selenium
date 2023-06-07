from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):
    """
            defines the url and the name of the locator
    """
    def __init__(self, driver) :
        self._driver = driver
        self._url = 'https://www.google.com/'
        self.search_locator = 'q'

    @property
    def is_loaded(self):
        """
            property is_loaded
        """
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(By.NAME,'q'))
        return True
    
    @property
    def keyword(self):
        """
            property keyword = text in the search field
        """
        input_field = self._driver.find_element(By.NAME, 'q')
        return input_field.get_attribute('value')
    
    def open(self):
        """
            open the url
        """
        self._driver.get(self._url)

    def type_search(self, keyword):
        """
            writes in the search field
        """
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.send_keys(keyword)

    def click_submit(self):
        """
            submits the search
        """
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.submit()

    def search(self, keyword):
        """
             full search process
        """
        self.type_search(keyword)
        self.click_submit()