import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE spisok_TO
                   (Names_ТО text, USD real, EUR real);
                   """)

#anextours = [('Test1', '71', '91')]

#query = "INSERT into spisok_TO values (?, ?, ?)"
#cursor.executemany(query, anextours)

connection.commit()

with connection:
     cursor = connection.cursor()
     cursor.execute("SELECT * FROM spisok_TO")

     while True:
         row = cursor.fetchone()
         if row == None:
             break
         print(row[0], row[1], row[2])
