import sqlite3
# import msvcrt



with sqlite3.connect("file.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS words (eng TEXT UNIQUE NOT NULL DEFAULT 0, rus TEXT NOT NULL DEFAULT 0)""")


def add_new_word(eng_word, rus_word):
    with sqlite3.connect("file.db") as conn:
        cursor = conn.cursor()
        words = [eng_word.lower(), rus_word.lower()]
        cursor.execute("INSERT INTO words (eng, rus) VALUES (?,?)", words)


        # asd = cursor.execute('''SELECT eng FROM words WHERE eng=?''', str(eng_word))
        # print(asd)
        # exists = cursor.fetchall()
        #
        #
        # if not exists:
        #     cursor.execute("INSERT INTO words (eng, rus) VALUES (?,?)", words)
        #     conn.commit()
        #     Successful = "Successful"
        #     return Successful
        # else:
        #     print("Error: words already exist")
        #     Unsuccessful = "unsuccessful"
        #     return Unsuccessful


def rand_word():
    with sqlite3.connect("file.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT eng, rus FROM words ORDER BY RANDOM() LIMIT 1")
        word = cursor.fetchone()

        return word


# def verify_word():
#     while True:
#         word = rand_word()
#         english_word = word[0]
#         russian_word = word[1]
#         print(english_word.capitalize())
#         your_word = input("Введите ваше слово - ")
#         if russian_word == your_word:
#             print("Молодец, Вы знаете это слово", "\n")
#         else:
#             print("Плохо, правильное слово - ", russian_word, "\n")
#         # backk = input("Чтобы продолжить нажмите \"Enter\" \n"
#         #       "Чтобы выйти, введите \"exit\"")
#         # if backk == "exit":
#         #     break
#         # else:
#         #     continue
#         if msvcrt.getch() == b'\x1b':
#             break
#         else:
#             continue



        # return word



# parse = wordfunc.rand_word()
# english_word = parse[0]
# russian_word = parse[1]






