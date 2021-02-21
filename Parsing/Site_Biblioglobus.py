import requests
from bs4 import BeautifulSoup


# создаю класс для парсинга данных с сайта
class Biblioglobus:
    # задаю атрибуты класса
    def __init__(self):
        self.site = 'https://www.bgoperator.ru/'
        self.data = self.parse_site()

    # функция осуществляющая непосредственный парсинг данных с сайта
    def parse_site(self):
        db_globus = {}
        company_name = 'Biblio Globus'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

        response = requests.get(self.site, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        rates = soup.findAll('script').pop(0).contents[0].split(';')[7][35:47].split(',')

        db_globus[company_name] = [float(rates[0]), float(rates[1])]

        return db_globus