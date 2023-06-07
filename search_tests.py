import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    
    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path= r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(14)

    def test_search_text_field(self):
        """
            search text field by id
        """
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_by_name(self):
        """
            search text by name
        """
        search_field = self.driver.find_element_by_name('q')

    def test_search_field_by_class_name(self):
        """
            search field by class name
        """
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enable(self):
        """
            search button enable
        """
        button = self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self):
        """
            count promo banner images
        """
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        """
            search vip promo
        """
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def shopping_cart(self):
        """
            search shopping cart
        """
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')
    
    def tearDown(self):
        """
            Driver exit
        """
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes', report_name= 'ecommerce'))
