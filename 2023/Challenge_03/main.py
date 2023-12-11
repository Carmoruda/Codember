import pyautogui as pg
import time as tm


def sol():
    final_string = ""
    file_keys = []
    final_keys = []
    result = 0

    file_text = open("encryption_policies.txt", "r", encoding="utf-8").read().split('\n')

    for line in file_text:
        file_keys.append(line.split())

    for line in file_keys:
        line[0] = line[0].split('-')
        line[1] = line[1][0]

        min_count = int(line[0][0])
        max_count = int(line[0][1])

        letter_count = line[2].count(line[1])

        if min_count > letter_count or max_count < letter_count:
            final_keys.append(line[2])

    return final_keys[41]


if __name__ == "__main__":
    tm.sleep(5)
    pg.typewrite("submit " + sol())