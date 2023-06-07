import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class LanguageOptions(unittest.TestCase):

    def setUp(self):
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(14)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
    
        #Lists to store the language options
        exposed_options = ['English', 'French', 'German']
        active_options = []

        #Stores the select list 
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        #Assert de lenght of the options
        self.assertEqual(3, len(select_language.options))

        #Fill the list with the founded options
        for option in select_language.options:
            active_options.append(option.text)

        #Compares the lists of options
        self.assertListEqual(exposed_options, active_options)

        #Checks if the first option of the select is English
        self.assertEqual('English', select_language.first_selected_option.text)

        #Selects the options by the visible text
        select_language.select_by_visible_text('German')                      

        #Checks if the language was changed
        self.assertTrue('store=german' in self.driver.current_url)

        #Changes the language again
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        """
            Driver exit
        """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)