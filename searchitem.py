import unittest
from selenium import webdriver
import time

class SearchCases(unittest.TestCase):

    def test_search_no_elements(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('http://automationpractice.com/index.php')

        driver.find_element_by_id('search_query_top').send_keys('hola')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        result = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        #Text sirve para buscar la propiedad 'text' del web element
        expected_result = 'No results were found for your search "hola"'
        
        self.assertEqual(result, expected_result)

        driver.close()
        driver.quit()


    def test_search_find_dresses(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('dress')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        result = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text
        expected_result = 'DRESS'

        self.assertTrue(expected_result in result)
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main()