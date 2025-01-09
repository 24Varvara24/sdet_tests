from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.load_delays_link = (By.LINK_TEXT, 'Load Delay')

    @allure.step('клик по ссылке "Load Delay"')
    def click_load_delays_link(self) -> None:
        self.click(self.load_delays_link)
