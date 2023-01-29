
import sqlite3 as sq
from sqlite3 import Error 
"""

	Database class holds user info for generating oracles and natal charts
"""

class Database():
    """
	Database class holds tables with user info 
    """
    def __init__(self, table, conn, usinfo):
        self.conn = conn
        self.usinfo = usinfo
        self.table = table

    def create_table(conn, table):
        try:
            c = conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def create_usinfo(conn, usinfo):
        cur = conn.cursor()
        sql_ = '''INSERT OR IGNORE INTO userInfo (userid, fname, lname, gender, city, btime, bdate, group_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        cur.execute(sql_, usinfo)
        conn.commit()
        return cur.lastrowid

    def update_usinfo(conn, usinfo):
        sql_ = '''UPDATE userInfo 
            SET gender = ?, city = ?, 
                btime = ?, bdate = ? 
            WHERE userid = ?'''
        cur = conn.cursor()
        cur.execute(sql_, usinfo)
        conn.commit()

    def del_usinfo(conn, us_id):
        #обязательно: ограничение по id, чтобы не было возможности удалять всех подряд
        #писать ворнинги, типа удалить эту нк может только пользователь (вытянуть ФИО по ID)
        sql = 'DELETE FROM userInfo WHERE userid = ?'
        cur = conn.cursor()
        cur.execute(sql, (us_id,))
        conn.commit()
