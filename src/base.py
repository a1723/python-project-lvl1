import sqlite3


def inserting_into_db(player_name, game_name, true_answers):
    try:
       #db connection
      conn = sqlite3.connect("sqlite_python.db")

      #object for work with base
      cursor = conn.cursor()
      print("База данных подключена к SQLite")         

      #creating table
      creating_table_query = (
         """CREATE TABLE IF NOT EXISTS games             
         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         player_name text, 
         game_name text,
         true_answers INTEGER)
         """
      )
      cursor.execute(creating_table_query)

      # Вставляем данные в таблицу
      data = (player_name, game_name, true_answers)
      sqlite_inserting = ("""INSERT INTO games (player_name, game_name, true_answers)
      VALUES (?, ?, ?)
      """)
      cursor.execute(sqlite_inserting, data)
      conn.commit()
      print("Запись успешно вставлена ​​в таблицу")
      cursor.close()

    except sqlite3.Error as error:
       print("Failed to insert variables into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")