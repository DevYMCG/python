from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):
    
    # constructor
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'
    
    # Verificar que el sitio web a cargado correctamente
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True
    
    # Termino de busquedad.
    @property
    def Keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')
    
    # Ingresar a la url
    def open(self):
        self._driver.get(self._url)
    
    def type_search(self, keyword):
        # ubicar la barra de busqueda
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)
    
    # Metodo para enviar el termino de busqueda
    def click_submit(self):
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()
    
    # Realizar busqueda
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()