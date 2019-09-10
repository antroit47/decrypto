import support

def encrypt(text, step):
    """
    Encrypts text with caesar cipher by moving each letter by the amount of
     steps specified in parameter
    :param text: Text to encrypt
    :param step: Encryption key
    :return: Encrypted text as string
    """
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
    """
    Decrypting caesar cipher with known step
    :param text: Encrypted text
    :param step: Key
    :return: Decrypted text
    """
    return encrypt(text, -step)


def decrypt_smart(text):
    """
    Decrypting Caesar cipher without known key. Takes all 26 possible permutations
    the encrypted text could be and tests, which one of them is most likely to be a language.
    Uses function islegit from support module
    :param text: Encrypted text
    :return: Dectypted text
    """
    options = {}
    for i in range(26):
        options[(encrypt(text, i))] = 0
    for option in options:
        options[option] = support.islegit(option)
    options = sorted(options.items(), key=lambda kv: kv[1])
    #print(options)
    return options


def select_best(options):
    """
    Support function which returns most-likely-to-be-language text out of dict
    containing many of these texts
    :param options: Dict of possible real-language texts
    :return: Most likely text
    """
    return options[0][0]
