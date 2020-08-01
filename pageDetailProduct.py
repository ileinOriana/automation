from selenium.webdriver.common.by import By

class PageDetailProduct():

    def __init__(self, driver):
        self.quantity_input = 'quantity_wanted'
        self.add_quantity_button = 'icon-plus'
        self.driver = driver
    
    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity_input).clear()
        self.driver.find_element_by_id(self.quantity_input).send_keys(quantity)
        
    def add_items(self, items):
        for i in range(items):
            self.driver.find_element_by_class_name(self.add_quantity_button).click()

    def get_number_of_elements(self):
        return self.driver.find_element_by_id(self.quantity_input).get_attribute('value')

    
