import allure

from pages.start_page import StartPage
from pages.progressbar_page import ProgressbarPage
from pages.delays_pages import LoadDelayPage
from pages.textinput_page import TextInputPage
from pages.dynamictable_page import DynamicTablePage
from pages.nbsp_page import NonBreakingSpacePage


@allure.suite('Тесты лабы')
class Tests:
    @allure.title('Тест 1: прогрессбар на странице Progress Bar')
    @allure.description(
        '''
        Шаги теста:
        Перейти на страницу Progress Bar
        Нажать на кнопку старт
        ожидание, пока  прогресс не станет равен 75%
        нажать кнопку Stop
        проверить значение Result (должно быть меньше 5)
        проверить значение Duration (должно быть меньше 17 000)
        ''')
    def test_progressbar(self, driver) -> None:
        progressbar_page = ProgressbarPage(driver)

        progressbar_page.move_to_progressbar()
        progressbar_page.click_start_btn()

        progressbar_page.wait_for_progress('75')

        progressbar_page.click_stop_btn()

        progressbar_page.check_result_value('5')
        progressbar_page.check_duration_value('17000')

    @allure.title('Тест 2: отображение кнопки на странице Load Delay')
    @allure.description(
        '''
        Шаги теста:
        1)Перейти по ссылке Progress Bar из домашней старницы
        2)Проверить как отображается кнопка Button Appearing After Delay
        ''')
    def test_load_delays(self, driver) -> None:
        start_page = StartPage(driver)
        start_page.click_load_delays_link()

        delays_pages = LoadDelayPage(driver)
        delays_pages.btn_primary_is_display()

    @allure.title('Тест 3: изменение названия кнопки (и проверка самого изменения)')
    @allure.description(
        '''
        Шаги теста:
        1)Перейти на страницу Text Input
        2)Получение старого имени кнопки
        3)Ввод нового названия кнопки
        4)Клик по кнопке для изменения ее названия
        5)Сравнение старого названия и нового
        ''')
    def test_text_input(self, driver) -> None:
        text_input_page = TextInputPage(driver)

        text_input_page.move_to_textinput()
        old_btn_name = text_input_page.get_btn_name()
        text_input_page.input_new_name_btn()
        text_input_page.click_btn()
        text_input_page.compare_btn_names(old_btn_name, text_input_page.get_btn_name())

    @allure.title('Тест 4: сравнить значение Chrome CPU из таблицы и  со значением Chrome CPU из желтой строки')
    @allure.description(
        '''
        Шаги теста:
        1)Перейти на страницу Dynamic Table
        2)Cравнить CPU из таблицы и строки
        ''')
    def test_dynamic_table(self, driver) -> None:
        dynamic_table = DynamicTablePage(driver)
        dynamic_table.move_to_dynamictable()
        dynamic_table.compare_values_cpu()

    @allure.title('Тест 5: проверка отображения кнопки My Button ')
    @allure.description(
        ''' 
        Шаги теста:
        1)Перейти  на страницу 
        2)Проверить отображение кнопки с надписью "My Button"
        ''')
    def test_nbsp(self, driver) -> None:
        nbsp = NonBreakingSpacePage(driver)
        nbsp.move_to_nbsp()
        nbsp.btn_is_display()
