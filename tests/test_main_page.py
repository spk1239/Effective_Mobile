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

    @allure.title("Проверка перехода в раздел 'О нас' по нажатию на соответствующую кнопку")
    def test_click_button_about_us(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_about_us_button()
        main_page.click_button_about_us()
        main_page.wait()
        assert "#about" in main_page.current_url()

    @allure.title("Проверка перехода в раздел 'Вакансии' по нажатию на соответствующую кнопку")
    def test_click_button_vacancy(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_vacancy_button()
        main_page.click_button_vacancy()
        main_page.wait()
        assert "#specializations" in main_page.current_url()

    @allure.title("Проверка перехода в раздел 'Отзывы' по нажатию на соответствующую кнопку")
    def test_click_button_reviews(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_reviews_button()
        main_page.click_button_reviews()
        main_page.wait()
        assert "#testimonials" in main_page.current_url()

    @allure.title("Проверка перехода в раздел 'Контакты' по нажатию на соответствующую кнопку")
    def test_click_button_contacts(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_contacts_button()
        main_page.click_button_contacts()
        main_page.wait()
        assert "#contact" in main_page.current_url()

    @allure.title("Проверка перехода в раздел 'Аутстафф' по нажатию на соответствующую кнопку")
    def test_click_button_outstaff(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_outstaff_button()
        main_page.click_button_outstaff()
        main_page.wait_for_outstaff_header()
        assert "#services" in main_page.current_url() and main_page.is_outstaff_header_visible()

    @allure.title("Проверка перехода в раздел 'Трудоустройство' по нажатию на соответствующую кнопку")
    def test_click_button_employment(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_employment_button()
        main_page.click_button_employment()
        main_page.wait_for_employment_header()
        assert "#services" in main_page.current_url() and main_page.is_employment_header_visible()

    @allure.title("Проверка перехода в раздел 'Консультация' по нажатию на соответствующую кнопку")
    def test_click_button_consultation(self, driver):
        main_page = MainPage(driver)
        main_page.get_urls(Urls.MAIN_PAGE_EFFECTIVE_MOBILE)
        main_page.scroll_to_bottom()
        main_page.wait_for_consultation_button()
        main_page.click_button_consultation()
        main_page.wait_for_contact_us()
        assert "#contact" in main_page.current_url() and main_page.is_contact_us_visible()