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
        f = 0
        for tr in trs[0]:
            f += 1
            #print(i)
            if f == 8:
                #print('here')
                tds = tr.findAll("td")

                name = 'ICS'

                usd1 = tds[3].text
                usd2 = usd1[32:37]

                usd_spisok = []
                for i in range(len(usd2)):
                    #print(i)
                    usd_spisok.append(usd2[i])
                    #print('usd_spisok ==> ', usd_spisok)

                    if usd2[i] == ',':
                        usd_spisok[i] = '.'

                usd_stroka = usd_spisok[0] + usd_spisok[1] + usd_spisok[2] + usd_spisok[3] + usd_spisok[4]
                #print('usd_stroka ==>', usd_stroka)


                eur1 = tds[3].text
                eur2 = eur1[-14:-9]

                eur_spisok = []
                for i in range(len(eur2)):
                    #print(i)
                    eur_spisok.append(eur2[i])
                    #print('eur_spisok ==> ', eur_spisok)

                    if eur2[i] == ',':
                        eur_spisok[i] = '.'

                eur_stroka = eur_spisok[0] + eur_spisok[1] + eur_spisok[2] + eur_spisok[3] + eur_spisok[4]
                #print('eur_stroka ==>', eur_stroka)

                db_ics[name] = [usd_stroka, eur_stroka]
                #print('db_ics ==> ', db_ics)

        return db_ics

if __name__ == '__main__':
    pars = ICS()
    # def get_data(self):
    #     return self.data