from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class ProgressbarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # строка с редультатами,локатор по id
        self.result = (By.ID, 'result')
        # кнопка Start,локатор по id
        self.start_btn = (By.ID, 'startButton')
        # кнопка Stop,локатор по id
        self.stop_btn = (By.ID, 'stopButton')
        # Прогрессбар,локатор по css селектору
        self.progressbar = (By.CSS_SELECTOR, "[role='progressbar']")

        self.url = 'http://uitestingplayground.com/progressbar'

    @allure.step('Перейти на страницу прогрессбара')
    def move_to_progressbar(self):
        self.move_url(self.url)

    @allure.step('Клик по кнопке Start')
    def click_start_btn(self) -> None:
        self.click(self.start_btn)

    @allure.step('Клик по кнопке Stop')
    def click_stop_btn(self) -> None:
        self.click(self.stop_btn)

    @allure.step('Получение Result')
    def get_result(self) -> str:
        record = self.get_text(self.result).split(',')
        return record[0][-2:]

    @allure.step('Получение Duration')
    def get_duration(self) -> str:
        record = self.get_text(self.result).split(',')
        return record[1][-5:]

    @allure.step('Получение значения прогресса')
    def get_progress(self) -> str:
        return self.get_text(self.progressbar)
