from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        # начальное значение кнопки
        self.btn_name = (By.ID, 'updatingButton')
        # инпут для ввода нового значения кнопки
        self.inp_for_new_name = (By.ID, 'newButtonName')

        self.url = 'http://uitestingplayground.com/textinput'

    @allure.step('Перейти на страницу c TextInput')
    def move_to_textinput(self):
        self.move_url(self.url)

    @allure.step('получить название кнопки')
    def get_btn_name(self):
        return self.get_text(self.btn_name)

    @allure.step('ввод данных в инпут')
    def input_new_name_btn(self) -> None:
        self.input(self.inp_for_new_name, 'new nameee')

    def click_btn(self) -> None:
        self.click(self.btn_name)

    @allure.step('Сравнение старого названия и нового названия кнопки')
    def compare_btn_names(self, old_mane, new_name) -> None:
        assert old_mane != new_name, ('[FAILED]:Название кнопки не поменялось!')
