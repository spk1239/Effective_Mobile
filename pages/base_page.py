from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import allure

class BasePage():

    def __init__(self, driver):

        self.driver = driver

    @allure.step("Получаем нужную страницу")
    def get_urls(self, element):
          
        self.driver.get(element)

    @allure.step("Скролим до нужного элемента")
    def scroll_to_the_element(self, locator):

        element = self.driver.find_element(*locator)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ждем указанное количество секунд')
    def wait(self, seconds=15):
        WebDriverWait(self.driver, seconds)
    
    @allure.step("Ждем появления элемента")
    def wait_element(self, locator):

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем URL')
    def wait_url(self, url):

        WebDriverWait(self.driver, 15).until(EC.url_contains(url))
    
    @allure.step("Жмем на элемент")
    def click_to_element(self, element):
          
        self.driver.find_element(*element).click()

    @allure.step('Ищем элемент')
    def find_element(self, element):

        return self.driver.find_element(*element)

    @allure.step('Проверяем что элемент появился на экране')
    def element_is_displayed(self, locator):

        element = self.driver.find_element(*locator)
        
        return element.is_displayed()
    
    @allure.step("Ждем и находим элемент")
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Проверяем URL')    
    def current_url(self, locator):
        
        return self.driver.current_url == locator

    @allure.step("Кликаем на элемент через JavaScript")
    def click_to_element_js(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ищем элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    