import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    """
        Run all tests cases
    """

    @classmethod
    #Decorator to prevent browser from closing
    def setUpClass(cls):
        """

        """
        cls.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(self):
        """
            Unit test
        """
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        """
            Unit test
        """     
        self.driver.get('https://www.wikipedia.org')
    
    def tearDown(cls):
        """
            Driver exit
        """
        cls.driver.quit()
        
    

if __name__ == '__main__':
    """
        Run al test cases and generate an html report
    """
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))

