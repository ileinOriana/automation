from selenium import webdriver 
import unittest
import time 

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver')
driver.get('http://automationpractice.com/index.php')

search_box = driver.find_element_by_id('search_query_top')
search_box.send_keys('hola')
search_box_button = driver.find_element_by_name('submit_search')
search_box_button.click()
time.sleep(5)

results_label = driver.find_element_by_xpath('//*[@id="center_column"]/p')
tc.assertEqual('No results were found for your search "hola"', results_label.text)
women_link = driver.find_element_by_link_text('Women') 
women_link.click()
time.sleep(3)
dress_link = driver.find_element_by_partial_link_text('res')
dress_link.click()

driver.find_element_by_class_name('subcategory-name').click()

driver.close()
driver.quit() 
