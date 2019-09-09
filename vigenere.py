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




# TODO 2 moznosti - 1) projit třeba sestimistna hesla, zacit AAAA a menit
# prvni pismena (pokud bude klic kratky tak je to blby) / nebo delat od A po AA po AAA - tohle bude opakovat vicekrat ABAB treba
def decrypt_smart(text, key_len):
    options = {}
    keys = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    if key_len > 5:
        print("key longer than 5 is too long to brute force")
    total = 26 ** key_len

    if key_len > 0:
        for key in keys:
            result = decrypt(text, key)
            options[result] = support.islegit(result)
    if key_len > 1:
        for key1 in keys:
            for key2 in keys:
                key = key1 + key2
                result = decrypt(text, key)
                options[result] = support.islegit(result)
                count += 1
    if key_len > 2:
        for key1 in keys:
            for key2 in keys:
                for key3 in keys:
                    key = key1 + key2 + key3
                    result = decrypt(text, key)
                    options[result] = support.islegit(result)
                    count += 1
                    if not count % 10000:
                        print(count, " / ", total, " iterations tested")
    if key_len > 3:
        for key1 in keys:
            for key2 in keys:
                for key3 in keys:
                    for key4 in keys:
                        key = key1 + key2 + key3 + key4
                        result = decrypt(text, key)
                        options[result] = support.islegit(result)
                        count += 1
                        if not count % 10000:
                            print(count, "/", total, " iterations tested")
    if key_len > 4:
        print("memory error may occur")
        for key1 in keys:
            for key2 in keys:
                for key3 in keys:
                    for key4 in keys:
                        for key5 in keys:
                            key = key1 + key2 + key3 + key4 + key5
                            result = decrypt(text, key)
                            options[result] = support.islegit(result)
                            count += 1
                            if not count % 10000:
                                print(count, "/", total, " iterations tested")

    options = sorted(options.items(), key=lambda kv: kv[1])
    print(options[0:15])
    return options[0:15]
