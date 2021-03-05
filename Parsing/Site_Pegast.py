import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class Pegast:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://pegast.ru/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        rates = soup.findAll('script')[4].contents[0].split(',')
        #print('rates ==> ', rates)

        db_pegast = {}

        usd = rates[13][-6:-1]
        #print('usd ==> ', usd)
        euro = rates[22][-14:-8]
        #print('euro ==> ', euro)

        if '}' in euro:
            euro = euro.replace('}', '1')

        name = 'Pegast'
        db_pegast[name] = [usd, euro]
        #print(db_pegast)
        return db_pegast


if __name__ == '__main__':
    pars = Pegast()