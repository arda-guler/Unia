import os
import random
from PIL import Image

path_letters = "letters"
letter_size = 64

def init():
    global path_letters
    img_letters = os.listdir(path_letters)
    dict_letters = {}

    for img_letter in img_letters:
        if not img_letter[0] in dict_letters:
            dict_letters[img_letter[0]] = [img_letter]
        else:
            dict_letters[img_letter[0]].append(img_letter)

    return dict_letters

def get_input_str():
    return input("Please enter the string to convert:")

def main():
    d_letters = init()

    while True:
        str_original = get_input_str().upper()
        if str_original == "":
            return
        
        str_converted = []

        for char in str_original:
            if char == " ":
                char_img = "special/SPACE.png"
            else:
                char_img = path_letters + "/" + random.choice(d_letters[char])
                
            str_converted.append(char_img)

        y_size = letter_size
        x_size = letter_size * len(str_converted)
        img_output = Image.new('RGBA', (x_size, y_size), color="white")
        
        index_coord = 0
        for char_img in str_converted:
            img_output.paste(Image.open(char_img), (index_coord, 0))
            index_coord += letter_size

        img_output.save("output/" + str_original + ".png")

main()
