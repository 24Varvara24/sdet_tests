from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class NonBreakingSpacePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # button=(By.XPATH,"//button[text()[contains(.,'My')] and text()[contains(.,'Button')]]")
        self.button = (By.XPATH, "//button[text()='My\u00A0Button']")

        self.url = 'http://uitestingplayground.com/nbsp'

    @allure.step('Перейти на страницу c Non-Breaking Space')
    def move_to_nbsp(self):
        self.move_url(self.url)

    @allure.step('Проверка отображения кнопки')
    def btn_is_display(self) -> None:
        self.elem_is_display(self.button)
