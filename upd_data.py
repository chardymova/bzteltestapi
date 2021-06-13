from extra_data import ExtraData
# def upd_user_counter():
#     '''Имя пользователей не должно повторяться,
#     поэтому мы обновляем счетчик пользователя
#     для дальнейшей генерации юзернейма (где юзернейм = стандартное значение + счетчик).'''
#     with open('user_counter.txt', 'r') as f:
#         counter = int(f.read())
#     with open('user_counter.txt', 'w') as f:
#         f.write(str(counter + 1))
#         return str(counter)

def get_user_counter():
    with open('user_counter.txt', 'r') as f:
        counter = int(f.read()) - 1
        print(counter)
    with open('user_counter.txt', 'w') as f:
        f.write(str(counter))
    return str(counter)

#user_id_for_upd = get_user_counter()

class UpdatePwData:

    username_list = ['test1w2e2e' + user_id_for_upd,
                     'test1w2e2e' + user_id_for_upd,
                     'test1w2e2e22' + user_id_for_upd,
                     'test1w2e2e' + user_id_for_upd,
                     'test1w2e2e' + user_id_for_upd,
                     'test1w2e2e' + user_id_for_upd]
    old_password_list = [ExtraData.password1_list[1],
                         ExtraData.password1_list[1],
                         ExtraData.password1_list[1],
                         ExtraData.password1_list[1] + '3',
                         ExtraData.password1_list[1],
                         1231231232]
    password1_list = [ExtraData.password1_list[1] + user_id_for_upd,
                      ExtraData.password1_list[1],
                      ExtraData.password1_list[1] + user_id_for_upd,
                      ExtraData.password1_list[1] + user_id_for_upd,
                      'ncPW',
                      123123123]
    password2_list = [ExtraData.password1_list[1] + user_id_for_upd,
                      ExtraData.password1_list[1],
                      ExtraData.password1_list[1] + user_id_for_upd,
                      ExtraData.password1_list[1] + user_id_for_upd,
                      'ncPW',
                      123123123]
    result_list = [True, False, False, False, False, False]
    comment_list = ['Обновление пароля на новое отличающееся значение',
                    'Использование старого пароля вместо нового',
                    'Обновление пароля для несуществующего пользователя',
                    'Неверный старый пароль',
                    'Некорректный новый пароль',
                    'Некорректный тип данных пароля']