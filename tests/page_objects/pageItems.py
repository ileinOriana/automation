from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems():
    def __init__(self, driver):
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.order = (By.ID, 'selectProductSort')
        self.checkbox = (By.CLASS_NAME, 'checkbox')
        self.color_check = (By.CLASS_NAME, 'color-option  ')
        self.driver = driver

    
    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.title_banner)
    
    def select_by_text(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(text)
    
    def select_by_value(self, value):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_value(value)
    
    def select_by_index(self, index):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_index(index)
    
    def click_checkbox(self, number): 
        self.driver.find_elements(*self.checkbox)[number].click()
    
    def click_colors(self, number):
        self.driver.find_elements(*self.color_check)[number].click()

    
   
