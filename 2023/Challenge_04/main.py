import pyautogui as pg
import time as tm


def sol():
    final_string = ""
    file_names = []
    correct_file_names = []
    result = ""

    file_text = open("files_quarantine.txt", "r", encoding="utf-8").read().split('\n')

    for line in file_text:
        file_names.append(line.split('-'))

    for word in file_names:
        for letter in word[0]:
            letter_count = word[0].count(letter)
            if letter_count == 1:
                result += letter
        if result == word[1]:
            correct_file_names.append(result)
        result = ""

    return correct_file_names[32]


if __name__ == "__main__":
    tm.sleep(5)
    pg.typewrite("submit " + sol())