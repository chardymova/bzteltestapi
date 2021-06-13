class TokenData:
    username_list = ['test1w2e2e1', 'test1w2e2e1','testnoexuser', 111]
    password1_list = ['test1w2ep0', 'test1w2ep022','test1w2e', 123456789]
    result_list = [True, False, False, False]
    comment_list = ['Получение токена существующего пользователя(правильный пароль)', 'Получение токена существующего пользователя(неправильный пароль)', 'Получение токена несуществующего пользователя',
                    'Передача неподходящего типа данных']