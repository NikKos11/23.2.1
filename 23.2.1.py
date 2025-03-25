import requests
from bs4 import BeautifulSoup
import pandas as pd
user_login = input('Введите логин пользователя Киноафиша: ') #Пример: 15001288

def collect_user_rates(user_login):
    data = []

    while True:
        url = f'https://www.kinoafisha.info/user/{user_login}/votes/'

        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content, 'lxml')

        entries = soup.find_all('div', class_='profileRatingsList_item')

        if len(entries) == 0:
            break

        for entry in entries:
            film_name = entry.find('a').text

            profileRatingsList = entry.find('div', class_='profileRatingsList_mark mark')
            rating = profileRatingsList.find('span', class_='mark_num')
            user_rating = rating.text

            data.append({'Название фильма или сериала': film_name, 'Рейтинг пользователя': user_rating})
    return data
user_rates = collect_user_rates(user_login)
df = pd.DataFrame(user_rates)

df.to_excel('user_rates1.xlsx')
