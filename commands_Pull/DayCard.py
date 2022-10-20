import random
# для этого точно нужно понять как организовать данные в таблице
dayCard= {1: ["Шут", "Кто? Я дурак? А может быть ты ", "photo-184856977_457239059"], 2: ["Верховная Жрица", 
	"Самосознание, обучаемость, внимательность. В негативе: Эмоциональный кризис, эгоизм, антиобщественное поведение.", 
	"photo-184856977_457239058"]}

    
class CardOfTheDay:
    def __init__(self, text, link):
        self.link = link
        self.text = text
        
    def Card(self, picture, link, description):
        self.p = picture
        self.l = link
        self.d = description
        #if ".карта дня" in str(event).lower():
		#	card = dayCard[random.randint(1, len(dayCard))]
		#	vk_session.method("messages.send", {"peer_id": id, "message": str(card[0])+'\n' +'\n' +str(card[1]), "attachment": str(card[2]), "random_id": 0})

