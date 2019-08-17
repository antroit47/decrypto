

def isvowel(letter):
    """
    checks if the letter is vowel
    :param letter:
    :return: true/false
    """
    if letter in ["a","e","i","o","u","y"]:
        return True
    return False


def islegit(text):
    words = text.split()
    """
    counts valid sentence score based on vowels
    :param text: to be verified 
    :return: score: value based on repeating vowels
    """
    score = 0
    for word in words:
        word = word.strip()
        multiplyer = 0
        lastletterwasvowel = True
        for letter in word:
            if letter in [" ", ",", ".", "!", "?", ":", "/"]:
                continue
            thisletterisvowel = isvowel(letter)
            if lastletterwasvowel == thisletterisvowel:
                multiplyer += 1
            else:
                multiplyer = 0
            score += multiplyer
            lastletterwasvowel = thisletterisvowel
    return score


def inscribe_1bit(number, bit):
    if bit == "0":
        if number % 2 == 1:
            number -= 1
    else:
        if number % 2 == 0:
            number += 1
    return number


def get_lastbit(number):
    if number % 2 == 0:
        return "0"
    return "1"


def inscribe_2bit(number, bit):
    if bit == "00":
        if number % 4 == 0:
            return number
        if number % 4 == 1:
            return number-1
        if number % 4 == 2:
            return number-2
        if number % 4 == 3:
            return number-3
    elif bit == "01":
        if number % 4 == 0:
            return number+1
        if number % 4 == 1:
            return number
        if number % 4 == 2:
            return number-1
        if number % 4 == 3:
            return number-2
    elif bit == "10":
        if number % 4 == 0:
            return number+2
        if number % 4 == 1:
            return number+1
        if number % 4 == 2:
            return number
        if number % 4 == 3:
            return number-1
    else:
        if number % 4 == 0:
            return number+3
        if number % 4 == 1:
            return number+2
        if number % 4 == 2:
            return number+1
        if number % 4 == 3:
            return number


def get_last2bit(number):
    if number % 4 == 0:
        return "00"
    elif number % 4 == 1:
        return "01"
    elif number % 4 == 2:
        return "10"
    elif number % 4 == 3:
        return "11"


def numbertobinary(number): #number is string of 001010
    return '{0:08b}'.format(number)

def bintodec(number):
    return int(number, 2)
