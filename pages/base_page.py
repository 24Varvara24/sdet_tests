import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import List


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = 'http://uitestingplayground.com/'

    def find_element(self, by: By or str, value: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or str, value: str) -> List[WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    @allure.step('Переход по юрлу')
    def move_url(self,url:str) -> str:
        self.driver.get(url)



    def get_text(self, element: tuple) -> str:
        return self.find_element(*element).text

    def click(self, element: tuple) -> None:
        self.find_element(*element).click()

    @allure.step('Ввод данных')
    def input(self, element: tuple, input_data: str) -> None:
        self.find_element(*element).send_keys(input_data)

    @allure.step('Проверка отображения элемента')
    def elem_is_display(self, element: tuple) -> None:
        assert self.find_element(*element).is_displayed(), ('[FAILED]:элемент не отображается ')


