def baza(): #генерируем новые данные для регистрации
    import random
    symbols = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(0,10)]
    login_length = random.randint(6, 10)
    login, email, password = '', '', ''
    for _ in range(login_length):
        login += random.choice(symbols)
        password += random.choice(symbols)
        email += random.choice(symbols)
    email = login + '@' + email + '.com'
    return login, email, password

registered_email = "olesya123456@mail.ru" #почта зарегистрированного пользователя
registered_password = "12345678" # пароль зарегистрировванного пользователя
incorrect_password = "12345"

main_url = 'https://stellarburgers.nomoreparties.site/' #главная страница
login_url = 'https://stellarburgers.nomoreparties.site/login' #страница входа
registration_url = 'https://stellarburgers.nomoreparties.site/register' #страница регистрации
forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password' #страница восттановления пароля
