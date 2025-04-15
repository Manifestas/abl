import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_dkp1_list(self):
        sql = """SELECT
                    d.id,
                    d.contract_date,
                    d."number",
                    sel.short_name AS seller,
                    buy.short_name AS buyer,
                    count(c.id) AS cars_count,
                    round(sum(c.price)/100, 2) AS summa
                FROM
                    dkp1 d
                LEFT JOIN companies AS sel
                ON
                    sel.id = d.seller_id
                LEFT JOIN companies AS buy
                ON
                    buy.id = d.buyer_id
                LEFT JOIN cars c
                ON
                    c.dkp1_id = d.id
                WHERE
                    d.deleted_at IS NULL
                    AND buy.deleted_at IS NULL
                    AND sel.deleted_at IS NULL
                    AND c.deleted_at IS NULL
                GROUP BY
                    d.contract_date ,
                    d."number" ,
                    sel.short_name,
                    buy.short_name"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def add_dkp1(self, number, contract_date):
        sql = """INSERT INTO dkp1(number, contract_date) VALUES (?, ?)"""
        try:
            tm = math.floor(time.time())
            self.__cur.execute(sql, (number, contract_date))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления ДКП1: " + str(e))
            return False
        return True

    def get_dkp1(self, id_dkp1):
        sql = f"""SELECT
                        d.id,
                        d.contract_date,
                        d."number",
                        sel.short_name AS seller,
                        buy.short_name AS buyer
                    FROM
                        dkp1 d
                    LEFT JOIN companies AS sel
                    ON
                        sel.id = d.seller_id
                    LEFT JOIN companies AS buy
                    ON
                        buy.id = d.buyer_id
                    WHERE
                        d.deleted_at IS NULL
                        AND buy.deleted_at IS NULL
                        AND sel.deleted_at IS NULL
                        AND d.id = {id_dkp1}"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения ДКП1 из БД")

        return False, False

    def update_dkp1(self, id_dkp1, number, contract_date):
        sql = f"""UPDATE dkp1 SET number = '{number}', contract_date = '{contract_date}' WHERE id = {id_dkp1}"""
        try:
            self.__cur.execute(sql)
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления ДКП1: " + str(e))
            return False
        return True

    def get_dkp1_car_list(self, id_dkp1):
        sql = f"""
        SELECT
            c.id,
            c.vin,
            c.mark,
            c.model,
            c.color,
            round(c.price/100, 2) as price,
            d."number",
            d.id AS dkp2_id 
        FROM
            cars c
            LEFT JOIN dkp2 d
            ON d.id= c.dkp2_id 
        WHERE
            d.deleted_at IS NULL
            AND c.deleted_at IS null
            AND dkp1_id = {id_dkp1}"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def get_car(self, car_id):
        sql = f"""SELECT * from cars WHERE id = {car_id}"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения ДКП1 из БД")

        return False
