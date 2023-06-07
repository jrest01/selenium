import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Typos(unittest.TestCase):

    def setUp(self):
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/typos')
        driver.maximize_window

    def test_find_typo (self):
        driver = self.driver
        correct_text = "Sometimes you'll see a typo, other times you won't."
        #Find the paragraph
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text

        #Tries counter
        tries = 1

        while text_to_check != correct_text:
            tries += 1
            #Refresh the web page
            driver.refresh()
            #Find the paragraph
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            time.sleep(5)


        print(f'It tooks {tries} tries')



    def tearDown(self) :
        """
            Driver exit
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)