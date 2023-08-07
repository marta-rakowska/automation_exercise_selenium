from pages.base_page import BasePage

class HomePage(BasePage):
    signup_login_button_xpath = "//*[text()=' Signup / Login']"

    home_page_url = "https://www.automationexercise.com/"
    expected_title = "Automation Exercise"
    def title_of_page(self):
        assert self.get_page_title(self.home_page_url) == self.expected_title

    def click_signup_login_button(self):
        self.wait_for_element_to_be_clickable(self.signup_login_button_xpath)
        self.click_on_the_element(self.signup_login_button_xpath)

    