import requests
import pytest
import csv
from extra_data import ExtraData
from upd_data import UpdatePwData

class APIClient:
    '''Клиент для работы с API.'''

    def __init__(self, base_address='http://bzteltestapi.pythonanywhere.com'):
        self.base_address = base_address

    def put_request(self, path, data):
        '''Put запрос'''
        response = requests.put(self.base_address + str(path), json=data)
        return response

    def post_request(self, path, data):
        '''Post запрос'''
        response = requests.post(self.base_address + str(path), json=data)
        return response

class Dataset:
    def __init__(self, get_data_from_csv, data):
        get_data_from_csv(self, data)

    username_list = []
    password1_list = []
    password2_list = []
    result_list = []
    comment_list = []

    def get_data_from_csv(self, file_path):
        '''Считываем данные о пользователях из csv файла.'''
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                if row[0] == 'username':
                    continue
                self.username_list.append(row[0])
                self.password1_list.append(row[1])
                self.password2_list.append(row[2])
                self.result_list.append(row[3])
                self.comment_list.append(row[4])


    def get_login_data(self, i):
        return dataset.username_list[i], \
               dataset.password1_list[i], \
               dataset.password2_list[i], \
               dataset.result_list[i], \
               dataset.comment_list[i]
    def get_extra_login_data(self, i):
        return ExtraData.username_list[i], \
               ExtraData.password1_list[i], \
               ExtraData.password2_list[i], \
               ExtraData.result_list[i], \
               ExtraData.comment_list[i]
    def get_upd_pw_data(self, i):
        return UpdatePwData.username_list[i], \
               UpdatePwData.old_password_list[i], \
               UpdatePwData.password1_list[i], \
               UpdatePwData.password2_list[i], \
               UpdatePwData.result_list[i], \
               UpdatePwData.comment_list[i]


dataset = Dataset(Dataset.get_data_from_csv, 'name-pw1-pw2.csv')
api_client = APIClient()
class TestAPI:

    @pytest.mark.parametrize('username, password1, password2, exp_result, comment',
                             [dataset.get_login_data(i) for i in range(len(dataset.comment_list))])
    def test_status_code(self, username, password1, password2, exp_result, comment):
        data = {"username": username, "password1": password1, "password2": password2}
        response_code = api_client.post_request(path='/users', data=data).status_code
        print(response_code)
        if exp_result == 'True':
            assert 100<= response_code<400
        else:
            assert response_code>=400

    @pytest.mark.parametrize('username, password1, password2, exp_result, comment',
                             [dataset.get_extra_login_data(i) for i in
                              range(len(ExtraData.comment_list))])
    def test_status_code_extra_data(self, username, password1, password2, exp_result, comment):
        data = {"username": username, "password1": password1, "password2": password2}
        response_code = api_client.post_request(path='/users', data=data).status_code
        print(response_code)
        print(username, password1, password2)
        if exp_result == True:
            assert 100<= response_code<400
        else:
            assert response_code>=400

    @pytest.mark.parametrize('username, old_pw, password1, password2, exp_result, comment',
                             [dataset.get_upd_pw_data(i) for i in range(len(UpdatePwData.username_list))])
    def test_upd_pw(self, username, old_pw, password1, password2, exp_result, comment):
        data = {"username": username, "old_password": old_pw, "password1": password1, "password2": password2}
        response = api_client.put_request(path='/users', data=data)
        response_code = response.status_code
        print(response)
        print(response_code)
        print(username, old_pw, password1)

        if exp_result == True:
            assert 100<= response_code<400
        else:
            assert response_code>=400



def main():
    pass


if __name__ == '__main__':
    main()
