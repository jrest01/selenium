import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        """
            Inicialize the project with the webdriver
        """
        cls.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')

    def test_search(self):
        """
            instance the GooglePage object and search 'platzi'
        """
        google = GooglePage (self.driver)
        google.open()
        google.search('Platzi')

        """
            compares 'platzi' with the property keyword
        """
        self.assertEquals('Platzi', google.keyword)

    def test_search2(self):
        googlee = GooglePage (self.driver)
        googlee.open()
        googlee.search('millonarios vs')

        self.assertEquals('millonarios vs', googlee.keyword)

    @classmethod
    def tearDownClass(cls) :
        """
            Driver exit
        """
        cls.driver.close()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)