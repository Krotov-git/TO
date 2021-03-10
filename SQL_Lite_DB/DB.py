import sqlite3
from Parsing.Common_parsing import Common_Parser
from datetime import date

class DataBase:
    def __init__(self):
        self.info = []
        self.db_TO = {}
        self.date = date.today()

    def set_values_TO(self):

        connection = sqlite3.connect("SQL_Lite_DB/database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM spisok_TO")
        rows = cursor.fetchall()
        now_date = str(self.date)
        #print('now_date==> ', now_date)
        self.spisok_table_date = []
        self.spisok_now_date = []

        for row in rows:
            self.table_date = row[3]
            #print('table_date==> ', table_date)
            self.spisok_table_date.append(self.table_date)
            self.spisok_now_date.append(now_date)

        # print('spisok_table_date==> ', self.spisok_table_date)
        # print('spisok_now_date==> ', self.spisok_now_date)
        # print(self.spisok_now_date != self.spisok_table_date)

        if self.spisok_now_date != self.spisok_table_date:
            j = Common_Parser()
            i = j.get_new_data()
            cursor.execute("DELETE FROM spisok_TO")
            for item in i.items():
                self.info.append(item[0])
                self.info.append(item[1][0])
                self.info.append(item[1][1])
                self.info.append(self.date)

                query = "INSERT into spisok_TO(Names_ТО, USD, EUR, DataTime) values (?, ?, ?, ?)"
                cursor.execute(query, self.info)
                connection.commit()
                self.info.clear()

        cursor.close()
        connection.close()

    def get_values_TO(self):
        connection = sqlite3.connect("SQL_Lite_DB/database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM spisok_TO")
        rows = cursor.fetchall()

        for row in rows:
            self.db_TO[row[0]] = [row[1], row[2], row[3]]

        cursor.close()
        connection.close()

        return self.db_TO



if __name__ == '__main__':
    DaBa = DataBase()
    # CP = Common_Parser()
    # i = CP.get_new_data()
    #Test = {'TezTours': ['75.30', '90.70'], 'AnexTours': ['75.63', '91.17'], 'ICS': ['75.631', '91.16'], 'BiblioGlobus': ['75.63', '91.17'], 'Pegast': ['75.63', '91.171'], 'Tui': ['75.7 ', '91.2 '], 'Intourist': ['75.6311', '91.1657'], 'Panteon': ['75.6311', '91.1657']}
    DaBa.set_values_TO()
    DaBa.get_values_TO()
    print('return!', DaBa.get_values_TO())



