import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)


    def tearDown(self) :
        """
            Driver exit
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)