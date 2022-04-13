import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    """
        Identificar que el campo de busqueda esta presente
    """
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    
    """
        Identificar si el id del lenguaje esta presente
    """
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()
    
    """
        Función que permite saber cuando un elemento esta presente 
        de acuerdo a sus parametros
    """
    def is_element_present(self, how, what):
        # how tipo de selector
        # what valor que tiene
        try:
            self.driver.find_element(by = how , value= what)
        except NoSuchElementException as variable:
            return False

        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)