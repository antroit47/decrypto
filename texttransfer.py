import support

def is_ascii(text):
    for letter in text:
        if (ord(letter) > 127) or (ord(letter) < 32):
            print("character:", letter, "is not encodable - abandoning")
            return False
    return True
    

def ascii_to_bits(text):
    if not is_ascii(text):
        print("procedure ascii to bits failed")
        return False
    message = ""
    for letter in text:
        #print(ord(letter))
        message += support.numbertobinary(ord(letter))
        #print(support.numbertobinary(ord(letter)))
    #print(message)
    return message


def bits_to_ascii(text):
    #print(len(text))
    msg_pointer = len(text)
    message = ""
    while msg_pointer > 0:
        if msg_pointer - 8 < 0:
            #print(msg_pointer)
            final = text[0:msg_pointer]
            while 8-msg_pointer != 0:
                final = "0" + final
                msg_pointer += 1
            message = chr(support.bintodec(final)) + message
            break
        #print (text[msg_pointer:msg_pointer+8])
        message = chr(support.bintodec(text[msg_pointer-8:msg_pointer])) + message
        msg_pointer = msg_pointer - 8
        
    #print(message)
    return message


    
