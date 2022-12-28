import requests
import json as complexjson
from common.logger import logger


class RestClient():

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:

                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("Адрес запроса интерфейса ==>> {}".format(url))
        logger.info("Метод запроса интерфейса ==>> {}".format(method))

        logger.info("заголовок запроса интерфейса ==>> {}".format(complexjson.dumps(headers, indent=4 )))
        logger.info("Параметр параметров запроса интерфейса ==>> {}".format(complexjson.dumps(params, indent=4 )))
        logger.info("Параметр данных тела запроса интерфейса ==>> {}".format(complexjson.dumps(data, indent=4 )))
        logger.info("JSON-параметр тела запроса интерфейса==>> {}".format(complexjson.dumps(json, indent=4 )))
        logger.info("Параметр загрузки вложенных файлов интерфейса==>> {}".format(files))
        logger.info("Параметр cookie интерфейса ==>> {}".format(complexjson.dumps(cookies, indent=4 )))
