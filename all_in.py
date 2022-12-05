from email import message
import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
#import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from commands_Pull import Oracle, User_Atributes, DayCard
import json 
import sqlite3


token = #token
vk_session = vk_api.VkApi(token=token)
group_id = 184856977
longpoll = VkBotLongPoll(vk_session, group_id)

#хеш-таблица для тарот.тхт
oracle= '/Users/mihailkocedykov/Projects/Nerd_bot/db/oracle.txt'

db = sqlite3.connect('db/action.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    userId BIGINT,
    act TEXT,
    fio TEXT,
    gender TEXT
    )""")
#birthdate TEXT,
#birthtime TEXT,
#city TEXT,
#country TEXT
db.commit()
userAct = '0'
#User_Atributes.ReadWriteMessage.WriteMessage()

def fixMsg(msg):
	msg = "'"+msg+"'"
	return msg

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:      

		id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1]
		us_id = event.object.message['from_id']
		print(us_id, )
		
		MSG = User_Atributes.ReadWriteMessage
		
		GetInfo = User_Atributes.UserInfo
		#print(str(id), str(GetInfo.BirthDate(event, vk_session)), GetInfo.Sex(event, vk_session), GetInfo.userFirstName(event, vk_session))
		#MSG.WriteMsg(vk_session, us_id, str(id))
		#Oracle.MindReader(vk_session, event, id, oracle)
		msg = str(event).lower()
		sql.execute(f"SELECT userId FROM users WHERE userId = '{us_id}'")
		if sql.fetchone() is None:
			sql.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (us_id, 'newUser', "0", "0"))
			db.commit()
			User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, 'Привет, напиши .натальная карта, чтобы создать свою НК')
		else:
			userAct = sql.execute(f"SELECT act FROM users WHERE userId = '{us_id}'").fetchone()[0]
			if userAct == "newUser" and msg == ".совместимость": #сменить на функцию из того класса
				User_Atributes.ReadWriteMessage.WriteMsg(vk_session, id, 'Я бы вас пошипперил, но мне нужны твои данные. Напиши .натальная карта') #+ заменить . на tag + команды доступные без заноса в бд
			elif userAct == "newUser" and msg == ".натальная карта":
				name = GetInfo.userFirstName(event, vk_session)+ " " +GetInfo.userSurname(event, vk_session)
				sql.execute(f"UPDATE users SET act = 'getFio' WHERE userId = {us_id}")
				db.commit()
				MSG.WriteMsg(vk_session, id, 'имя получилось?')
				sql.execute(f"UPDATE users SET fio = {fixMsg(name)} WHERE userId = {us_id}")	
				db.commit()
				MSG.WriteMsg(vk_session, id, 'имя получилось.')
				sql.execute(f"UPDATE users SET act = 'getGender' WHERE userId = {us_id}")
				MSG.WriteMsg(vk_session, id, 'секс получился?')
				db.commit()
				sex  = GetInfo.Sex(event, vk_session)
				sex_dict = {1: "Ж", 2: "М"} #делать проверку на пол
				if sex == 1 or 2:
					sex_str = sex.dict[sex]
					sql.execute(f"UPDATE users SET gender = {fixMsg(sex_str)} WHERE userId = {us_id}")
					MSG.WriteMsg(vk_session, id, 'сех получилось')
					sql.execute(f"UPDATE users SET act = 'full' WHERE userId = {us_id}")
					MSG.WriteMsg(vk_session, id, 'фулл получилось')
					db.commit()
					MSG.WriteMsg(vk_session, id, 'Успешно')
				else: 
					msg_sex= 'Впиши свой пол: М/Ж или Н, если не хочешь делиться информацией'#реализуй клавиатурой
					MSG.WriteMsg(vk_session, id, msg_sex)
					if userAct == "getGender":
						sql.execute(f"UPDATE users SET gender = {fixMsg(msg)} WHERE userId = {us_id}")
						sql.execute(f"UPDATE users SET act = 'full' WHERE userId = {us_id}")
						db.commit()
					MSG.WriteMsg(vk_session, id, 'Успешно')
				
			elif userAct == "full" and msg == ".совместимость":
				MSG.WriteMsg(vk_session, id, 'Теперь тебе доступна .совместимость')
		

				





			#elif :



				



	#	if 'натальная карта' in str(event).lower():
	#		User_Atributes.UserInfo.BirthTime(event, vk_session, id)
