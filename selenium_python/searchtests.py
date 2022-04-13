from itertools import product
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    """
        buscar en nuestro eccomers de prueba una
        camisa
    """
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # limpiar campo de busqueda
        search_field.clear()

        # simulacion de buqueda en la barra de busqueda
        search_field.send_keys('tee')
        search_field.submit()
    

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        """
            listar los productos si buscamos aparece solamente
            uno
        """
        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)