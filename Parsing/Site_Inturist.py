import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class Inturist:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://intourist.ru/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        divs = soup.findChildren("div", "footer__rate")
        # print(divs)

        db_inturist = {}

        usd1 = divs[0].text
        usd2 = usd1[-30:-23]
        #         print('usd==> ', usd1)
        #         print('usd==> ', usd2)
        eur1 = divs[0].text
        eur2 = eur1[-11:-4]
        #         print('eur==> ', eur1)
        #         print('eur==> ', eur2)
        name = 'Intourist'
        db_inturist[name] = [usd2, eur2]
        #print(db_inturist)
        return db_inturist


if __name__ == '__main__':
    pars = Inturist()