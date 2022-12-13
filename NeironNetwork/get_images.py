import cv2
import numpy as np
import tensorflow as tf
from image_recognition import run_recognition


def extract_images(filename):
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\grayimage.png', gray)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\gradient.png', gradient)

    contours, _ = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    result = image.copy()
    counter = 0
    for cnt in contours:
        x, y, width, height = cv2.boundingRect(cnt)
        roi = image[y:y+height, x:x+width]        
        cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\image'+str(counter)+'.png', roi)
        cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\dividedimage.png', cv2.rectangle(image, (x,y), (x+width,y+height), (0,0,255)))
        counter+=1
    res = f'{counter} photos was divided in {filename}'
    return res


def extract_image_classes(filename):
    model = tf.keras.models.load_model(r'E:\Coursework\PictureRecognition\NeironNetwork\image.h5')
    
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    contours, _ = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    res = ''
    result = image.copy()
    counter = 0
    for cnt in contours:
        x, y, width, height = cv2.boundingRect(cnt)
        roi = image[y:y+height, x:x+width]
        cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\image'+str(counter)+'.png', roi)
        cv2.imwrite(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\dividedimage.png', cv2.rectangle(image, (x,y), (x+width,y+height), (0,0,255)))
        result = run_recognition(model, r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\image'+str(counter)+'.png')
        res+=result+'\n'
        counter+=1
    res += f'{counter} photos was divided in {filename}'
    return res

#print(extract_image_classes(r'E:\Coursework\PictureRecognition\PictureRecognition\uploads\divided\dividedimage.png'))