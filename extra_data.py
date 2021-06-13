'''Часть тестов отправки запросов с тестовыми данными из файла "name-pw1-pw2.csv" не прошла, потому что:
Ограничения на юзер нейм: от 6 до 32 символов.
Ограничения на пароль: от 6 до 20 символов.
На основе этого генерируем добавляем новые тестовые данные.'''
def upd_user_counter():
    '''Имя пользователей не должно повторяться,
    поэтому мы обновляем счетчик пользователя
    для дальнейшей генерации юзернейма (где юзернейм = стандартное значение + счетчик).'''
    with open('user_counter.txt', 'r') as f:
        counter = int(f.read())
        print(counter, "extra")
    with open('user_counter.txt', 'w') as f:
        f.write(str(counter + 1))
        print(counter, "записали")
        return str(counter)



user_id_for_create = upd_user_counter()

class ExtraData:
    username_list = ['test1w2e2e' + user_id_for_create, 'test1w2e2e' + user_id_for_create, 12345678,
                     'test1w2e' + user_id_for_create]
    password1_list = ['test1w2ep0', 'test1w2ep0', 123456789, 'test1w2e' + user_id_for_create]
    password2_list = ['test1w2ep0', 'test1w2ep0', 123456789, 'test1w2e' + user_id_for_create]
    result_list = [True, False, False, False]
    comment_list = ['Регистрация пользователя с корректными данными', 'Регистрация уже существующего пользователя',
                    'Передача неподходящего типа данных', 'Пароли не отличающиеся от логина']
