def test_correct_product_name(product_page):
    product_page.check_product_name_on_page("Office Design Software")


def test_add_product_to_cart(product_page):
    product_page.check_add_to_cart()


def test_search_input_highlight(product_page):
    product_page.check_search_input_highlight()
