import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicElemets(unittest.TestCase):

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/disappearing_elements')

    def test_name_elements(self):
        #defines gallery as a list
        gallery = []
        tries = 1

        while len(gallery) == 0:
            #Will try find the 'gallery' button until achieve it
            gallery = self.driver.find_elements(By.LINK_TEXT, 'Gallery')
            if len(gallery) == 0:
                time.sleep(3)
                print('Not Found')
                self.driver.refresh()
                tries += 1

        print(f'it took {tries} tries')

    def tearDown(self):
        """
            Driver exit
        """
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)