# UI Tests - Effective Mobile

Автотесты для сайта "Effective Mobile"

**Структура проекта:**
- `pages/` - классы страниц в стиле Page Object
- `locators/` - локаторы элементов  
- `tests/` - тестовые сценарии
- `urls.py` - URL для тестирования

**Запуск тестов:**
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск в Chrome
pytest tests/ -v --browser=chrome

# Запуск в Firefox  
pytest tests/ -v --browser=firefox

# С отчетом Allure
pytest tests/ -v --alluredir=allure-results
allure serve allure-results

# Запуск в Docker
docker build -t selenium-tests .
docker run --rm selenium-tests
