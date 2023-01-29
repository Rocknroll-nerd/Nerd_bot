import sqlite3 as sq
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload

from kerykeion import KrInstance, MakeSvgInstance
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

from commands_Pull import User_Atributes, CommandDB

sql_table = """CREATE TABLE IF NOT EXISTS userInfo (
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT,
   city TEXT,
   btime TIME,
   bdate DATE,
   group_id INT);
"""
conn =  sq.connect('db/users.db')
if conn is not None:
    CommandDB.Database.create_table(conn, sql_table)
else:
    print("Error! cannot create the database connection.")

<<<<<<< HEAD
"""
Создание шаблона сообщения для натальной карты
=======
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
>>>>>>> fb7a763d28fcc8ddfb018ce75961e9f70db87684

"""
def userFriendlyData(user):
    sex = user[3]
    if sex == 1:
        gender = "женский"
    elif sex == 2:
        gender = "мужской"
    else:    
        gender = "не указан"    
    return '\n Имя: {} {} \n Пол: {} \n Город: {} \n Время: {} \n Дата: {}'.format(user[1], user[2], gender, user[4], user[5], user[6])

<<<<<<< HEAD
#обработка svg в png
def create_png(us_id, path, path_svg, path_png):
=======
#Конвертация svg в png
def create_png(us_id):
    path = 'db/charts/'
    path_svg = '{}{}NatalChart.svg'.format(path, us_id)
    path_png = '{}{}NatalChart.png'.format(path, us_id)
>>>>>>> fb7a763d28fcc8ddfb018ce75961e9f70db87684
    if os.path.exists(path_png): 
        print('png есть')
    else:             
        drawing = svg2rlg(path_svg)
        renderPM.drawToFile(drawing, path_png, fmt='PNG')
    #os.delete(path_svg)

#cоздание натала
def create_natal(us_id, path, path_svg, path_png):
    #add date and datetime, вытягивать данные из sql по us_id

    first = KrInstance(us_id, 1999, 8, 12, 9, 30, city='Yekaterinburg')
    name = MakeSvgInstance(first, new_output_directory=path)
    svg = name.makeSVG()
    

#работает внутри чата, позже добавится возможность писать в лс группы
def main():
<<<<<<< HEAD
    __token = #token
    vk_session = vk_api.VkApi(token=__token)
    group_id = #id
=======
    token = #token
    vk_session = vk_api.VkApi(token=token)
    group_id = #group_id
>>>>>>> fb7a763d28fcc8ddfb018ce75961e9f70db87684
    longpoll = VkBotLongPoll(vk_session, group_id)
    upload = VkUpload(vk_session)
    UI = User_Atributes.UserInfo
    global user
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if '.натальная карта' in str(event).lower():
                #добавить клавиатуру с кнопками: создать свою, из базы данных, добавить в бд
                path = 'db/charts/'
                us_id = event.object.message['from_id']
                path_svg = '{}{}NatalChart.svg'.format(path, us_id)
                path_png = '{}{}NatalChart.png'.format(path, us_id)
                id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
                user = (us_id, UI.userFirstName(event, vk_session), UI.userSurname(event, vk_session), UI.Sex(event, vk_session), UI.City(event, vk_session), UI.BirthTime(event), UI.BirthDate(event, vk_session), id)
                CommandDB.Database.create_usinfo(conn, user)
                #year, month, day, hour, minutes
                create_natal(us_id, path, path_svg, path_png)
                print("Натальная карта готова")
                create_png(us_id, path, path_svg, path_png)
                if os.path.exists(path_svg):
                    os.remove(path_svg)
                photo = upload.photo_messages(photos=path_png)[0]
                #добавить проверку на наличие даты и времени рождения
                vk_session.method("messages.send", {"peer_id": id, "message":"Ваши данные: \n {} \n Если вы хотите изменить данные, введите .обновить".format(userFriendlyData(user)), "random_id": 0, "attachment": 'photo{}_{}'.format(photo['owner_id'], photo['id'])})
                #User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, "Ваши данные: \n" + userFriendlyData(user))    
                if os.path.exists(path_png):
                    os.remove(path_png)
            
            if '.обновить'in str(event).lower():
                #дать возможность ввода с клавиатуры город, пол, дату, время в формате чч:мм 
                us_id = event.object.message['from_id']
                id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
                dict_commands = {1: "Пол", 2: "Место рождения", 3: "Дата рождения", 4: "Время рождения"}
                message = ''.join('{} {} \n'.format(key, val) for key, val in dict_commands.items())
                mess = 'Введите цифру позиции, которую хотите заменить:\n{}\n'.format(message)
                User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, mess)    
                #update_usinfo(conn, user)

            if '.удалить'in str(event).lower():
                #добавить возможность удалять из бд или свои данные, клавиатура
                us_id = event.object.message['from_id']
                id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
                CommandDB.Database.del_usinfo(conn, us_id)
                User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, "Ваши данные успешно удалены")    
        

if __name__ == '__main__':
    main()
