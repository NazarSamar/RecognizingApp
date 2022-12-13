# make a prediction for a new image.

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten, Dense,Lambda
from keras.utils import plot_model

from tensorflow.keras.utils import load_img, img_to_array
from keras.models import load_model
import tensorflow.keras as keras
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import os
import numpy as np

classes = ['civilian aircraft','civilian car','military aircraft', 'military helicopter','military tank','military truck']
image_rows, image_cols = 256, 256

# load and prepare the image
def load_image(filename):
    try:
        img = keras.utils.load_img(filename, target_size=(image_rows, image_cols))
        
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, image_rows, image_cols, 3)
        # prepare pixel data
        img = img.astype('float32')
        img = img / 255.0
        return img
    except Exception as error:
        print(f"Exception = {error}")

def predict_classes(self, X, batch_size=128, verbose=1):
  proba = self.predict(X, batch_size=batch_size, verbose=verbose)


# load an image and predict the class
def run_recognition(model,filename):    
	# load the image
	img = load_image(filename)	
	# predict the class
	result = model.predict_classes(img)	
	toret = ""
	toret = f"{filename}: {classes[result[0]]}"
	probabilities = model.predict_proba(img)
	maxx = np.max(probabilities, axis=1)
	m1 = maxx[0]		
	if m1<0.98:
		toret = f"cannot recognize"
	return toret

def recognite(model,filename):
    img = load_image(filename)
    pred = model.predict(img,verbose = 0)
    predicted_class_indices=np.argmax(pred,axis=1)
    labels = {   
                 'civilian aircraft': 0,
                 'civilian car': 1,
                 'military aircraft': 2,
                 'military helicopter': 3,
                 'military tank': 4,
                 'military truck': 5
              }
    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]
    maxx = np.max(pred, axis=1)
    
    if(maxx<0.6):
        return 'cannot recognize'
    return predictions[0]

#model = tf.keras.models.load_model(r"C:\Users\nazar\NeironNetworkMilitary\military.h5")
#filename = r"C:\Users\nazar\NeironNetworkMilitary\test_img\c2c2fdc4dcd980c6ed21a88c673db2f8.png";
#print(recognite(filename,model))

#print(model.summary())
#run_recognition(model, 'asfaf.jpg') # car
#run_recognition('red-car.jpg') # car 
#run_recognition('Pilotless Airplanes 1.jpg') # airplane
#run_recognition('boeing-737.jpg') # airplane
#run_recognition('cat.jpg') # cat
