import cv2
import numpy as np
import tensorflow as tf
import io 
import pytesseract
from image_recognition import run_recognition,recognite
from detect_symbols import detect_symbols
import string 
from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import Output
import os 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
alphabet = list(string.ascii_lowercase)
alphabet_uppercase = list(string.ascii_uppercase)
alphabet.extend(alphabet_uppercase)

def getimage_allinfo(filename):
    try:
        model_img = tf.keras.models.load_model(r"C:\Users\nazar\NeironNetworkMilitary\military.h5")
        model_text = tf.keras.models.load_model(r'E:\Coursework\NeironNetwork\model.h5')

        image = cv2.imread(rf"{filename}")        

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\grayimage.png', gray)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\gradient.png', gradient)
        contours, _ = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        res = ''
        result = image.copy()
        counter = 0
        for cnt in contours:
            x, y, width, height = cv2.boundingRect(cnt)
            roi = image[y:y+height, x:x+width]
            nametosave = r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\image'+str(counter)+'.png'
            cv2.imwrite(nametosave, roi)
            cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\dividedimage.png', cv2.rectangle(image, (x,y), (x+width,y+height), (0,0,255)))
            result = recognite(model_img, nametosave)            
            if result == f'cannot recognize':
                result_text = detect_symbols(model_text, nametosave)
                res += f'{nametosave} = {result_text}, \n'                
            else:
                res+=result+'\n'                
            counter+=1            
        #res += f'{counter} p {filename}'
        return res
    except Exception as error:
        print(f"Exception = {error}")
        return f"Exception = {error}"

#getimage_allinfo(r"E:\Coursework\PictureRecognition\PictureRecognitionApp\PictureRecognitionApp\uploads\divided\boeing-737.jpg")