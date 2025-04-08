import random
def baza(): #генерируем новые данные для регистрации

    symbols = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(0,10)]
    login_length = random.randint(6, 10)
    login, email, password = '', '', ''
    for _ in range(login_length):
        login += random.choice(symbols)
        password += random.choice(symbols)
        email += random.choice(symbols)
    email = login + '@' + email + '.com'
    return login, email, password