"""
Вытаскивает данные пользователя: имя, фамилия, пол, 
                                город рождения, дата рождения, 
                                время рождения
"""
"""
Второй класс парсит json файл, ищет слова-триггеры и выводит сообщения в беседу 
"""
#на случай, если добавлю возможность заменить "." - self.tag = tag 
from datetime import datetime
import json
from vk_api.bot_longpoll import VkBotEventType
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import Error



class UserInfo():
    def  __init__(self, event, vk_session, id):
        self.event = event
        self.vk_session = vk_session
        self.id = id
    
    def collectInfo(event, vk_session):
        vk = vk_session.get_api()
        id = event.obj['message']['from_id']
        #можно было бы и добавить филдс в сам класс, но мне вломы
        user_get=vk.users.get(user_ids = (id), fields='bdate, city, sex, country')
        user_get=user_get[0]
        return user_get

    #Вытаскивает имя пользователя
    def userFirstName(event, vk_session):
        user_get = UserInfo.collectInfo(event, vk_session)
        name=user_get['first_name']
        return str(name)

    #Фамилия, нужна для формирования натальной карты
    def userSurname(event, vk_session):
        user_get = UserInfo.collectInfo(event, vk_session)
        name=user_get['last_name']
        return str(name)
    
    #format DD.MM.YYYY нужно дописать код с заполнением общего формата
    def BirthDate(event,vk_session):
        user_get = UserInfo.collectInfo(event, vk_session)
        times = ['day', 'month', 'year']
        try:
            birthday = user_get['bdate']
            return birthday
        except Error as e:
            print(e)
        #dict_date = dict(zip(times, birthday.split("."))) 
        
        #print(len(birthday))
        
    def BirthTime(event, vk_session):
        birthtime = '?'
        #ReadWriteMessage.WriteMsg(event, vk_session, id,  'Мне нужно твое время рождения в формате HH:MM:SS'+'\n'+'Например: 09:30:00')
        #нужно чтобы он читал следующее за этим сообщение, 
        #сохранял по айди в джейсон и преобразовывал его в формат %H:%M:%S
        #в противном случае выдавал ошибку мол я не понимаю введи еще раз
        return birthtime

    def Sex(event, vk_session):
        #пол в цифрах, 1 = женский, потому что все давно знают, миром правит матриархат
        #0 = человек без пола, жалко его...
        try:
            sex = UserInfo.collectInfo(event, vk_session)['sex']
            return sex
        except Error as e:
            print(e)
            
    
    def City(event, vk_session):
        user_get = UserInfo.collectInfo(event, vk_session)
        try:
            city=user_get['city']['title']
        #code_city = user_get['city']['id']
            return str(city)
        except Error as e:
            print(e)
    

class ReadWriteMessage():
    def  __init__(self, event, vk_session, group_id, id):
        self.group_id = group_id
        self.event = event
        self.vk_session = vk_session
        self.id = id
    #формат сообщений пользователю и от пользователя
    def WriteMessage(vk_session, event, id, message: str, command):
        tag = '.'
        if tag + command in str(event).lower():
            vk_session.method("messages.send", {"peer_id": id, "message": message, "random_id": 0})
    #eсли нужно вызвать бота без команды
    def WriteMsg(vk_session, id, message: str):
        vk_session.method("messages.send", {"peer_id": id, "message": message, "random_id": 0})
    #запись в json
    def ParseJson(event, group_id):
        d1 = event.object.message
        s1 = json.dumps(d1)
        d2 = json.loads(s1)
        json_object = d2
        message = json_object['text']
        message = message.split(" ")
        str1 = message[0].split("|")[0]
        str1 = str1.replace("[club", "")
        if group_id == str1:
            message.pop(0)
        message = ' '.join(message).lower()
        id = json_object['peer_id']
        print(message)
        return message, id
    
    

