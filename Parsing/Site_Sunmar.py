# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class Sunmar:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://tour-kassa.ru/%D0%BA%D1%83%D1%80%D1%81%D1%8B-%D0%B2%D0%B0%D0%BB%D1%8E%D1%82-%D1%82%D1%83%D1%80%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_sunmar = {}

        i = 0
        for tr in trs[0]:
            i += 1

            if i == 28:
                tds = tr.findAll("td")
                name = 'Sunmar'
                usd = tds[4].text
                eur = tds[1].text
                db_sunmar[name] = [usd, eur]
        #print(db_sunmar)
        return db_sunmar


if __name__ == '__main__':
    pars = Sunmar()
