#Решила через pandas сформировать сбор и обработку данных по натальным картам
#посмотрим, как по скорости и костылям, но по-другому я долго буду учиться уметь
import pandas as pd
import numpy as np

#тестовый словарик колонок к датафрейму
user_data =[
    "User ID", 
    "Username",
    "Year of birth",
    "Month of Birth",
    "Day of birth",
    "Birth Time",
    "Place of Birth",
    "Description"
]



UserData = pd.DataFrame(columns=user_data)
print(UserData)
print(UserData.columns)