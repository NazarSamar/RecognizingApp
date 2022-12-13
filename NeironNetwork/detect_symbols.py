import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from neiron_model import emnist_labels
from get_symbols_from_image import get_symbols_from_image


def get_text_symbol_from_image(model, img):
    out_size = 28
    img_arr = np.expand_dims(img, axis=0)
    img_arr = 1 - img_arr / 255.0
    img_arr[0] = np.rot90(img_arr[0], 3)
    img_arr[0] = np.fliplr(img_arr[0])
    img_arr = img_arr.reshape((1, out_size, out_size, 1))

    result = model.predict([img_arr],verbose=0)
    predicted_class_indices=np.argmax(result,axis=1)
    #print(emnist_labels[0])
    return chr(emnist_labels[predicted_class_indices[0]])


def detect_symbols(model, image_file):
    result = ""
    letters = get_symbols_from_image(image_file)

    for i in range(len(letters)):
        dn = 0
        if i < len(letters) - 1:
            dn = letters[i + 1][0] - letters[i][0] - letters[i][1]
        result += get_text_symbol_from_image(model, letters[i][2])
        if dn > letters[i][1] / 4:
            result += ' '
    return result

def detect_images(model, image_file):
    result = ""
    letters = get_symbols_from_image(image_file)

    for i in range(len(letters)):
        dn = 0
        if i < len(letters) - 1:
            dn = letters[i + 1][0] - letters[i][0] - letters[i][1]
        result += get_text_symbol_from_image(model, letters[i][2])
        if dn > letters[i][1] / 4:
            result += ' '
    return result

