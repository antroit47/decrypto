import support
from PIL import Image
import os

"This whole set of functions works well with 24 bit depth images. " \
"Anything else than that could fail horribly"


def steg1bit_encrypt(message, image_name):
    """
    encrypts message into last 1 bit - in reverse form so themessage is 101000000
    :param message: message in bits string
    :param image_name: name of image in .jpg - has to be 24 bit depth
    :return: nothing - creates an image with message encrypted
    """
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
    """
    decrypts message from last 1 bits of image
    :param filename:  image name - .jpg - should be 24 bit depth
    :return: message - string in bits
    """
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
    """ works for all bit depths - maybe :D
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
    analyses and compares image and a message and tells if it fits
    :param image:
    :param message:
    :return: nothing - gives printed information about situation
    """
    im = Image.open(image)
    width, height = im.size
    im.close()
    print("image size: ", width * height)
    print("1 bit steg: ", (width * height * 3))
    print("2 bit steg: ", (width * height * 3)*2)
    print("message length: ", len(message))
    if len(message*7) <= (width*height*3):
        print("message fits into 1 bit steg")
    if len(message*4) <= (width*height*3)*2:
        print("message fits into 2 bit steg")
    else:
        print("message does not fit")

def msg_1bit_kowalzsis(image, message):
    """
    checks if message fits into one bit steg, also gives written feedback and
    also checks for correct bit depth
    :param image:
    :param message:
    :return: true/false
    """
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
        return(len(message*7) <= (width*height*3))
        


def analski_kowalzsis_image(image, image_enc):
    """analyses *image* and checks is *image_enc* fits into it
    :param image: bigger image - to store
    :param image_enc: smaller image - the secret
    :return: nothing - prints results
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
    for _ in pixels1[0]:
        BDcount += 1
    print("Image bit depth:",BDcount,"(",BDcount*8,")")

    print("1 bit steg: ", (width1 * height1)*BDcount)
    print("2 bit steg: ", (width1 * height1)*BDcount*2)

    BDcount2 = 0
    for _ in pixels2[0]:
        BDcount2 += 1
    print("Secret bit depth:",BDcount2,"(",BDcount2*8,")")
    print("Message length(",width2,"x",height2,"):", width2*height2*BDcount2*8)

    if width2*height2 <= (width1*height1)*3:
        print("message fits into 1 bit steg")
    if width2*height2 <= (width1*height1)*6:
        print("message fits into 2 bit steg")
    else:
        print("message does not fit")


def image_2bit_kowalzsis(image, image_enc):
    """
    checks if image fits into two bit steg, also gives written feedback and
    also checks for correct bit depth
    :param image: bigger store image
    :param image_enc: smaller secret image
    :return: true/false
    """
    im = Image.open(image)
    width1, height1 = im.size
    pixels1 = im.getdata()
    im.close()
    im2 = Image.open(image_enc)
    width2, height2 = im2.size
    pixels2 = im2.getdata()
    im2.close()

    BDcount1 = 0
    for color in pixels1[0]:
        BDcount1 += 1
    print("Base image bit depth:",BDcount1,"(",BDcount1*8,")")

    BDcount2 = 0
    for color2 in pixels2[0]:
        BDcount2 += 1
    print("Secret bit depth:",BDcount2,"(",BDcount2*8,")")
                     #
    if BDcount1 != 3 or BDcount2 != 3:  #removing this will produce strange pictures
        print("Wrong bitdepth - select another image")
        return False

    if width2*height2*8 > (width1*height1)*6:
        print("message does not fit into 2 bit steg")
        return False
    print("secret image resolution:  ", width2, " x ", height2)
    return True


def image_inimage_kowalzsis(image, resolution):
    """
    Applied when trying to decode an image from an image based on secret image resolution
    :param image: source image
    :param resolution: resolution of a secret image
    :return: true/false
    """
    im = Image.open(image)
    width1, height1 = im.size
    pixels1 = im.getdata()
    im.close()

    BDcount1 = 0
    for color in pixels1[0]:
        BDcount1 += 1
    print("Base image bit depth:",BDcount1,"(",BDcount1*8,")")

    if BDcount1 != 3:
        print("Wrong bitdepth - select another image")
        return False

    if resolution*8 > (width1*height1)*6:
        print("message does not fit into 2 bit steg")
        return False
    return True        

def steg_encrypt_image(source, secret):
    """
    encrypts *secret* image into *source* image
    :param source:
    :param secret:
    :return: creates new image
    """
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


def steg_decrypt_image(image, x, y, BDsecret): #, bit depth of secret
    """
    decrypts secret image out of an image - DONT use any BDsecret except 24
    :param image:
    :param x: size of secret picture
    :param y: size of secret picture
    :param BDsecret: bit depth of secret image (24/32)
    :return:
    """
    message = steg2bit_decrypt(image)
    message = [message [i:i+8] for i in range(0, len(message), 8)]
    #splicing message into 8bit pieces
    newpixels = []
    message_pointer = 0

    #print("pocet pixelu zpravy ", len(message)//3)
    for i in range(x*y):
        newcolors = []
        for _ in range(BDsecret//8):
            newcolors.append(int(message[message_pointer], 2))
            message_pointer += 1
        newcolors = tuple(newcolors)
        newpixels.append(newcolors)


    newtuple = tuple([0] * (BDsecret//8))
    if (BDsecret//8) == 3:
        #print("secret is rgb")
        final_image = Image.new("RGB", (x, y), newtuple)
    elif (BDsecret // 8) == 4:
        #print("secret is cmyk")
        final_image = Image.new("RGBA", (x, y), newtuple)
    else:
        #print("INVALID BIT DEPTH, CHOSE 24/32")
        return

    final_image.putdata(newpixels)
    final_image.save("secret_image.png")
    final_image.close()


def same_images_test(img1, img2):   #images have to be the same size
    """
    checks if two images are exactly the same.
    :param img1:
    :param img2:
    :return: true/false
    """
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
            return False
        pixcount += 1
    print("SAME")
    return True


def createFolder(directory):
    """
    creates folder
    :param directory: name of the directory
    :return: true/false based on whether the operation was successful
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            return True
    except OSError:
        print('Error: Creating directory. ' + directory)
        return False


def each_color_check_blacknwhite(image):
    """
    Makes image black and white and then it creates 256 images for every shade of grayscale.
    Used for looking for secret patterns in images of same color. The color is represented by white,
    The rest is black.
    :param image:
    :return: creates 256 images
    """
    im = Image.open(image).convert('LA')
    pixels = im.getdata()
    width, height = im.size
    im.close()

    createFolder("blacknwhite_color_check")
    i = 0
    for j in range(256):
        i += 1
        newtitle = "blacknwhite_color_check\\newimage" + str(i) + ".png"
        newpixels = []
        for px in pixels:
            if px[0] == j:
                newpixels.append((255, 255, 255))
            else:
                newpixels.append((0, 0, 0))
        final_image = Image.new("RGB", (width, height), (0, 0, 0))
        final_image.putdata(newpixels)
        final_image.save(newtitle)
        final_image.close()
        print("picture: ", i, " was created")
    print("Done")


def top_pixels_color_check(image, amount_of_imgs):
    """
    takes most common colors in a picture and makes a set of pictures where
    each of these colors is represented by white, the rest is black
    :param image:
    :param amount_of_imgs: max amount of images created
    :return: creates *amount_of_images* images
    """
    im = Image.open(image)
    pixels = im.getdata()
    width, height = im.size
    im.close()
    createFolder("each_color_check")
    individual_colors = {}
    for pixel in pixels:
        if pixel not in individual_colors:
            individual_colors[pixel] = 0
        else:
            individual_colors[pixel] += 1
    individual_colors = sorted(individual_colors.items(), key=lambda kv: kv[1])[::-1]
    i = 0
    for entry in individual_colors[:amount_of_imgs]:
        i += 1
        newtitle = "each_color_check\\newimage" + str(i) + ".png"
        newpixels = []
        for px in pixels:
            if px == entry[0]:
                newpixels.append((255, 255, 255))
            else:
                newpixels.append((0, 0, 0))
        final_image = Image.new("RGB", (width, height), (0, 0, 0))
        final_image.putdata(newpixels)
        final_image.save(newtitle)
        final_image.close()
        print("picture: ", i, " was created")


def stegano_last1bit_diff(original, encrypted):
    """
    function to visualize ANY difference in 2 pictures.
    White indicates the difference
    :param original:
    :param encrypted:
    :return: creates new difference pisture
    """
    im = Image.open(original)
    o_pixels = im.getdata()
    width, height = im.size
    im.close()

    im2 = Image.open(encrypted)
    e_pixels = im2.getdata()
    width2, height2 = im2.size
    im2.close()

    if (width != width2) or (height != height2):
        print("Images have different resolutions. Aborting")
        return

    new_pixels = []
    diff_counter = 0
    for o_pix, e_pix in zip(o_pixels, e_pixels):
        if o_pix == e_pix:
            new_pixels.append((0, 0, 0))
        else:
            new_pixels.append((255, 255, 255))
            diff_counter += 1


    e_final_image = Image.new("RGB", (width, height), (0, 0, 0))
    e_final_image.putdata(new_pixels)
    e_final_image.save("diff_last_1bit.png")
    e_final_image.close()
    print("spotted differences: ", diff_counter)
    total = width*height
    print(" Difference in pictures: ", diff_counter*100/(width*height),"%")


def stegano_last1bit_diff_EXP(original, encrypted):
    """
    function to visualize the difference in 2 pictures.
    the more white the color, the more difference was in the two pictures
    :param original:
    :param encrypted:
    :return: creates new difference pisture
    """
    im = Image.open(original)
    o_pixels = im.getdata()
    width, height = im.size
    im.close()

    im2 = Image.open(encrypted)
    e_pixels = im2.getdata()
    width2, height2 = im2.size
    im2.close()

    if (width != width2) or (height != height2):
        print("Images have different resolutions. Aborting")
        return

    new_pixels = []
    diff_counter = 0
    for o_pix, e_pix in zip(o_pixels, e_pixels):
        if o_pix == e_pix:
            new_pixels.append((0, 0, 0))
        else:

            new_pixels.append((abs(o_pix[0]-e_pix[0]), abs(o_pix[1]-e_pix[1]), abs(o_pix[2]-e_pix[2])))
            diff_counter += 1


    e_final_image = Image.new("RGB", (width, height), (0, 0, 0))
    e_final_image.putdata(new_pixels)
    e_final_image.save("diff_last_1bit.png")
    e_final_image.close()
    print("spotted differences: ", diff_counter)
    total = width*height
    print(" Difference in pictures: ", diff_counter*100/(width*height),"%")