from selenium.webdriver.common.action_chains import ActionChains
from pages.locators import cart_locators as cart_loc
from pages.base_page import BasePage
from utils.test_data import expected_color_login_button as button_color


class CartPage(BasePage):
    page_url = "/shop/cart"

    def check_cart_empty_text(self, text):
        self.verify_element_text(cart_loc.banner_loc, text)

    def check_phone_number_is_correct(self, text):
        self.verify_element_text(cart_loc.phone_number_loc, text)

    def get_button_color(self):
        search_button = self.find(cart_loc.button_login)
        return search_button.value_of_css_property("background-color")

    def hover_to_button(self):
        button_login = self.find(cart_loc.button_login)
        actions = ActionChains(self.driver)
        actions.move_to_element(button_login).perform()

    def check_button_color_is_correct(self, actual_color):
        assert button_color == actual_color
