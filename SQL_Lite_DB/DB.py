import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

class DataBase:
    def __init__(self):
        self.info = []

    def set_info(self, value1, value2, value3):
        self.info.append(value1)
        self.info.append(value2)
        self.info.append(value3)


    def get_info(self):
        return self.info

    def insert_info_db(self):  # связывется с дб и вносит в таблицу ои данные, открыть бд вставить данные закрыть бд
        query = "INSERT into spisok_TO(Names_ТО, USD, EUR) values (?, ?, ?)"
        cursor.execute(query, self.info)
        connection.commit()
        self.info.clear()

    def get_from_db(self):     # спомощью селект получить данные из таблицы. преобразовать данныев нужный вид
        cursor.execute("SELECT * FROM spisok_TO")
        rows = cursor.fetchall()
        #for row in rows:
            #print("{0} {1} {2}".format(row[0], row[1], row[2]))
        return rows
        connection.commit()

if __name__ == '__main__':
    DB = DataBase()
    DB.set_info('TezTours', '75', '92')
    DB.insert_info_db()
    DB.set_info('ICS', '72', '95')
    DB.insert_info_db()
    print('вывожу данные из БД', DB.get_from_db())


























# # создаю класс для парсинга данных с сайта
# class DataBase:
#
#     # задаю атрибуты класса
#     def __init__(self):
#        # self.site = 'https://pay.travel/site_controller_courses/index/?date='
#         self.site = 'https://www.tez-tour.com/'
#         self.data = self.parse_site()
#
#     # функция осуществляющая непосредственный парсинг данных с сайта
#     def parse_site(self):
#         # now = datetime.datetime.now()
#         # date = now.strftime("%Y-%m-%d")
#         #site = self.site + date
#         site = 'https://www.tez-tour.com/'
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
#         }
#
#         response = requests.get(site, headers=headers)
#         soup = BeautifulSoup(response.text, features='lxml')
#         trs = soup.findChildren("table")
#
#         # создаю саму базу данных по типу словаря где ключ название туроператора, а курс значение ключа
#         db = {}
#         i = 0
#         for tr in trs[2]:
#             i += 1
#             if i == 4:
#                 tds = tr.findAll("td")
#                 name = 'TezTour'
#                 usd = tds[1].text
#                 eur = tds[2].text
#                 db[name] = [usd[:-3], eur[:-3]]
#
#         return db
#
#     def get_data(self):
#         return self.data


