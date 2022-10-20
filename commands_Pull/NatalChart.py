from commands_Pull import User_Atributes
import sqlite3
"""
Класс, описывающий атрибуты натальной карты, собирает нужные данные и формирует картинку о пользователе
"""
db = sqlite3.connect('action.db')
sql = db.cursor('')
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    userId.BIGINT,
    act TEXT,
    fio TEXT,
    gender TEXT,
    birthdate TEXT,
    birthtime TEXT,
    city TEXT,
    country TEXT
    )""")

db.commit()
userAct = '0'
sendM = User_Atributes.ReadWriteMessage.WriteMessage()

class NatalChart():
    def __init___(self, response, name, bdate, btime, sex, city, country):
        self.name = name
        self.bdate = bdate
        self.btime = btime
        self.sex = sex
        self.city = city
        self.country = country 
        self.response = response
    
    def CorrectBirth(event, vk_session):
        date = User_Atributes.UserInfo.BirthDate(event, vk_session)
        User_Atributes.ReadWriteMessage.Dialog(func=date, count_nums=3)
        return " "
    


        