from selenium.webdriver.common.by import By

class MainPageLocators():

    BUTTON_SUBMIT_APPLICATION = (By.XPATH, "//button[text()='Оставить заявку']")

    BUTTON_LEARN_MORE = (By.XPATH, "//button[text()='Узнать больше']")

    BUTTON_CURRENT_VACANCIES = (By.XPATH, "//a[text()='Актуальные вакансии']")

    BOTTOM_BUTTON_ABOUT_US = (By.XPATH, "//a[text()='О нас']")

    BOTTOM_BUTTON_VACANCY = (By.XPATH, "//a[text()='Вакансии']")

    BOTTOM_BUTTON_REVIEWS = (By.XPATH, "//a[text()='Отзывы']")

    BOTTOM_BUTTON_CONTACTS = (By.XPATH, "//a[text()='Контакты']")

    BOTTOM_BUTTON_OUTSTAFF = (By.XPATH, "//a[text()='Аутстафф']")

    BOTTOM_BUTTON_EMPLOYMENT = (By.XPATH, "//a[text()='Трудоустройство']")

    BOTTOM_BUTTON_CONSTULTATION = (By.XPATH, "//a[text()='Консультация']")

    HEADLINE_CONTACT_US = (By.XPATH, "//h2[text()='Свяжитесь с нами']")

    HEADLINE_EMPLOYEE_FORM = (By.XPATH, "//h2[text()='Форматы сотрудничества']")

    OUTSTAFF_HEADER = (By.XPATH, "//h3[text()='Аутстафф']")

    EMPLOYMENT_HEADER = (By.XPATH, "//h3[text()='Помощь в трудоустройстве']")