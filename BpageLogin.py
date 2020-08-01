class LoginPage():
    def __init__(self, driver):
        self.email_input = 'login_input_mail'
        self.password_input = 'login_input_password'
        self.submit_button = 'login_btn'
        self.invalid_credentials = 'login_input_password-helper-text'
        self.default_login_view = 'DASH_FPAY_VIEW'
        self.driver = driver

    def send_email(self, email):
        self.driver.find_element_by_id(self.email_input).send_keys(email)
    
    def send_password(self, password):
        self.driver.find_element_by_id(self.password_input).send_keys(password)
    
    def click_submit_button(self):
        self.driver.find_element_by_id(self.submit_button).click()
    
    def return_invalid_credentials(self):
        return self.driver.find_element_by_id(self.invalid_credentials).text
    
    def return_default_login_view(self):
        return self.driver.find_element_by_id(self.default_login_view)
