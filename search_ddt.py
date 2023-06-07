import unittest, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack

def ged_data(file_name):
    """
        Reads a CSV and fill 'rows' with the data excepting the header
    """
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    
    return rows

#Metodología para automatizaciones para desarrollar pruebas para código existente y validar escenarios favorables y no favorables
@ddt
class SearchDdt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        cls.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = cls.driver
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(*ged_data('testdata.csv'))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        #Find the search field and search each value defined at @data
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #Store the products finded
        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')
        
        expected_count = int(expected_count)

        #Assert the found products and the 'expected_count'
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(By.CLASS_NAME, 'note-msg')
            self.assertEqual(message.text, 'Your search returns no results.')

        print(f'Found {len(products)} products')

    @classmethod
    def tearDownClass(cls) :
        """
            Driver exit
        """
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)