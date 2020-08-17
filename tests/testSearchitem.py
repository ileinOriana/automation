import unittest
from selenium import webdriver
import time

from page_objects.pageIndex import PageIndex
from page_objects.pageItems import PageItems
from page_objects.pageTshirts import PageTshirts
from page_objects.pageDetailProduct import PageDetailProduct
from selenium.webdriver.chrome.options import Options

class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("--start-fullscreen")
        option.add_argument("incognito")
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome('chromedriver', options = option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        #self.driver.maximize_window()
        #self.driver.set_window_size(200, 240) Esto es para setear el tamanio del navegador
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.tshirtsPage = PageTshirts(self.driver)
        self.DetailProductPage = PageDetailProduct(self.driver)

    @unittest.skip(' Not needed now')
    def test_search_no_elements(self):
        try:
            self.indexPage.search('hola')
            self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')
        except:
            self.driver.save_screenshot('hola_bug.jpg')
        
    @unittest.skip(' Not needed now')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())
        

    
    def test_tarea(self):
        self.indexPage.search_tshirts()
        self.tshirtsPage.click_orange_button()
        self.DetailProductPage.enter_quantity('25')
        self.DetailProductPage.add_items(3)
        number = self.DetailProductPage.get_number_of_elements()
        self.assertTrue(number == '28')
        self.driver.save_screenshot('no_element.png')
    
    @unittest.skip(' Not needed now')
    def test_selections(self):
        self.indexPage.search_tshirts()
        self.itemsPage.select_by_text('Product Name: A to Z')
        time.sleep(3)
        self.itemsPage.select_by_value('reference:asc')
        time.sleep(2)
        self.itemsPage.select_by_index(3)
        time.sleep(3)

    @unittest.skip(' Not needed now')
    def test_dresses_options(self):
        self.indexPage.click_dresses()
        self.itemsPage.click_checkbox(2)
        self.itemsPage.click_checkbox(4)
        self.itemsPage.click_colors(2)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()