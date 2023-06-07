import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tables(unittest.TestCase):

    def setUp(self) :
        """
            Inicialize the project with the webdriver, url and window settigns
        """
        self.driver = webdriver.Chrome(executable_path = r'D:\Platzi_Courses\Selenium\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/tables')
        driver.maximize_window()

    def test_tables(self):
        driver = self.driver
        #Defines 'table_data' as a nested list
        table_data = [[] for i in range(5)]
        
        for i in range(len(table_data)):
            #Fill 'table_data', each nested list saves a column from the table
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)
            for j in range(len(table_data)-1):
                field = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{1+i}]')
                table_data[i].append(field.text)


        for i in range(len(table_data)):
            #Prints 'table_data' 
            for j in range(len(table_data)):
                print(table_data[j][i].center(22), end="")
            print("")


    def tearDown(self) :
        """
            Driver exit
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)