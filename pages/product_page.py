from pages.base_page import BasePage
from pages.locators import product_locators as PL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data import expected_color_input_border as border_color


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"

    def check_product_name_on_page(self, text):
        self.verify_element_text(PL.product_name_loc, text)

    def check_add_to_cart(self):
        cart_quantity = self.find(PL.cart_quantity_loc)
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.text_to_be_present_in_element(
                PL.cart_quantity_loc, "1"
            ))
        assert cart_quantity.text == "1"

    def add_product_to_cart(self):
        add_to_cart_button = self.find(PL.add_to_cart_button_loc)
        add_to_cart_button.click()

    def click_input(self):
        search_input = self.find(PL.search_input_loc)
        search_input.click()

    def get_border_color(self):
        search_input = self.find(PL.search_input_loc)
        return search_input.value_of_css_property("box-shadow")

    def check_search_input_highlight(self):
        search_input = self.find(PL.search_input_loc)
        wait = WebDriverWait(self.driver, 3)
        wait.until(
            lambda driver:
            search_input.value_of_css_property("box-shadow") == border_color
        )
        actual_color = search_input.value_of_css_property("box-shadow")
        assert actual_color == border_color
