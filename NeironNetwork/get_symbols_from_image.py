import cv2
import numpy as np
import os
from pathlib import Path

def get_symbols_from_image(image_file: str):
    letters = []
    out_size = 28
    image = cv2.imread(image_file,cv2.IMREAD_COLOR)
    result = image.copy()
    

    # переводить зображення в чорнобілий формат
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # переводить кожен піксель який темніший за 0 в колір cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    # це дає можливість відслідкувати малі помітки які можуть бути важливими при розпізнанні символів
    # а те що світліше в 255 - білий
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)
    # знаходить контури для кожного символа тексту
    # параметри (картинка, режим групування, режим упакування)
    # cv2.RETR_EXTERNAL - видає лише зовнішні контури символа
    # cv2.CHAIN_APPROX_SIMPLE - склеєює всі горизонтальні, вертикальні і діагональні контури
    # контури це список всіх найдених контурів, який представляється в вигляді вектора
    contours, hierarchy = cv2.findContours(img_erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color_line = (34, 139, 34)
    width_line = 1
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(result, (x, y), (x + w, y + h), color_line, width_line)
        letter_crop = gray[y:y + h, x:x + w]
        max_size = max(w, h)
        letter_square = 255 * np.ones(shape=[max_size, max_size], dtype=np.uint8)
        if w > h:
            y_square = max_size // 2 - h // 2
            letter_square[y_square:y_square + h, 0:w] = letter_crop
        elif w < h:
            x_square = max_size // 2 - w // 2
            letter_square[0:h, x_square:x_square + w] = letter_crop
        else:
            letter_square = letter_crop
        letters.append((x, w, cv2.resize(letter_square, (out_size, out_size), interpolation=cv2.INTER_AREA)))
    letters.sort(key=lambda x: x[0], reverse=False)

    #for i in range(0, len(letters)):
        #cv2.imwrite(f'symbols/{i}.png', letters[i][2])
        #cv2.imshow(f'symbols/{i}.png', letters[i][2])
    #cv2.imshow('Image', image)
    #cv2.imwrite('examples/Gray.png', gray)
    #cv2.imwrite('examples/Thresh.png', thresh)
    #cv2.imshow('Erode', img_erode)
    #cv2.imwrite('examples/Divided.png', result)
    #cv2.waitKey()
    return letters

#get_symbols_from_image('images/apple_handwriten.png')
#letter_square = 255 * np.ones(shape=[28, 28], dtype=np.uint8)
#cv2.imwrite('examples/white.png', letter_square)