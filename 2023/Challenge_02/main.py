import pyautogui as pg
import time as tm


def sol():
    final_string = ""
    result = 0

    file_text = list(open("message_02.txt", "r", encoding="utf-8").read())

    for character in file_text:
        match character:
            case '#':
                result += 1
            case '@':
                result -= 1
            case '*':
                result *= result
            case '&':
                final_string += str(result)

    return final_string


if __name__ == "__main__":
    tm.sleep(5)
    pg.typewrite("submit " + sol())
