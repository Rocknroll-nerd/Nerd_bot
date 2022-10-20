import random

#я обязательно превращу тебя в нейронку
from commands_Pull import User_Atributes

def MindReader(vk_session, event, id, text: str):
	#random.seed(42)
	with open(text) as t:
		lines= t.readlines()
		oracle = [line.split("\n") for line in lines]
		t.close()
		oracle = oracle[random.randint(0,len(oracle)-1)][0]
		message = User_Atributes.UserInfo.userFirstName(event, vk_session)+", " + oracle
		User_Atributes.ReadWriteMessage.WriteMessage(event, vk_session, id, message, 'предсказание')

