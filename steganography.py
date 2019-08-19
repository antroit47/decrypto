import support
from PIL import Image


def steg1bit_encrypt(message, image_name):
    #only works for 24 bit deph images
    message = message[::-1]
    im = Image.open(image_name)
    pixels = im.getdata()
    width, height = im.size
    #print(width, height)
    im.close()
    newpixels = []
    message_pointer = 0
    #COUNTER = 0
    mess_over = False
    mess_len = len(message)
    for pixel in pixels:
        newcolors = []
        for color in pixel:
            #COUNTER += 1
            if mess_over:
                bin_pix = support.inscribe_1bit(color, "0")
            else:
                bin_pix = support.inscribe_1bit(color, message[message_pointer])
            message_pointer += 1
            newcolors.append(bin_pix)

            if message_pointer >= mess_len:
                mess_over = True
        newcolors = tuple(newcolors)
        newpixels.append(newcolors)
    final_image = Image.new("RGB", (width, height), (0, 0, 0))
    final_image.putdata(newpixels)
    final_image.save("encrypted.png")
    final_image.close()
    #print(COUNTER)


def steg1bit_decrypt(filename):
    #only works for 24 bit deph images
    im = Image.open(filename)
    pixels = im.getdata()
    im.close()
    message = ""
    zerocount = 0
    for pixel in pixels:
        stopflag = False
        for color in pixel:
            bit = support.get_lastbit(color)
            message += bit
            if bit == "0":
                zerocount += 1
            else:
                zerocount = 0
            if zerocount == 20:
                message = message[:-20]
                stopflag = True
                break
        if stopflag:
            break
    message = message[::-1]
    return message


def steg2bit_encrypt(message, image_name):
    #works for all bit deph images
    """
    saves message into the 2 least significant bits in reverse form
    :param message:
    :param image_name:
    :return:
    """
    if len(message) % 2 == 1:
        message = "0" + message
    message = message[::-1]
    im = Image.open(image_name)
    pixels = im.getdata()
    width, height = im.size
    im.close()
    newpixels = []
    message_pointer = 0
    mess_over = False
    mess_len = len(message)
    for pixel in pixels:
        newcolors = []
        for color in pixel:
            if mess_over:
                bin_pix = support.inscribe_2bit(color, "00")
            else:
                bin_pix = support.inscribe_2bit(color, message[message_pointer]+message[message_pointer+1])
            message_pointer += 2
            newcolors.append(bin_pix)
            if message_pointer >= mess_len:
                mess_over = True
        newcolors = tuple(newcolors)
        newpixels.append(newcolors)

    newBD = 0
    for color in pixels[0]:
        newBD += 1

    newtuple = tuple([0]*newBD)
    final_image = Image.new("RGB", (width, height), newtuple)
    final_image.putdata(newpixels)
    final_image.save("encrypted.png")
    final_image.close()


def steg2bit_decrypt(filename):
    """ works for all bit depths
    decrypts message form least significant 2 bits in reverse
    :param filename:
    :return:
    """
    im = Image.open(filename)
    pixels = im.getdata()
    im.close()
    message = ""
    zerocount = 0
    for pixel in pixels:
        stopflag = False
        for color in pixel:
            bits = support.get_last2bit(color)
            message += bits
            if bits == "00":
                zerocount += 1
            else:
                zerocount = 0
            if zerocount == 1000:
                stopflag = True
                break
        if stopflag:
            break
    message = message[::-1]
    for digit in message:
        if digit == "0":
            message = message[1:]
        else:
            break
    return message


def analski_kowalzsis_text(image, message):
    """
    analyses and compares image and a message
    :param image:
    :param message:
    :return:
    """
    im = Image.open(image)
    width, height = im.size
    im.close()
    print("image size: ", width * height)
    print("1 bit steg: ", (width * height * 3))
    print("2 bit steg: ", (width * height * 3)*2)
    print("message length: ", len(message))
    if len(message) <= (width*height*3):
        print("message fits into 1 bit steg")
    if len(message) <= (width*height*3)*2:
        print("message fits into 2 bit steg")
    else:
        print("message does not fit")

def msg_1bit_kowalzsis(image, message):
    im = Image.open(image)
    width, height = im.size
    pixels1 = im.getdata()
    im.close()

    BDcount = 0
    for color in pixels1[0]:
        BDcount += 1
    print("Image bit depth:",BDcount,"(",BDcount*8,")")
    if BDcount != 3:
        print("Wrong bitdepth - select another image")
        return False
    else:
        print("message length: ", len(message),"; image capacity: ",(width * height * 3))
        return(len(message) <= (width*height*3))
        


def analski_kowalzsis_image(image, image_enc):
    """                     storing img,  secret message
    analyses and compares 2 images
    :param image:
    :param image_enc:
    :return:
    """
    im = Image.open(image)
    width1, height1 = im.size
    pixels1 = im.getdata()
    im.close()
    im2 = Image.open(image_enc)
    width2, height2 = im2.size
    pixels2 = im2.getdata()
    im2.close()

    print("image size (",width1,"x",height1,"):", width1 * height1)
    BDcount = 0
    for color in pixels1[0]:
        BDcount += 1
    print("Image bit depth:",BDcount,"(",BDcount*8,")")

    print("1 bit steg: ", (width1 * height1)*BDcount)
    print("2 bit steg: ", (width1 * height1)*BDcount*2)

    BDcount2 = 0
    for color2 in pixels2[0]:
        BDcount2 += 1
    print("Secret bit depth:",BDcount2,"(",BDcount2*8,")")
    print("Message length(",width2,"x",height2,"):", width2*height2*BDcount2*8)

    if width2*height2 <= (width1*height1)*3:
        print("message fits into 1 bit steg")
    if width2*height2 <= (width1*height1)*6:
        print("message fits into 2 bit steg")
    else:
        print("message does not fit")


def steg_encrypt_image(source, secret):
    im = Image.open(secret)
    pixels = im.getdata()
    #width, height = im.size
    #print("secret image size: ", width, height)
    im.close()
    message = ""
    #test_pixel_count = 0
    #test_color_count = 0
    for pixel in pixels:
        #test_pixel_count += 1
        #colorscount = 0
        for color in pixel:
            #colorscount += 1
            #print(colorscount, support.numbertobinary(color))
            message += support.numbertobinary(color)
            #test_color_count += 1

        #print(colorscount)
    #print(test_pixel_count)    #the amount of pixels is correct
    #print(test_color_count)

    #print(len(message))
    steg2bit_encrypt(message, source)


def steg_decrypt_image(image, x, y, BDsecret): #size of secret picture, bit depth of secret
    message = steg2bit_decrypt(image)
    message = [message [i:i+8] for i in range(0, len(message), 8)]
    #splicing message into 8bit pieces
    newpixels = []
    message_pointer = 0

    print("pocet pixelu zpravy ", len(message)//3)
    for i in range(x*y):
        newcolors = []
        for _ in range(BDsecret//8):
            newcolors.append(int(message[message_pointer], 2))
            message_pointer += 1
        newcolors = tuple(newcolors)
        newpixels.append(newcolors)


    newtuple = tuple([0] * (BDsecret//8))
    if (BDsecret//8) == 3:
        print("secret is rgb")
        final_image = Image.new("RGB", (x, y), newtuple)
    elif (BDsecret // 8) == 4:
        print("secret is cmyk")
        final_image = Image.new("RGBA", (x, y), newtuple)
    else:
        print("INVALID BIT DEPTH, CHOSE 24/32")
        return

    final_image.putdata(newpixels)
    final_image.save("secret_image.png")
    final_image.close()


def same_images_test(img1, img2):   #images have to be the same size
    im = Image.open(img1)
    pixels1 = im.getdata()
    im.close()
    
    im2 = Image.open(img2)
    pixels2 = im2.getdata()
    im2.close()

    #print("XXXXXXX", pixels1[0][3])
    #print("XXXXXXX", pixels2[0][3])

    diff = False
    pixcount = 0
    for pixel in pixels1:
        colorcount = 0
        for color in pixel:
            #print(pixcount, colorcount)
            if color != pixels2[pixcount][colorcount]:
                diff = True
                #print("BR")
                print(color, pixels2[pixcount][colorcount], pixcount,
                      colorcount)

                break
            colorcount += 1
        if diff:

            print("DIFF")
            print(color, pixels2[pixcount][colorcount], pixcount, colorcount)
            return
        pixcount += 1
    print("SAME")


# TODO XXXXXXXXXXXXXXXXXX
def stegano_last1bit(original, encrypted):
    """
    TODO XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    not really working function to visualize the difference in pictures -
    could be better with 2 bits

    :param original:
    :param encrypted:
    :return:
    """
    im = Image.open(original)
    o_pixels = im.getdata()
    width, height = im.size
    im.close()

    new_o_pixels = find_last_bit_map(o_pixels)

    o_final_image = Image.new("RGB", (width, height), (0, 0, 0))
    o_final_image.putdata(new_o_pixels)
    o_final_image.save("lastbit_orig.png")
    o_final_image.close()

    im = Image.open(encrypted)
    e_pixels = im.getdata()
    im.close()

    new_e_pixels = find_last_bit_map(e_pixels)

    e_final_image = Image.new("RGB", (width, height), (0, 0, 0))
    e_final_image.putdata(new_e_pixels)
    e_final_image.save("lastbit_encrypted.png")
    e_final_image.close()


# TODO XXXXXXXXXXXXXXXXXXXXXXXXX
def find_last_bit_map(pixels):
    """
    TODO incomplete kinda / no purpose for 1 bit encrypt / 2 bit maybe?
    :param pixels:
    :return:
    """
    new_o_pixels = []
    for pixel in pixels:
        newcolor = []
        for color in pixel:
            if support.get_lastbit(color) == "1":
                newcolor.append(255)
            else:
                newcolor.append(0)
        newcolor = tuple(newcolor)
        new_o_pixels.append(newcolor)
    return new_o_pixels
