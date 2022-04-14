import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    def test_new_user(self):
        driver = self.driver
        # entramos a este elementos y le damos un clic para que se despliegue el menu de opciones
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        # le decimos al driver que encuentre el texto que esta en el menu de opciones llamado login y hacemos clic sobre el
        driver.find_element_by_link_text('Log In').click()

        #Esto nos llevara a la pantalla del login de la página, como no tenia mucha informacion lo obtendremos a traves de su XPath
        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a')
        # Revisamos si el botton esta habilitado
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        #verificamos si realmente nos encontramos en la pantalla de creación de cuenta, esto lo podremos lograr 
        # con el titulo de la pestaña.
        self.assertEqual('Create New Customer Account', driver.title)

        # identificar cada uno de los elementos del form para el registro
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        new_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled() 
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and new_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        # enviar datos para cada una de las nuevas variables
        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@testingmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)