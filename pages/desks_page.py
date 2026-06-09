from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import desks_locator as DL
from utils import test_data as TL


class DesksPage(BasePage):
    page_url = "/shop/category/desks-1"

    def check_desks_on_page(self):
        desks = self.find_all(DL.desks_loc)
        assert len(desks) > 0

    def find_desks_titles(self):
        desks = self.find_all(DL.desks_titles_loc)
        desks_text = []
        for desk in desks:
            desks_text.append(desk.text)
        return desks_text

    def sorted_desk_titles(self, titles):
        titles = sorted(titles)
        return titles

    def check_all_titles(self):
        actual_titles = self.find_desks_titles()
        assert actual_titles == TL.desk_titles

    def select_sort_option(self):
        titles = self.find_desks_titles()
        titles_sort_without_click_button = self.sorted_desk_titles(titles)
        dropdown_button = self.find(DL.dropdown_button_loc)
        dropdown_button.click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(
            EC.visibility_of_all_elements_located(DL.dropdown_menu_loc))
        button_sort_list = self.find_all(DL.dropdown_button_list_loc)
        button_sort_list[8].click()
        wait_second = WebDriverWait(self.driver, 5)
        wait_second.until(
            EC.text_to_be_present_in_element(
                DL.dropdown_button_loc, "Name (A-Z)")
        )
        titles_sort_after_click_button = (
            self.find_desks_titles()
        )
        assert (
            titles_sort_without_click_button == titles_sort_after_click_button
        )
