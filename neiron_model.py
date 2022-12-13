from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.utils import plot_model

emnist_labels = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

def neiron_model():
    image_rows, image_cols = 28, 28
    model = Sequential(
        [
            Convolution2D(filters=32, kernel_size=(3, 3), padding='valid', input_shape=(image_rows, image_cols, 1), activation='relu'),
            Convolution2D(filters=64, kernel_size=(3, 3), activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Dropout(0.25),
            Flatten(),
            Dense(512, activation='relu'),
            Dropout(0.5),
            Dense(len(emnist_labels), activation='softmax')
        ]
    )
    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])
    return model

#plot_model(emnist_model(), to_file='examples\model.png', show_shapes=True)\
