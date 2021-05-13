import sqlite3

# Собираем список необходимых данных
game_statics = []

#db connection
conn = sqlite3.connect(":memory:")

#object for work with base
cursor = conn.cursor()            

#creating table
cursor.execute("""CREATE TABLE games                        
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  user_name text, 
                  game_name text,
                  true_answers INTEGER,
                  false_answers INTEGER)
               """)


def inserting_into_db(user_name, game_name, true_answers, false_answers):
    # Вставляем данные в таблицу
    cursor.execute("""INSERT INTO games
                  VALUES (user_name, game_name, true_answers, false_answers)"""
               )