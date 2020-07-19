from selenium import webdriver 
import unittest

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver')
driver.get('https://payments-wallet-int.fif.tech/merchant/web/login')

email_input = driver.find_element_by_id('email')
password_input = driver.find_element_by_id('password')

email_input.send_keys('todomodasa@gmail.com')
password_input.send_keys('112233')

