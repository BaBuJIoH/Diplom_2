Diplom_2

1. Создал папку utils с исполняемыми файлами:
    1.1. Вынес базвый URL в файл config.py
    1.2. В файле api_client.py класс ApiClient обрабатывает все запросы и использует BASE_URL из config.py
    1.3. Тестовые данные вынес в файл data.py
2. Создал файл conftest.py с фикстурами
3. Все автотесты вынесены в папку tests
4. Зависимости добавлены в requirements.txt
5. Исключения добавлены в .gitignore
6. Создана папка allure-results с отчётом Allue
