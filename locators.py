class Locator:
    # Заголовок страницы
    PAGE_TITLE = "h1.title"  # Заголовок страницы

    # Регистрация
    NAME_FIELD = "input[name='name']"  # Поле "Имя"
    EMAIL_FIELD = "input[name='email']"  # Поле "Email"
    PASSWORD_FIELD = "input[name='password']"  # Поле "Пароль"
    REGISTER_BUTTON = "button[data-test='register']"  # Кнопка "Зарегистрироваться"

    # Вход
    LOGIN_BUTTON_MAIN = "button[data-test='login-main']"  # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_PERSONAL_CABINET = "button[data-test='login-cabinet']"  # Кнопка "Личный кабинет"
    LOGIN_BUTTON_REGISTER = "button[data-test='login-register']"  # Кнопка в форме регистрации
    LOGIN_BUTTON_RECOVERY = "button[data-test='login-recovery']"  # Кнопка в форме восстановления пароля

    # Личный кабинет
    PERSONAL_CABINET_BUTTON = "button[data-test='personal-cabinet']"  # Кнопка "Личный кабинет"
    LOGOUT_BUTTON = "button[data-test='logout']"  # Кнопка "Выйти"

    # Конструктор
    CONSTRUCTOR_BUTTON = "button[data-test='constructor']"  # Кнопка "Конструктор"
    BUNS_SECTION = "a[data-test='buns']"  # Раздел "Булки"
    SAUCES_SECTION = "a[data-test='sauces']"  # Раздел "Соусы"
    FILLINGS_SECTION = "a[data-test='fillings']"  # Раздел "Начинки"