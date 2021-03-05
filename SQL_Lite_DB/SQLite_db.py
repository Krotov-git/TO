import sqlite3

connection = sqlite3.connect("database1.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS spisok_TO")
cursor.execute("""CREATE TABLE IF NOT EXISTS spisok_TO
                   (Names_ТО TEXT,
                    USD REAL,
                    EUR REAL);
                   """)
# anextours = [('Test1', '71', '91')]
#
# query = "INSERT into spisok_TO values (?, ?, ?)"
# cursor.executemany(query, anextours)

connection.commit()

with connection:
     cursor = connection.cursor()
     cursor.execute("SELECT * FROM spisok_TO")

     while True:
         row = cursor.fetchone()
         if row == None:
             break
         print(row[0], row[1], row[2])
