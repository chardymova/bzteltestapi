import csv
import requests
import pytest

from extra_data import ExtraData
from token_data import TokenData


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


class DatasetRegistration:
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
        return dataset_reg.username_list[i], \
               dataset_reg.password1_list[i], \
               dataset_reg.password2_list[i], \
               dataset_reg.result_list[i], \
               dataset_reg.comment_list[i]


def get_extra_login_data(i):
    return ExtraData.username_list[i], \
           ExtraData.password1_list[i], \
           ExtraData.password2_list[i], \
           ExtraData.result_list[i], \
           ExtraData.comment_list[i]


def get_token_data(i):
    return TokenData.username_list[i], \
           TokenData.password1_list[i], \
           TokenData.result_list[i], \
           TokenData.comment_list[i]


dataset_reg = DatasetRegistration(DatasetRegistration.get_data_from_csv, 'name-pw1-pw2.csv')
api_client = APIClient()


class TestAPI:

    @pytest.mark.parametrize('username, password1, password2, exp_result, comment',
                             [dataset_reg.get_login_data(i)
                              for i in range(len(dataset_reg.comment_list))])
    def test_status_code(self, username, password1, password2, exp_result, comment):
        data = {"username": username, "password1": password1, "password2": password2}
        response_code = api_client.post_request(path='/users', data=data).status_code
        print(response_code)
        if exp_result == 'True':
            assert 100 <= response_code < 400
        else:
            assert response_code >= 400

    @pytest.mark.parametrize('username, password1, password2, exp_result, comment',
                             [get_extra_login_data(i) for i in
                              range(len(ExtraData.comment_list))])
    def test_status_code_extra_data(self, username, password1, password2, exp_result, comment):
        data = {"username": username, "password1": password1, "password2": password2}
        response_code = api_client.post_request(path='/users', data=data).status_code
        print(response_code)
        print(username, password1, password2)
        if exp_result is True:
            assert 100 <= response_code < 400
        else:
            assert response_code >= 400

    @pytest.mark.parametrize('username, password1, exp_result, comment',
                             [get_token_data(i) for i in range(len(TokenData.comment_list))])
    def test_get_token(self, username, password1, exp_result, comment):
        data = {"username": username, "password": password1}
        print(username, password1)
        response_code = api_client.post_request(path='/login', data=data).status_code
        print(username, password1)
        if exp_result is True:
            assert 100 <= response_code < 400
        else:
            assert response_code >= 400


def main():
    pass


if __name__ == '__main__':
    main()
