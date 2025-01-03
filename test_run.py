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
        '''Включаем(нажимаем Start) прогрессбар,ждем пока прогресс не дойдет до 75%,
        выключаем(нажимаем Stop) его и после этого проверяем,
        что значение Result < 5, Duration < 17000''')
    def test_progressbar(self, driver) -> None:
        progressbar_page = ProgressbarPage(driver)
        with allure.step('Перейти по ссылке Progress Bar'):
            progressbar_page.move_to_progressbar()


        with allure.step('Нажать на кнопку старт'):
            progressbar_page.click_start_btn()

        with allure.step('ждем пока  прогресс не станет равен 75% '):
            while progressbar_page.get_progress() < '75%':
                progressbar_page.get_progress()

        with allure.step('нажимаем кнопку Stop'):
            progressbar_page.click_stop_btn()

        with allure.step('получаем Result и проверяем меньше ли оно 5 '):
            assert progressbar_page.get_result() < "5", ('[FAILED]:Result >= 5 ')

        with allure.step('получаем Duration'):
            assert progressbar_page.get_duration() < '17500', ('[FAILED]:Duration >= 17000 ')

    @allure.title('Тест 2: отображение кнопки на странице Load Delay')
    @allure.description(
        ''' ждем, пока загрузится страница Load Delay и отобразится кнопка,
        проверить, что кнопка Button Appearing After Delay отображается''')
    def test_load_delays(self, driver) -> None:
        start_page = StartPage(driver)
        with allure.step('Перейти по ссылке Progress Bar'):
            start_page.click_load_delays_link()

        delays_pages = LoadDelayPage(driver)
        with allure.step('Проверить как отображается кнопка Button Appearing After Delay'):
            delays_pages.btn_primary_is_display()


    @allure.title('Тест 3: изменение названия кнопки (и проверка самого изменения)')
    @allure.description(
        ''' вводим новое название кнопки в поле ввода,
        нажимаем на саму кнопку,и проверяем,
        изменилось ли ее название(сравниваем со старым) ''')
    def test_text_input(self, driver) -> None:
        text_input_page = TextInputPage(driver)
        with allure.step('Перейти по ссылке Text Input'):
            text_input_page.move_to_textinput()



        with allure.step('Получение старого имени кнопки'):
            old_btn_name = text_input_page.get_btn_name()

        with allure.step('Ввод нового названия кнопки'):
            text_input_page.input_new_name_btn()

        with allure.step('Клик по кнопке для изменения ее названия'):
            text_input_page.click_btn()

        with allure.step('Сравнение старого названия и нового'):
            text_input_page.compare_btn_names(old_btn_name, text_input_page.get_btn_name())

    @allure.title('Тест 4: сравнить значение Chrome CPU из таблицы и  со значением Chrome CPU из желтой строки')
    @allure.description(
        ''' cчитываем значения Chrome CPU из таблицы и из желтой строки,затем сравнить их (в точности до символа)''')
    def test_dynamic_table(self, driver) -> None:
        dynamic_table = DynamicTablePage(driver)
        with allure.step('Перейти по ссылке Dynamic Table'):
            dynamic_table.move_to_dynamictable()

        with allure.step('Сравнение CPU из таблицы и строки'):
            assert dynamic_table.get_cpu_from_yellow_line() == dynamic_table.get_cpu_from_table(), (
                '[FAILED]: значение из таблицы не равно значению в выделенной желтым строке ')

    @allure.title('Тест 5: проверка отображения кнопки My Button ')
    @allure.description(
        ''' найти кнопку My Button и проверить ее отображение ''')
    def test_nbsp(self, driver) -> None:
        nbsp = NonBreakingSpacePage(driver)
        with allure.step('Перейти по ссылке Non-Breaking Space'):
            nbsp.move_to_nbsp()

        with allure.step('Проверить,отображается ли кнопка с надписью "My Button"'):
            nbsp.btn_is_display()
