import sqlite3 as sq
import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from commands_Pull import User_Atributes
from sqlite3 import Error


conn =  sq.connect('db/users.db')
cur = conn.cursor()

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
    sql_ = ''' INSERT OR IGNORE INTO userInfo (userid, fname, lname, gender, city, btime, bdate) VALUES (?, ?, ?, ?, ?, ?, ?) '''
    cur.execute(sql_, usinfo)
    conn.commit()
    return cur.lastrowid

def userFriendlyData(user):
    sex = user[3]
    if sex == 1:
        gender = "женский"
    elif sex == 2:
        gender = "мужской"
    else:    
        gender = ""    
    m = 'Имя:{} \n Пол:{} \n Город: {} \n Время: {} \n Дата: {}'.format(user[1:3], gender, user[4], user[5], user[6])
    return m

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if '.натальная карта' in str(event).lower():
            us_id = event.object.message['from_id']
            id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
            user = (us_id, User_Atributes.UserInfo.userFirstName(event, vk_session), User_Atributes.UserInfo.userSurname(event, vk_session), User_Atributes.UserInfo.Sex(event, vk_session), User_Atributes.UserInfo.City(event, vk_session), User_Atributes.UserInfo.BirthTime(event, vk_session), User_Atributes.UserInfo.BirthDate(event, vk_session))
            create_usinfo(conn, user)
            User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, "Ваши данные: \n" + userFriendlyData(user))
            
