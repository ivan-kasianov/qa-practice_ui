import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.desks_page import DesksPage
from pages.product_page import ProductPage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(1920, 1080)
    return chrome_driver


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def desks_page(driver):
    return DesksPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)
