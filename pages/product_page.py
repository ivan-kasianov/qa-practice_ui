from pages.base_page import BasePage
from pages.locators import product_locators as PL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"

    def check_product_name_on_page(self, text):
        self.open_page()
        product = self.find(PL.product_name_loc)
        assert product.text == text

    def check_add_to_cart(self):
        self.open_page()
        add_to_cart_button = self.find(PL.add_to_cart_button_loc)
        add_to_cart_button.click()
        cart_quantity = self.find(PL.cart_quantity_loc)
        wait_second = WebDriverWait(self.driver, 5)
        wait_second.until(
            EC.text_to_be_present_in_element(
                PL.cart_quantity_loc, "1"
            ))
        assert cart_quantity.text == "1"

    def check_search_input_highlight(self):
        self.open_page()
        search_input = self.find(PL.search_input_loc)
        color_before = search_input.value_of_css_property("box-shadow")
        search_input.click()
        color_after = search_input.value_of_css_property("box-shadow")
        assert color_after != color_before
