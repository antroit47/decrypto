import support

def encrypt(text, key):
    forbidden = [" ", ",", ".", "!", "?", ":", "/", "1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "0"]
    final = ""
    key = key.lower()
    if len(key) == 0:
        print("invalid key")
        return False
    for keychar in key:
        if keychar in forbidden:
            print("invalid key")
            return False

    iterator = 0
    for char in text.lower():
        if iterator >= len(key):
            iterator = 0
        if char in forbidden:
            final += char
            iterator += 1
            continue
        char = chr(((( (ord(char)-97) + ord(key[iterator])-97 ))%26)+97)
        final += char
        iterator += 1
    #print(final)
    return final

def decrypt(text, key):
    forbidden = [" ", ",", ".", "!", "?", ":", "/", "1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "0"]
    key = key.lower()
    for keychar in key:
        if keychar in forbidden:
            print("invalid key")
            return False
    iterator = 0
    final = ""
    for char in text.lower():
        if iterator >= len(key):
            iterator = 0
        if char in forbidden:
            final += char
            iterator += 1
            continue
        if (ord(char) - ord(key[iterator])) < 0:
            result = ord(char) - ord(key[iterator]) + 26
        else:
            result = ord(char) - ord(key[iterator])

        #print(char, key[iterator], result + 97)
        char = chr(result + 97)
        final += char
        iterator += 1
    # print(final)
    return final