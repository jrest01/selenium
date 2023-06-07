import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class CompareProducts(unittest.TestCase):

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        #Locates de search module, cleans it and search 'tee'
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

        #Locates the compare button, validates if is enabled and displayed and click it
        compare_button = driver.find_element(By.CLASS_NAME, 'link-compare')
        self.assertTrue(compare_button.is_enabled and compare_button.is_displayed)
        compare_button.click()

        #Locates the clear button, validates if is enabled and displayed and click it
        clear_button = driver.find_element(By.LINK_TEXT, 'Clear All')
        self.assertTrue(clear_button.is_enabled and clear_button.is_displayed)
        clear_button.click()

        #Switchs to the alert, compares the text of the alert and click accept
        alert = driver.switch_to.alert 
        alert_text = alert.text
        self.assertEqual(alert_text, 'Are you sure you would like to remove all products from your comparison?')
        alert.accept()

    def tearDown(self) :
        """
            Driver exit
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)