from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class LoadDelayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

    # кнопка Button Appearing After Delay
    btn_primary = (By.CSS_SELECTOR, '[type="button"]')

    @allure.step('проверка отображения кнопки Button Appearing After Delay')
    def btn_primary_is_display(self):
        self.elem_is_display(self.btn_primary)
