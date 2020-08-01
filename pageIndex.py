from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex():
    def __init__(self, driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        #self.query_top = 'search_query_top'
        #self.query_button = 'submit_search'
        self.tshirts_button = '//*[@id="block_top_menu"]/ul/li[3]/a'
        self.dresses_link = (By.XPATH, '//*[@title= "Dresses"]')

        self.driver = driver

    def search(self, item):
        try:
            search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(self.query_button))
            search_button.click()
        except:
            print("No se encuentra el elemento")
        #self.driver.find_element_by_id(self.query_top).send_keys(item)
        #self.driver.find_element_by_name(self.query_button).click()
        #self.driver.find_element(*self.query_top).send_keys(item)
        #self.driver.find_element(*self.query_button).click()


    def search_tshirts(self):
        self.driver.find_element_by_xpath(self.tshirts_button).click()
    
    def click_dresses(self):
        self.driver.find_elements(*self.dresses_link)[1].click()