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
        db_pegast = {}
        company_name = 'Pegast'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        rates = soup.findAll('script')[4].contents[0].split(',')
        usd = rates[14][7:12]
        euro = rates[23][7:12]

        ''' данные парсились 21.02, курс был 91.9 (с одним знаком после запятой), 
            поэтому в качестве последнего символа выступает '}' кодом ниже мы 
            заменяем '}' на символ '0'. Если у нас курс будет иметь два значка после 
            запятой мы его не отрежем теперь.'''

        if '}' in euro:
            euro = euro.replace('}', '0')

        db_pegast[company_name] = [float(usd), float(euro)]

        return db_pegast
