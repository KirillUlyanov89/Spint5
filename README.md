
## Структура проекта_v2


    - `locators.py`: Локаторы для элементов на веб-странице, используемые в тестах.
    - `data.py`: Переменные для тестов.
- **`tests/`**: Папка, содержащая все тестовые файлы и настройки.
    - `test_constructor_navigation.py`: Проверяет переход по разделам "Булки", "Соусы", "Начинки" в конструкторе.
    - `test_navigation.py`: Проверяет переход в личный кабинет пользователя.
    - `test_login.py`: Проверяет различные способы входа в профиль.
    - `test_logout.py`: Проверяет функциональность выхода из профиля.
    - `test_registration.py`: Проверяет регистрацию пользователя.

## Тесты

### `test_registration.py`

- **test_successful_registration**: Проверяет успешную регистрацию пользователя с корректным именем, email и паролем.
- **test_failed_registration_short_password**: Проверяет отображение ошибки при попытке регистрации с некорректным паролем.

### `test_login.py`

- **test_login_via_main_page**: Проверяет вход по кнопке "Войти в аккаунт" на главной странице.
- **test_login_via_profile_button**: Проверяет вход через кнопку "Личный кабинет".
- **test_login_via_register_button**: Проверяет вход через кнопку в форме регистрации.
- **test_login_via_forgot_password_button**: Проверяет вход через кнопку в форме восстановления пароля.

### `test_logout.py`

- **test_logout_from_personal_cabinet**: Проверяет функциональность выхода из личного кабинета.

### `test_navigation.py`

- **test_navigate_to_personal_cabinet**: Проверяет переход в личный кабинет по клику на кнопку "Личный кабинет" после входа в систему.


### `test_constructor_navigation.py`

- **test_navigate_to_sections**: Проверяет переходы между разделами "Булки", "Соусы", "Начинки" в конструкторе.
