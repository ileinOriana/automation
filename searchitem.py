import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageTshirts import PageTshirts
from pageDetailProduct import PageDetailProduct

class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.tshirtsPage = PageTshirts(self.driver)
        self.DetailProductPage = PageDetailProduct(self.driver)

    @unittest.skip(' Not needed now')
    def test_search_no_elements(self):
        self.indexPage.search('hola')
        time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')

    @unittest.skip(' Not needed now')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

      
    def test_tarea(self):
        self.indexPage.search_tshirts()
        self.tshirtsPage.click_orange_button()
        self.DetailProductPage.enter_quantity('25')
        self.DetailProductPage.add_items(3)
        number = self.DetailProductPage.get_number_of_elements()
        self.assertTrue(number == '28')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()