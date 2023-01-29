import sqlite3 as sq
import vk_api
#from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType 
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard  
from commands_Pull import User_Atributes, CommandDB
from sqlite3 import Error
from kerykeion import KrInstance, MakeSvgInstance
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

Database = CommandDB.Database

conn =  sq.connect('db/users.db')

def main():
    token = #token
    vk_session = vk_api.VkApi(token=token)
    group_id = #id
    longpoll = VkLongPoll(vk_session)
    
    keyboard = VkKeyboard(one_time=True)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW: 
            if event.to_me:
                if '.обновить'in str(event).lower():
                    us_id = event.object.message['from_id']
                    UI = User_Atributes.UserInfo
                    user = (us_id, UI.userFirstName(event, vk_session), UI.userSurname(event, vk_session), UI.Sex(event, vk_session), UI.City(event, vk_session), UI.BirthTime(event, vk_session), UI.BirthDate(event, vk_session))
                    #дать возможность ввода с клавиатуры город, пол, дату, время в формате чч:мм                 
                    id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
                    keyboard.add_button('Пол')
                    keyboard.add_button('Место рождения')
                    keyboard.add_button('Дата рождения')
                    keyboard.add_button('Время рождения')
                    print("клава готова")
                    User_Atributes.ReadWriteMessage.WriteMessage(vk_session, event, id, "Выберите, какие данные нужно обновить", keyboard.keyboard())
                #Database.update_usinfo(conn, user)ß

if __name__ == "__main__":
    main()