import sys
import numpy as np
import tensorflow as tf
from pathlib import Path
import os
from detect_symbols import detect_symbols


filename = rf"{str(sys.argv[1])}"

model = tf.keras.models.load_model(r'E:\Coursework\NeironNetwork\model.h5')

result = detect_symbols(model, filename)
print(result)
