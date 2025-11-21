# UI Tests - Effective Mobile

Автотесты для сайта "Effective Mobile"

**Технологии:** Python 3.10, Selenium, Pytest, Allure, Docker

**Структура проекта:**
- `pages/` - классы Page Object Model
- `locators/` - локаторы элементов  
- `tests/` - тестовые сценарии
- `urls.py` - URL для тестирования

**Запуск тестов:**
```bash
# Локальный запуск
pytest tests/ -v --browser=chrome

# С отчетом Allure
pytest tests/ -v --alluredir=allure-results
allure serve allure-results

# Docker
docker build -t selenium-tests .
docker run --rm selenium-tests
