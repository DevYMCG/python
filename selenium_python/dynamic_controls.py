import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # Esperas explicitas
from selenium import webdriver

class DynamicControls(unittest.TestCase):
    
    def setUp(self):
        #prepara entorno de prueba
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Dynamic Controls').click()

    # casos de prueba
    def test_dynamic_controls(self):
        driver = self.driver
        #identificar elementos a través del selector
        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()

        #Identificamos el bottom para remover
        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()

        #  #Webdriver wait (driver, espera). hasta que (EC.el elemento sea clickable(tupla)) tupla (por selector CSS, "Selector")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkbox-example > button")))
        remove_add_button.click() 

        # boton de habilitar y deshabilitar el textArea para llegar el boton usamos el selector
        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')

        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))

        #identificar text area o textbox
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_disable_button.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)