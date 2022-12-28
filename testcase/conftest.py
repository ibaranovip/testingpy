import pytest
import os
import allure
from api.devices import devices
from common.mysql_operation import db
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")


@allure.step("Предварительные шаги ==>> чистые данные")
def step_first():
    logger.info("******************************")
    logger.info("Предшаговый старт ==>> чистые данные")


@allure.step("После шага ==>> очистить данные")
def step_last():
    logger.info("После шага ==>> очистить данные")


@allure.step("Предварительные шаги ==>> Вход администратора")
def step_login(username, password):
    logger.info("Предварительные шаги ==>> администратор {} логин, обратная информация: {}".format(username, password))


@pytest.fixture(scope="session")
def login_fixture():
    username = base_data["init_admin_user"]["username"]
    password = base_data["init_admin_user"]["password"]
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": username,
        "password": password
    }
    loginInfo = devices.login(data=payload, headers=header)
    step_login(username, password)
    yield loginInfo.json()


@pytest.fixture(scope="function")
def insert_delete_user():



@pytest.fixture(scope="function")
def delete_register_user():

