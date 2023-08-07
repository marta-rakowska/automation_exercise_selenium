from pages.base_page import BasePage
class LoginPage(BasePage):
    new_user_signup_xpath = "//*[text()='New User Signup!']"
    name_field_xpath = "//*[@name='name']"
    email_field_xpath = "//*/div[3]/div/form/input[3]"
    signup_button_xpath = "//*[text()='Signup']"

    def type_in_name(self, name):
        self.wait_for_element_to_be_visible(self.new_user_signup_xpath)
        self.field_send_keys(self.name_field_xpath, name)
    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def click_signup_button(self):
        self.click_on_the_element(self.signup_button_xpath)