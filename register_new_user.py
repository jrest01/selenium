import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

        

    def test_new_user(self):
        driver = self.driver
        #Press click at the with the xpath"..."(Account)
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        #Press click at the option 'Log In'
        driver.find_element_by_link_text('Log In').click()

        #find the button with the xpath("...")
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        
        #Asserts if the button is displayed and enabled and click it
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        #Asserts if the title of the page is the waited
        self.assertEqual('Create New Customer Account', driver.title)

        #Declares the form fields
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        #Asserts if the fields are enabled
        self.assertTrue(first_name.is_enabled() and
        middle_name.is_enabled() and
        last_name.is_enabled() and
        email_address.is_enabled() and
        news_letter_subscription.is_enabled() and
        password.is_enabled() and
        confirm_password.is_enabled() and
        submit_button.is_enabled() )

        #Fill the form fields with the values ("...") and press the submit button
        first_name.send_keys('test')
        middle_name.send_keys('test')
        last_name.send_keys('test')
        email_address.send_keys('test@mail.com')
        news_letter_subscription.send_keys('test')
        password.send_keys('test')
        confirm_password.send_keys('test')
        submit_button.click()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)