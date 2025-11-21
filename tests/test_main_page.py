from urls import Urls
from pages.main_page import MainPage
import pytest
import allure

class TestConstructPage():

    @allure.title("Проверка перехода в раздел 'Свяжитесь с нами', по нажатию на кнопку Оставить заявку")
    def test_click_button_submit_application(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.click_button_submit_application()
        main_page.wait_for_contact_us()
        assert main_page.is_contact_us_visible()

    @allure.title("Проверка перехода в раздел 'Форма сотрудничества', по нажатию на кнопку Узнать больше")
    def test_click_button_learn_more(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.click_button_learn_more()
        main_page.wait_for_employee_form()
        assert main_page.is_employee_form_visible()

    @allure.title("Проверка перехода на сайт AI Hunt по нажатию на кнопку 'Актуальные вакансии'")
    def test_click_button_current_vacancies(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.click_button_current_vacancies()
        main_page.switch_to_new_tab()
        main_page.wait_url(Urls.AI_HUNT)
        assert main_page.current_url() == Urls.AI_HUNT