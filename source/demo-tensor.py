###################################################################

import argparse

parser = argparse.ArgumentParser(description='Ermes Variables')
parser.add_argument('--models', dest='models', type=str, default=".output/models",help='Models path')
parser.add_argument('--images', dest='images', type=str,default=".outputs/images",help='Image path')
parser.add_argument('--logs', dest='logs', type=str,default=".output/logs" ,help='logs path')

args = parser.parse_args()
MODELPATH = args.models
IMAGESPATH = args.images
LOGSPATH = args.logs

###################################################################

import tensorflow as tf
import datetime

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def create_model():
  return tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])

model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

log_dir = LOGSPATH + "/fit" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x=x_train, 
          y=y_train, 
          epochs=5, 
          validation_data=(x_test, y_test), 
          callbacks=[tensorboard_callback])


