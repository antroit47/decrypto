import support


def encrypt(text, step):
    final = ""
    for char in text.lower():
        if char in [" ", ",", ".", "!", "?", ":", "/", "1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "0"]:
            final += char
            continue
        char = chr((((ord(char)+step)-97)%26)+97)
        final += char
    #print(final)
    return final

def decrypt(text, step):
    return encrypt(text, -step)


def decrypt_smart(text):
    options = {}
    for i in range(26):
        options[(encrypt(text, i))] = 0
    #print(options)
    for option in options:
        options[option] = support.islegit(option)
    options = sorted(options.items(), key=lambda kv: kv[1])
    #print(options)
    return options

def select_best(options):
    return options[0][0]
