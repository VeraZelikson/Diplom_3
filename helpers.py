import allure
import requests
from fakedata import FakeData
from test_data import TestData
from endpoints import Url


@allure.step('Зарегистрировать нового юзера и вернуть его данные')
def register_new_user_and_return_user_data():
    user_data = {}
    email = FakeData.generate_random_email()
    password = FakeData.generate_random_password(10)
    name = FakeData.generate_random_name()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    response = requests.post(Url.CREATE_USER_HANDLE, data=payload)

    if response.status_code == 200:
        user_data = {
            'email': email,
            'password': password,
            'name': name,
            'status_code': response.status_code,
            'json': response.json()
        }

    return user_data


@allure.step('Удалить юзера')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Url.DELETE_USER_HANDLE, headers=headers)


@allure.step('Создать заказ')
def create_order(user):
    payload = {
        'ingredients': [TestData.INGREDIENTS]
    }
    headers = {'Authorization': user['json']['accessToken']}
    response = requests.post(Url.ORDERS_HANDLE, data=payload, headers=headers)
    return response
