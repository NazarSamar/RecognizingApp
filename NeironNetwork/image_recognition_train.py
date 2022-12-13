import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.constraints import maxnorm
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import cifar10

#def get_mstar_data(stage, width=128, height=128, crop_size=128, aug=False):
#    data_dir = "MSTAR-10/train/" if stage == "train" else "MSTAR-10/test/" if stage == "test" else None
#    print("------ " + stage + " ------")
#    sub_dir = ["2S1", "BMP2", "BRDM_2", "BTR60", "BTR70", "D7", "T62", "T72", "ZIL131", "ZSU_23_4"]
#    X = []
#    y = []

#    for i in range(len(sub_dir)):
#        tmp_dir = data_dir + sub_dir[i] + "/"
#        img_idx = [x for x in os.listdir(tmp_dir) if x.endswith(".jpeg")]
#        print(sub_dir[i], len(img_idx))
#        y += [i] * len(img_idx)
#        for j in range(len(img_idx)):
#            img = im.imresize(im.imread((tmp_dir + img_idx[j])), [height, width])
#            img = img[(height - crop_size) // 2 : height - (height - crop_size) // 2, \
#                  (width - crop_size) // 2: width - (width - crop_size) // 2]
#            # img = img[16:112, 16:112]   # crop
#            X.append(img)

#    return np.asarray(X), np.asarray(y)

car_files = glob.glob("resizedImage\cars\*")

(x_train,y_train),(x_test,y_test)=cifar10.load_data()

x_train=x_train/255.0
x_test=x_test/255.0

cifar10_model= Sequential()

cifar10_model.add(Conv2D(filters=32,kernel_size=3,padding="same", activation="relu", input_shape=[32,32,3]))
cifar10_model.add(Conv2D(filters=32,kernel_size=3,padding="same", activation="relu"))
cifar10_model.add(MaxPooling2D(pool_size=2,strides=2,padding='valid'))
cifar10_model.add(Conv2D(filters=64,kernel_size=3,padding="same", activation="relu"))
cifar10_model.add(Conv2D(filters=64,kernel_size=3,padding="same", activation="relu"))
cifar10_model.add(MaxPooling2D(pool_size=2,strides=2,padding='valid'))
cifar10_model.add(Flatten())
cifar10_model.add(Dropout(0.5,noise_shape=None,seed=None))
cifar10_model.add(Dense(units=128,activation='relu'))
cifar10_model.add(Dense(units=10,activation='softmax'))
cifar10_model.compile(loss="sparse_categorical_crossentropy", optimizer="Adam", metrics=["sparse_categorical_accuracy"])
cifar10_model.fit(x_train,y_train,epochs=15)
test_loss, test_accuracy = cifar10_model.evaluate(x_test, y_test)

cifar10_model.save("model.h5")

scores = cifar10_model.evaluate(x_test, y_test)
print("Accuracy: %.2f%%" % (scores[1]*100))