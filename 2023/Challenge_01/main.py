if __name__ == "__main__":
    finalString = ""
    wordDictionary = {}

    fileText = open("message_01.txt", "r", encoding="utf-8").read().split()

    for word in fileText:
        if word not in wordDictionary:
            wordDictionary[word] = fileText.count(word)
            finalString += word + str(wordDictionary[word])

    print(finalString)