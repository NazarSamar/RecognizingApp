import os
from idx2numpy import convert_from_file
import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from NeironNetwork.neiron_model import neiron_model, emnist_labels


def train_network(out_size=28, emnist_path='gzip/', name_model='model.h5'):
    train_images_folder = os.path.join(emnist_path, 'emnist-byclass-train-images-idx3-ubyte/')
    train_labels_folder = os.path.join(emnist_path, 'emnist-byclass-train-labels-idx1-ubyte/')
    test_images_folder = os.path.join(emnist_path, 'emnist-byclass-test-images-idx3-ubyte/')
    test_labels_folder = os.path.join(emnist_path, 'emnist-byclass-test-labels-idx1-ubyte/')

    train_x = convert_from_file(train_images_folder + 'emnist-byclass-train-images-idx3-ubyte')
    train_y = convert_from_file(train_labels_folder + 'emnist-byclass-train-labels-idx1-ubyte')

    test_x = convert_from_file(test_images_folder + 'emnist-byclass-test-images-idx3-ubyte')
    test_y = convert_from_file(test_labels_folder + 'emnist-byclass-test-labels-idx1-ubyte')

    x_train = np.reshape(train_x, (train_x.shape[0], out_size, out_size, 1))
    x_test = np.reshape(test_x, (test_x.shape[0], out_size, out_size, 1))

    x_train = x_train.astype(np.float32)
    x_train = x_train / 255.0
    x_test = x_test.astype(np.float32)
    x_test = x_test / 255.0

    y_train_cat = tf.keras.utils.to_categorical(train_y, len(emnist_labels))
    y_test_cat = tf.keras.utils.to_categorical(test_y, len(emnist_labels))

    learning_rate_reduction = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_acc', patience=3, verbose=1, factor=0.5,
                                                                   min_lr=0.00001)
    with tf.compat.v1.Session() as ses:
        ses.run(tf.compat.v1.global_variables_initializer())
    model = neiron_model()
    model.fit(x_train, y_train_cat, validation_data=(x_test, y_test_cat), callbacks=[learning_rate_reduction],
              batch_size=64, epochs=30)

    model.save(name_model)



