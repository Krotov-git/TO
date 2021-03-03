# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class ICS:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://www.icstrvl.ru/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_ics = {}

        f = 0
        for tr in trs[0]:
            f += 1
            if f == 8:
                tds = tr.findAll("td")

                usd1 = tds[3].text
                usd2 = usd1[31:37]
                if ',' in usd2:
                    usd2 = usd2.replace(',', '.')

                eur1 = tds[3].text
                eur2 = eur1[-14:-9]
                if ',' in eur2:
                    eur2 = eur2.replace(',', '.')

                name = 'ICS'
                db_ics[name] = [usd2, eur2]

        #print(db_ics)
        return db_ics


if __name__ == '__main__':
    pars = ICS()
