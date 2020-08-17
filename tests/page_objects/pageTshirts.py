class PageTshirts():
    def __init__(self, driver):
        self.orange_button = 'color_1'
        self.driver = driver

    def click_orange_button(self):
        self.driver.find_element_by_id(self.orange_button).click()
        self.driver.find_element_by_id(self.orange_button).click()