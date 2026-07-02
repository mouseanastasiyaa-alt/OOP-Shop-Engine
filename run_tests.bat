@echo off
chcp 65001 >nul
echo ========================================
echo     ЗАПУСК ТЕСТОВ С ПОКРЫТИЕМ
echo ========================================
echo.

echo Запуск тестов...
poetry run pytest tests/ -v

echo.
echo Запуск тестов с покрытием...
poetry run pytest --cov=src --cov-report=term --cov-report=html tests/

echo.
echo [OK] Отчет о покрытии создан в папке htmlcov/
echo Откройте htmlcov/index.html в браузере
echo.
pause
