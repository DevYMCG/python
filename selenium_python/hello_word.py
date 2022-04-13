from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

"""
    Proceso
    selenium abre una ventana del navegador el cual
    va a https://www.platzi.com y despues de ello la
    cierra.
"""

class HelloWord(unittest.TestCase):

    """
        @Ejecuta todo lo necesario antes de hacer una
        prueba es decir prepara el entorno de la prueba

        @classmethod # Decorador para que las distintas
        paginas corran en una sola pestaña

    """
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    """
        @caso de prueba, se van a ejecutar una serie de
        acciones para que el navegador los realice
    """
    
    def test_hello_word(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    """
        Luego de abrir platzi espera 10seg y abre 
        la pagina de wikipedia en una ventana diferente
    """
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    """
        @Acciones para finalizar la prueba generalmente lo
        mas recomensable es cerrar la ventana del navegador
    """
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='hello-word-report'))