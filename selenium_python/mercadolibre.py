from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingMercadoLibre(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.mercadolibre.com/")
    
    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        #inspeccionar barra de busqueda
        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        #enviar termino de busqueda
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        #aplicar filtro de ubicación, con el texto parcial del enlace
        location=driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/div[3]/div[6]/ul/li[1]/form/button/span[1]')
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        #aplicar filtro por condición 
        condition = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/div[3]/div[2]/ul/li[1]/form/button/span[1]')
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        #ordenar
        order_menu = driver.find_element_by_css_selector('#root-app > div > div > aside > div.ui-search-filter-groups > div:nth-child(4) > ul > li:nth-child(1) > form > button > span.ui-search-filter-name');
        driver.execute_script("arguments[0].click();", order_menu)
        sleep(3)
        
        #identificar el item de mayor precio
        higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > a:nth-child(3) > div.andes-list__item-first-column > div.andes-list__item-text > div')
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)

        #obtener el texto que se ubica en el articulo y la cantidad del precio
        articles = []
        prices = []

        #forma de iterar en los textos es a traves del xpath ya que nos da el numero del item en la lista
        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            # article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{ i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/span/div[2]/div/span/span[1]').text
            # prices.append(article_price)
        
        print(articles)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)