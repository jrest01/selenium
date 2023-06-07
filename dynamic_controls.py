import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DynamicControls(unittest.TestCase):

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/dynamic_controls')


    def enable_disable_button(self):
        """
            Searchs and waits for the button to click it
        """
        enable_disable_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))        
        enable_disable_button.click()
        
    def add_remove_button(self):
        """
            Searchs and waits for the button to click it
        """
        add_remove_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
        add_remove_button.click()

    def test_dynamic_controls(self):
        driver = self.driver
        
        #Enable the button, types at the button then disable and enable it
        self.enable_disable_button()
        text = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text.send_keys('Platzi.com')
        self.enable_disable_button()
        self.enable_disable_button()

        #Finds and clicks the checkbox
        check = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        check.click()
        
        #Removes and add the button
        self.add_remove_button()
        self.add_remove_button()
        self.add_remove_button()
        

    def tearDown(self):
        """
            Driver exit
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)