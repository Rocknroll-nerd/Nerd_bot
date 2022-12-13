import sqlite3 as sq
import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType 
from vk_api import VkUpload 
from commands_Pull import User_Atributes
from sqlite3 import Error
from kerykeion import KrInstance, MakeSvgInstance
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

conn =  sq.connect('db/users.db')

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_table = """CREATE TABLE IF NOT EXISTS userInfo (
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT,
   city TEXT,
   btime TEXT,
   bdate TEXT);
"""

if conn is not None:
    create_table(conn, sql_table)
else:
    print("Error! cannot create the database connection.")

token = '4cddc11e4389db86810ee2d30ad489af34bf6f4121b3e4a2a4a66e9770b9d90791c179e4cdae8a5206b76'
vk_session = vk_api.VkApi(token=token)
group_id = 184856977
longpoll = VkBotLongPoll(vk_session, group_id)

def create_usinfo(conn, usinfo):
    cur = conn.cursor()
    sql_ = '''INSERT OR IGNORE INTO userInfo (userid, fname, lname, gender, city, btime, bdate) VALUES (?, ?, ?, ?, ?, ?, ?) '''
    cur.execute(sql_, usinfo)
    conn.commit()
    return cur.lastrowid

def update_usinfo(conn, usinfo):
    sql_ = '''UPDATE userInfo 
        SET gender = ?, city = ?, 
            btime = ?, bdate = ? 
        WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql_, usinfo)
    conn.commit()

def del_usinfo(conn, usinfo):
    #обязательно: ограничение по id, чтобы не было возможности удалять всех подряд
    #писать ворнинги, типа удалить эту нк может только пользователь (вытянуть ФИО по ID)

    pass

def userFriendlyData(user):
    sex = user[3]
    if sex == 1:
        gender = "женский"
    elif sex == 2:
        gender = "мужской"
    else:    
        gender = "не указан"    
    return '\n Имя: {} {} \n Пол: {} \n Город: {} \n Время: {} \n Дата: {}'.format(user[1], user[2], gender, user[4], user[5], user[6])

def create_png(us_id):
    path = 'db/charts/'
    path_svg = '{}{}NatalChart.svg'.format(path, us_id)
    path_png = '{}{}NatalChart.png'.format(path, us_id)
    if os.path.exists(path_png): 
        print('png есть')
    else:             
        drawing = svg2rlg(path_svg)
        # download output file - скачиваем JPG картинку
        renderPM.drawToFile(drawing, path_png, fmt='PNG')
        os.delete()

#работает внутри чата, позже добавится возможность писать в лс беседы
def main():
    token = '4cddc11e4389db86810ee2d30ad489af34bf6f4121b3e4a2a4a66e9770b9d90791c179e4cdae8a5206b76'
    vk_session = vk_api.VkApi(token=token)
    group_id = 184856977
    longpoll = VkBotLongPoll(vk_session, group_id)
    upload = VkUpload(vk_session)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if '.натальная карта' in str(event).lower():
                #добавить клавиатуру с кнопками: создать свою, из базы данных, добавить в бд
                path = 'db/charts/'
                us_id = event.object.message['from_id']
                id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
                UI = User_Atributes.UserInfo
                user = (us_id, UI.userFirstName(event, vk_session), UI.userSurname(event, vk_session), UI.Sex(event, vk_session), UI.City(event, vk_session), UI.BirthTime(event, vk_session), UI.BirthDate(event, vk_session))
                city = UI.City(event, vk_session)
                create_usinfo(conn, user)
                #year, month, day, hour, minutes
                first = KrInstance(us_id, 1999, 8, 12, 9, 30, city=city)
                name = MakeSvgInstance(first, new_output_directory=path)
                svg = name.makeSVG()
                path_png = '{}{}NatalChart.png'.format(path, us_id)
                create_png(us_id)
                photo = upload.photo_messages(photos=path_png)[0]
                #добавить проверку на наличие даты и времени рождения
                vk_session.method("messages.send", {"peer_id": id, "random_id": 0, "attachment": 'photo{}_{}'.format(photo['owner_id'], photo['id'])})
                User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, "Ваши данные: \n" + userFriendlyData(user))    
                
        

if __name__ == '__main__':
    main()
