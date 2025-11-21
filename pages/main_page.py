import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("Жмем кнопку Оставить заявку")
    def click_button_submit_application(self):
        self.click_to_element(MainPageLocators.BUTTON_SUBMIT_APPLICATION)

    @allure.title("Жмем кнопку Узнать больше")
    def click_button_learn_more(self):
        self.click_to_element(MainPageLocators.BUTTON_LEARN_MORE)

    @allure.title("Жмем кнопку Актуальные вакансии")
    def click_button_current_vacancies(self):
        self.click_to_element(MainPageLocators.BUTTON_CURRENT_VACANCIES)

    @allure.title("Жмем кнопку О нас")
    def click_button_about_us(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_ABOUT_US)

    @allure.title("Жмем кнопку Вакансии")
    def click_button_vacancy(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_VACANCY)

    @allure.title("Жмем кнопку Отзывы")
    def click_button_reviews(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_REVIEWS)

    @allure.title("Жмем кнопку Контакты")
    def click_button_contacts(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_CONTACTS)

    @allure.title("Жмем кнопку Аутстафф")
    def click_button_outstaff(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_OUTSTAFF)

    @allure.title("Жмем кнопку Трудоустройство")
    def click_button_employment(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_EMPLOYMENT)

    @allure.title("Жмем кнопку Консультация")
    def click_button_consultation(self):
        self.click_to_element(MainPageLocators.BOTTOM_BUTTON_CONSTULTATION)

    @allure.step('Проверяем что заголовок "Свяжитесь с нами" отображается')
    def is_contact_us_visible(self):
        return self.element_is_displayed(MainPageLocators.HEADLINE_CONTACT_US)
    
    @allure.step('Проверяем что заголовок "Форма сотрудничества" отображается')
    def is_employee_form_visible(self):
        return self.element_is_displayed(MainPageLocators.HEADLINE_EMPLOYEE_FORM)
    
    @allure.step("Ожидаем появление заголовка 'Форма сотрудничества'")
    def wait_for_employee_form(self):
        self.wait_element(MainPageLocators.HEADLINE_EMPLOYEE_FORM)
    
    @allure.step("Ожидаем появление заголовка 'Свяжитесь с нами'")
    def wait_for_contact_us(self):
        self.wait_element(MainPageLocators.HEADLINE_CONTACT_US)