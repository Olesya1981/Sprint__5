from selenium.webdriver.common.by import By

# MainPage:
# https://stellarburgers.nomoreparties.site/
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка Конструктор на главной
CONSTRUCT_BURGER = (By.XPATH, ".//h1[text() = 'Соберите бургер']")  # блок соберите бургер на главной странице
CONSTRUCT_BURGER_XPATH = (By.XPATH, ".//h1[text() = 'Соберите бургер']")  # блок соберите бургер по XPATH
LOGIN_BUTTON = (By.XPATH, ".//button[text()= 'Войти в аккаунт']")  # Кнопка войти в аккаунт на главной странице
LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Лого на главной странице
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href ='/account']")  # Кнопка личный кабинет на главной странице

# RegistrationForm:
# https://stellarburgers.nomoreparties.site/register #страница регистрации нового пользователя
REGISTRATION_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # кнопка зарегистрироваться
PASSWORD_RECOVER_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль"
REGISTRATION_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@name='name']")  # поле ввода Имя
REGISTRATION_EMAIL_BUTTON = (By.XPATH, ".//label[text() = 'Email']/following::input[@name= 'name']")  # поле ввода Email
REGISTRATION_PASSWORD_BUTTON = (By.NAME, "Пароль")  # поле ввода Пароля
REGISTRATION_BUTTON_FINAL = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
ENTER_BUTTON = (By.XPATH, ".//a[text() ='Войти']")  # Кнопка войти
INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[text()= 'Некорректный пароль']")  # сообщение "некорректный пароль"

# Authorisation form
# https://stellarburgers.nomoreparties.site/login
ENTER_FORM = (By.XPATH, ".//h2[text() = 'Вход']")  #'вход' на странице входа в аккаунт
LOGIN_EMAIL_FIELD = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='text' ]")  # поле ввода email
LOGIN_PASSWORD_FIELD = (By.XPATH, ".//input[@name = 'Пароль']")  # поле ввода пароля
LOGIN_LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка "войти"

# Password reminder form
# https://stellarburgers.nomoreparties.site/forgot-password
FORGOT_PASSWORD_BUTTON = (By.XPATH, ".//a[text() = 'Восстановить пароль']")  #кнопка "восстановить пароль"
REMEMBER_PASSWORD_LOGIN_BUTTON = (
    By.XPATH, ".//a[@class= 'Auth_link__1fOlj' and @href ='/login' and text() = 'Войти']") # кнопка "вспомнили пароль?"

# Personal account
# https://stellarburgers.nomoreparties.site/account/profile
PROFILE = (By.XPATH, ".//a[text()= 'Профиль']")  #"Профиль"
LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")  #кнопка "выход"

# Constructor elements on main page
#https://stellarburgers.nomoreparties.site
BUNS_CLICK = (By.XPATH, "//span[text()='Булки']") #заголовок раздела Булки в конструкторе
SAUCES_CLICK = (By.XPATH, "//span[text()='Соусы']") #заголовок раздела Соусы в конструкторе
TOPPINGS_CLICK = (By.XPATH, "//span[text()='Начинки']") #заголовок раздела Начинки в конструкторе
BUNS_CLASS = (By.XPATH, ".//span[text()='Булки']/parent::div") #класс заголовка раздела Булки
SAUCES_CLASS = (By.XPATH, ".//span[text()='Соусы']/parent::div") #класс заголовка раздела Соусы
TOPPINGS_CLASS = (By.XPATH, ".//span[text()='Начинки']/parent::div") #класс заголовка раздела Начинки
