import cv2

def get_divided_symbols(image_file: str):
    image = cv2.imread(image_file)
    result = image.copy()

    # переводить зображення в чорнобілий формат
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # переводить кожен піксель який темніший за 0 в колір cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    # це дає можливість відслідкувати малі помітки які можуть бути важливими при розпізнанні символів
    # а те що світліше в 255 - білий
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # знаходить контури для кожного символа тексту
    # параметри (картинка, режим групування, режим упакування)
    # cv2.RETR_EXTERNAL - видає лише зовнішні контури символа
    # cv2.CHAIN_APPROX_SIMPLE - склеєює всі горизонтальні, вертикальні і діагональні контури
    # контури це список всіх найдених контурів, який представляється в вигляді вектора
    changed, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color_line = (34, 139, 34)
    width_line = 1
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(result, (x, y), (x + w, y + h), color_line, width_line)

    cv2.imshow('Image', image)
    cv2.imshow('Gray', gray)
    cv2.imshow('Thresh', thresh)
    cv2.imshow('Divided', result)

    cv2.waitKey()

