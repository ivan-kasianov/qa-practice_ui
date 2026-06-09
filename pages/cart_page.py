from selenium.webdriver.common.action_chains import ActionChains
from pages.locators import cart_locators as cart_loc
from pages.base_page import BasePage


class CartPage(BasePage):
    page_url = "/shop/cart"

    def check_cart_empty_text(self, text):
        cart_empty_banner = self.find(cart_loc.banner_loc)
        assert cart_empty_banner.text == text

    def check_phone_number_is_correct(self, text):
        phone_number = self.find(cart_loc.phone_number_loc)
        assert phone_number.text == text

    def check_button_color_is_correct(self):
        button_login = self.find(cart_loc.button_login)
        color_button_before = (
            button_login.value_of_css_property("background-color")
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(button_login).perform()
        color_button_after = (
            button_login.value_of_css_property("background-color")
        )
        assert color_button_after != color_button_before
