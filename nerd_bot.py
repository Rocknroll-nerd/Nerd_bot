import vk_api, vk

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='4ee575aeef3c9c53737cdf1d908cfff658a32a27491c5e37bf17cd95a5a76b6b6b76bfa32118fd6d491d9')
longpoll = VkBotLongPoll(vk_session, 184856977)
vk = vk_session.get_api()

oracle= {1: "вас ждет замечательный день", 2:"сегодня появится повод для радости", 3:"остерегайтесь сердечного признания в любви",
4: "попробуй карту Мир. Говорят, сегодня московское метро принимает старшие арканы"}
#count = len(oracle)
#forecast = random.randint(1, count)
#forecast = oracle[random.randint(1, count)]

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:
		#user_get=vk.users.get(user_ids = (id))
		#user_get=user_get[0]
		#name=user_get['first_name']
		if "Привет" in str(event) or "Нерда привет" in str(event)  or "Нерда, привет" in str(event):
			if event.from_chat:
				vk.messages.send(
					key=('43c8452e0529c35a05531fa83ee87ef0dc40dcd6'), 
					server = ("https://lp.vk.com/wh184856977"),
					ts=('1'),
					random_id= get_random_id(),
					message='Привет!',
					chat_id = event.chat_id
					)
		if ".предсказание" in str(event):
			if event.from_chat:
				#print_oracle=name + ", " + oracle[random.randint(1, len(oracle))]
				vk.messages.send(
					key=('43c8452e0529c35a05531fa83ee87ef0dc40dcd6'), 
					server = ("https://lp.vk.com/wh184856977"),
					ts=('1'),
					random_id= get_random_id(),
					message= oracle[random.randint(1, len(oracle))],
					chat_id = event.chat_id
					)




		


