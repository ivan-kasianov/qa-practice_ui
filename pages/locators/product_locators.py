from selenium.webdriver.common.by import By

product_name_loc = (By.TAG_NAME, "h1")
add_to_cart_button_loc = (By.ID, "add_to_cart")
cart_quantity_loc = (By.CSS_SELECTOR, ".my_cart_quantity")
search_input_loc = (By.CSS_SELECTOR, '[data-search-type="products"]')
