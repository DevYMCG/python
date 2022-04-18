import unittest
from selenium import webdriver
# Importando la clase 
from google_page import GooglePage

class GoogleTest(unittest.TestCase):
    
    """
        @classmethod decorador que permite que solo exista
        una instancia en el navegador
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= '../driver/chromedriver.exe')
    
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.Keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)