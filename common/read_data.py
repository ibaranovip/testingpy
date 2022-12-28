import yaml
import json
from configparser import ConfigParser
from common.logger import logger

class MyConfigParse(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)
    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():
    def __int__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("dowm load==>>  {} ".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data =yaml.safe_load(f)
        logger.info("read_date==>>  {} ".format(data))
        return data

    def load_json(self, file_path):
        logger.info("down_load==>>  {} ".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("read_date==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("load...==>>  {} .".format(file_path))
        config = MyConfigParse()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("чтение ==>>  {} ".format(data))
        return data

data = ReadFileData()