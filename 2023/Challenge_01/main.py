import pyautogui as pg
import time as tm


def sol():
    final_string = ""
    word_dictionary = {}

    file_text = open("message_01.txt", "r", encoding="utf-8").read().split()

    for word in file_text:
        if word not in word_dictionary:
            word_dictionary[word] = file_text.count(word)
            final_string += word + str(word_dictionary[word])

    return final_string


if __name__ == "__main__":
    tm.sleep(5)
    pg.typewrite("submit " + sol())