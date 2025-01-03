from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class DynamicTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # значение CPU из таблицы,локатор по  XPATH
        self.cpu_from_table = (
            By.XPATH, "//*[text()='Chrome']/../*[@role='cell']/../*[contains(text(),'%')]")

        self.url = 'http://uitestingplayground.com/dynamictable'

    @allure.step('Перейти на страницу c таблицей')
    def move_to_dynamictable(self):
        self.move_url(self.url)

    # строка Chrome CPU, локатор по названию класса
    cpu_from_yellow_line = (By.CLASS_NAME, 'bg-warning')

    @allure.step('Получить значение CPU из таблицы')
    def get_cpu_from_yellow_line(self) -> str:
        return self.get_text(self.cpu_from_yellow_line).replace('Chrome CPU:', '').strip()

    @allure.step('Получить значение CPU из желтой линии')
    def get_cpu_from_table(self) -> str:
        return self.get_text(self.cpu_from_table)
