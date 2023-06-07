import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AddRemove(unittest.TestCase):

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

    def test_add_remove_items(self):
        #Reads the args 
        elements_to_add = int(input('Elements to Add '))
        elements_to_del = int(input('Elements to Delete '))
        final_elements = elements_to_add - elements_to_del

        #Finds the button to add and valdiate it
        button_add = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        self.assertTrue(button_add.is_displayed and button_add.is_enabled)

        #Clicks the button to add element 'elements_to_add' times
        for i in range(elements_to_add):
            button_add.click()
        time.sleep(3)

        """
        #Checks the amount of items that can be delete to delete all
        elements_to_del = self.driver.find_elements(By.CLASS_NAME, 'added-manually')
        self.assertTrue(len(elements_to_del) == 3)
        """

        #Clicks the button to delete element 'elements_to_del' times validating that 'elements_to_del' <= 'elements_to_add'
        for i in range(elements_to_del):
            try:
                button_del = self.driver.find_element(By.CLASS_NAME, 'added-manually')
                button_del.click()
            except:
                print('Tryin to delete more elements than the exitent')
                break
        time.sleep(3)

        if final_elements > 0:
            print(f'There are {final_elements} elements')
        else:
            print(f'There are 0 elements')

        time.sleep(10)
    
    def tearDown(self):
        """
            Driver exit
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)