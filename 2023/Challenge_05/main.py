import pyautogui as pg
import time as tm
import re


def sol():
    final_string = ""
    user_information = []
    first_letter_wrong = ""
    result = ""

    file_text = open("database_attacked.txt", "r", encoding="utf-8").read().split('\n')

    for line in file_text:
        user_information.append(line.split(','))

    for user in user_information:
        if (not user[0].isalnum()) or (not user[1].isalnum()) or (not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", user[2])) or (user[3] != "" and user[3].isnumeric() == False) or (user[4] != "" and num_there(user[4]) == True):
            first_letter_wrong += user[1][0]
            continue

    return first_letter_wrong


def num_there(word):
    return any(letter.isdigit() for letter in word)


if __name__ == "__main__":
    tm.sleep(5)
    pg.typewrite("submit " + sol())