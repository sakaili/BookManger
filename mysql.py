import pymysql
from main import Book


class DBHelper:
    def GetCursor(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='515310szc', db="library",
                                     charset="utf8")
        return connection

    def

        return new_id
