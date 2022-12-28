import pytest
import allure

from operation.device_operation import get_all_user_info

from testcase.conftest import api_data
from common.logger import logger





@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("Получить данные")
@allure.feature("get device information")
class TestGetDeviceInfo():


    @allure.story("This story")
    @allure.description("add description")
    @allure.issue("https://www.your.com/story", name="issue")
    @allure.testcase("https://www.your.com/story", name="test case")
    @pytest.mark.single
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             api_data["test_get_all_user_info"])
    def test_get_all_devices_info(self, except_result, except_code, except_msg):
        logger.info("*************** Start ***************")

        result = get_all_user_info()
        # print(result.__dict__)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> Ожидаемый результат: {}, фактический результат: {}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_device_info.py"])
