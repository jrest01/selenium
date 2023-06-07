import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_account_link(self):
        driver = self.driver
        #Wait 10 seconds to compares if the length of the finded element == 3
        WebDriverWait(driver, 10).until(lambda s: s.find_element(By.ID,'select-language').get_attribute('length') == '3')

        #Wait 10 seconds to achieve the EC
        account = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):
        driver = self.driver
        #Clicks the link test ACCOUNT
        driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()

        #Wait 10 seconds to achieve the EC
        my_account = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()
        
        #Wait 20 seconds to achieve the EC. Then click
        create_account_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()
        
        #Wait 10 seconds to achieve the EC
        WebDriverWait(driver, 10).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        """
            Driver exit
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)