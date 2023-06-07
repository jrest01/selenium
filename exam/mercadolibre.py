from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MercadoLibre(object):
    """
            defines the url and the name of the locator
    """
    def __init__(self, driver) :
        self._driver = driver
        self._url = 'https://www.mercadolibre.com'
        self._driver.maximize_window()

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(By.CLASS_NAME,'nav-search-input'))

    @property
    def keyword(self):
        keyword = self._driver.find_element(By.CLASS_NAME, 'nav-search-input')
        return keyword.get_attribute('value')

    def open(self):
        """
            open the url
        """
        self._driver.get(self._url)

    def select_country(self, country = 'Colombia'):
        select_country = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, country)))
        select_country.click()

    def type_search(self, keyword):
        """
            writes in the search field
        """
        search_field = self._driver.find_element(By.CLASS_NAME, 'nav-search-input')
        search_field.clear()
        search_field.send_keys(keyword)

    def click_submit(self):
        """
            submits the search
        """
        search_field = self._driver.find_element(By.CLASS_NAME, 'nav-search-input')
        search_field.submit()

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()

    def condition_filter(self, condition = 'nuevo'):
        condition = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root-app"]/div/div[2]/aside/section/div[7]/ul/li[1]/a/span[1]')))
        self._driver.execute_script("arguments[0].click();", condition)


    def location_filter(self, location = 'Antioquia'):
        location_button = WebDriverWait(self._driver,5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, location)))
        self._driver.execute_script("arguments[0].click();", location_button)



    def pricing_order(self, option = 'Mayor precio'):
        order = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[2]/div[2]/div/div/div[2]/div/div/button')
        order.click()
        select_option = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_desc"]/div/div/span')))
        self._driver.execute_script("arguments[0].click();", select_option)


    def select_first_five(self):
        first_five = []

        for i in range(0,5):
            y = WebDriverWait(self._driver,10).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a')))
            first_five.append(y)

        x = first_five[2]
        self._driver.execute_script("arguments[0].click();", x)

    def first_five_names_prices(self):
        products = {}

        for i in range(0,5):
            item_name = self._driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]')
            item_price = self._driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            products[item_name.text] = item_price.text
            
        # print(products)
        print()
        
        for k, v in products.items():
            print(k,v)
