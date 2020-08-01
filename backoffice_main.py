from selenium import webdriver
import time
import unittest
from BpageLogin import LoginPage
from selenium.webdriver.chrome.options import Options

class LoginTest(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("--start-fullscreen")
        option.add_argument("incognito")
        self.driver = webdriver.Chrome('chromedriver', chrome_options = option)
        self.driver.get('https://payments-wallet-int.fif.tech/backoffice/web/login')
        self.driver.implicitly_wait(5)
        self.loginPage = LoginPage(self.driver)
    
    def test_successful_login(self):
        self.loginPage.send_email('backoffice_int@int.com')
        self.loginPage.send_password('000111')
        self.loginPage.click_submit_button()
        self.loginPage.return_default_login_view()
        

    def test_invalid_login(self):
        self.loginPage.send_email('backoffice_int@int.com')
        self.loginPage.send_password('000112')
        self.loginPage.click_submit_button()
        self.assertEqual(self.loginPage.return_invalid_credentials(), 'El email o la contraseña son incorrectos')




    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()