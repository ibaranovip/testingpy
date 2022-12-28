import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Devices(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Devices, self).__init__(api_root_url, **kwargs)

    def list_all_devices(self, **kwargs):
        return self.get("/devices", **kwargs)

    def list_one_device(self, username, **kwargs):
        return self.get("/devices/{}".format(username), **kwargs)

    def register(self, **kwargs):
        return self.post("/register", **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

    def update(self, user_id, **kwargs):
        return self.put("/update/devices/{}".format(user_id), **kwargs)

    def delete(self, name, **kwargs):
        return self.post("/delete/devices/{}".format(name), **kwargs)


devices = Devices(api_root_url)