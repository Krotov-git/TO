# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class ICS:
    #TODO: сущность туроператора ICS

    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://www.icstrvl.ru/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        site = 'https://www.icstrvl.ru/'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_ics = {}
        i = 0
        for tr in trs[0]:
            i += 1
            if i == 8:
                tds = tr.findAll("td")
                name = 'ICS'
                usd = tds[3].text
                eur = tds[3].text
                db_ics[name] = [usd[32:39], eur[-14:-7]]

        return db_ics

    # def get_data(self):
    #     return self.data