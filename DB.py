# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup
import datetime


# создаю класс для парсинга данных с сайта
class DataBase:

    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://pay.travel/site_controller_courses/index/?date='
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        site = self.site + date
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }

        response = requests.get(site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db = {}
        for tr in trs[2]:
            tds = tr.findAll("td")
            if len(tds) < 1:
                continue
            name = tds[0].text.lower()
            usd = tds[1].text
            eur = tds[4].text
            db[name] = [usd, eur]

        return db

    def get_data(self):
        return self.data
