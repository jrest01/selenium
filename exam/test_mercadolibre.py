import unittest
from selenium import webdriver
from mercadolibre import MercadoLibre
import time

class MercadoLibreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        """
            Inicialize the project with the webdriver
        """
        cls.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')

    def test_mercadolibre(self):
        mercadolibre = MercadoLibre(self.driver)
        mercadolibre.open()
        mercadolibre.select_country()
        mercadolibre.search('Playstation')

        mercadolibre.condition_filter()
        mercadolibre.location_filter()

        mercadolibre.pricing_order()
        # mercadolibre.select_first_five()
        mercadolibre.first_five_names_prices()
        # time.sleep(5)


    # @classmethod
    # def tearDownClass(cls):
    #     """
    #         Driver exit
    #     """
    #     cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)