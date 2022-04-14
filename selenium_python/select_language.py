from select import select
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    def test_select_language(self):
        # crear lista incluyendo los idiomas
        exp_options = ['English', 'French', 'German']
        # lista vacia para almacenar opciones seleccionadas
        act_options = []

        # Indicamos donde se encuentra el id del idioma
        select_language = Select(self.driver.find_element_by_id('select-language'))

        # validar que la lista de opciones tenga 3 
        self.assertEqual(3, len(select_language.options))

        # iterar por opciones cada una de las que tiene el drowndown
        for option in select_language.options:
            # agregamos a la lista el texto
            act_options.append(option.text)

        # verificar que las listas sean identicas
        self.assertListEqual(exp_options, act_options)

        # seleccionar un idioma de los que estan disponibles, verificar que sea la palabra ingles la primera opcion
        self.assertEqual('English', select_language.first_selected_option.text)

        # seleccionar el idioma aleman
        select_language.select_by_visible_text('German')

        # verificar que realmente este en aleman (cambia en la url con esto lo comparamos)
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id('select-language'))
        # seleccionamos  ingles para que quede como valor por defecto 
        select_language.select_by_index(0)
            

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)