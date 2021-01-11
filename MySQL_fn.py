import pymysql
from pymysql.cursors import DictCursor
from loguru import logger
import random

class Tables:

    def __init__(self, table_name):
        self.table_name = table_name #имя стола с которым мы работаем(может быть изменино)

    @staticmethod
    def create(table_name, what):
        con = Tables.join()
        with con.cursor() as cursor:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({what}) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
            logger.info(query)
            cursor.execute(query)
            con.commit()
        con.close()

    @staticmethod # создание статичного метода
    def join():
        """
        создание подключение к базе данных, с возвратом подключения
        """
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123',
        db='WL',
        charset='utf8mb4',
        cursorclass=DictCursor)
        return connection

    @staticmethod
    def show():
        con = Tables.join()

        with con.cursor() as cursor:
            query = f'SHOW TABLES'
            logger.info(query)
            cursor.execute(query)
            tables = [*cursor]
        con.close()
        logger.info(tables)
        return tables

    def select(self, what, where):
        """
        метод для получения любых данных из таблицы, по параметрам

        """

        con = Tables.join()

        with con.cursor() as cursor:
            query = f'SELECT {what} FROM {self.table_name} WHERE {where}'
            logger.info(query)
            cursor.execute(query)
            user_information = [*cursor]
        con.close()
        return user_information[0]

    def select_all(self):
        con = Tables.join()

        with con.cursor() as cursor:
            query = f'SELECT * FROM {self.table_name}'
            logger.info(query)
            cursor.execute(query)
            user_information = [*cursor]
        con.close()
        logger.info(user_information)
        return user_information

    def insert_all(self, what):
        """
        метод для записи всех даннных в таблицу
        """

        con = Tables.join()

        with con.cursor() as cursor:
            query = f"INSERT INTO {self.table_name} VALUES ({what})"
            logger.info(query)
            cursor.execute(query)
            con.commit()
        con.close()

    def insert(self, where ,what):

        con = Tables.join()

        with con.cursor() as cursor:
            query = f"INSERT INTO {self.table_name} ({where}) VALUES ({what})"
            logger.info(query)
            cursor.execute(query)
            con.commit()
        con.close()

    def delete(self, where):

        """
        метод для удаления данных из таблицы
        """

        con = Tables.join()
        with con.cursor() as cursor:
            query = f"DELETE FROM {self.table_name} WHERE {where}"
            logger.info(query)
            cursor.execute(query)
            con.commit()
        con

    @staticmethod
    def drop(table_name):
        con = Tables.join()
        with con.cursor() as cursor:
            query = f"DROP TABLE {table_name}"
            logger.info(query)
            cursor.execute(query)
            con.commit()
        con

    def update(self, what, where):

        con = Tables.join()
        with con.cursor() as cursor:
            query = f"UPDATE {self.table_name} SET {what} WHERE {where}"
            logger.info(query)
            cursor.execute(query)
            con.commit()
        con


