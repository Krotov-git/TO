# подгружаю необходимые библиотеки
import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class TUI:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://agent.tui.ru/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0' }

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        trs = soup.findChildren("table")

        # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
        db_tui = {}
        i = 0
        for tr in trs[0]:
            i += 1
            # print(i, '===========================================')
            # print(tr)
            if i == 5:
                tdsE = tr.findAll("td")
                # print('tdsE =', tdsE)
                eur = tdsE[1].text
                # print(eur)
                if ',' in eur:
                    eur = eur.replace(',', '.')

            if i == 7:
                tdsU = tr.findAll("td")
                # print('tdsU =', tdsU)
                usd = tdsU[1].text
                # print(usd)
                if ',' in usd:
                    usd = usd.replace(',', '.')

                name = 'Tui'
                db_tui[name] = [usd[:-1], eur[:-1]]
        #print(db_tui)
        return db_tui


if __name__ == '__main__':
    pars = TUI()
