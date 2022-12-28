from core.result_base import ResultBase
from api.devices import devices
from common.logger import logger


def get_all_user_info():

    result = ResultBase()
    res = devices.list_all_devices()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "Код возврата интерфейса 【 {} 】, info：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    return result



