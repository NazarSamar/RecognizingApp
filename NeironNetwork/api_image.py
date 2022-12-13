import sys
import numpy as np
import tensorflow as tf
from pathlib import Path
import os
from image_recognition import recognite, run_recognition


basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)
filename = rf"{str(sys.argv[1])}"

model = tf.keras.models.load_model(r"C:\Users\nazar\NeironNetworkMilitary\military.h5")

result = recognite(model, os.path.join(basedir,filename))
print(result)

#model = tf.keras.models.load_model(r"E:\Coursework\PictureRecognition\NeironNetwork\image.h5")
#print('filename1:'+filename)
#result = run_recognition(model, os.path.join(basedir,filename))
#print(result)