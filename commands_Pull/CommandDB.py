
import sqlite3 as sql3

from matplotlib.pyplot import connect

"""Database class holds user info for generating oracles and natal charts"""
class Database(object):
	__db = sql3.connect('db/action.db')
	def __init__(self):
		self.connection = sql3.connect(Database.__db)
		self.cur = self.connection.cursor()
		
	def close(self):
		self.connection.close()

	def execute(self, new_data):
		self.cur.execute(new_data)

	def create():
		sql3.execute("""CREATE TABLE IF NOT EXISTS users (§
            userId BIGINT,
            act TEXT,
			fio TEXT,
			gender TEXT
			)""")
		Database.__db.commit()
		userAct = '0'
	
	def actions(userAct):
		pass

	def fixMsg(msg):
		msg = "'"+msg+"'"
		return msg


#User_Atributes.ReadWriteMessage.WriteMessage()



"""
for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:      
		#я вообще зеро в джейсонах, скопировала с инета, мне понравилось 
		id = User_Atributes.ReadWriteMessage.ParseJson(event, group_id)[1] #это не id пользователя а id группы
		us_id = event.object.message['from_id']
		print(us_id)
		
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
"""

				





		