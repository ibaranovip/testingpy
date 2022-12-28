import pymysql
import os
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mysql"]

DB_CONF = {
    "host": data["MYSQL_HOST"],
    "port": int(data["MYSQL_PORT"]),
    "user": data["MYSQL_USER"],
    "password": data["MYSQL_PASSWD"],
    "db": data["MYSQL_DB"]
}


class MysqlDb():

    def __init__(self, db_conf=DB_CONF):

        self.conn = pymysql.connect(**db_conf, autocommit=True)

        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):

        self.cur.close()

        self.conn.close()

    def select_db(self, sql):

        self.conn.ping(reconnect=True)
        #  execute()  sql
        self.cur.execute(sql)
        #  fetchall()
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):

        try:

            self.conn.ping(reconnect=True)

            self.cur.execute(sql)

            self.conn.commit()
        except Exception as e:
            logger.info("Произошла ошибка в работе MySQL, причина ошибки: {}".format(e))

            self.conn.rollback()


db = MysqlDb(DB_CONF)
