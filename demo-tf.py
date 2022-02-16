# TensorFlow and tf.keras
import tensorflow as tf

# Suppress output
from contextlib import contextmanager
import sys, os

###################################################################

import argparse

parser = argparse.ArgumentParser(description='Ermes Variables')
parser.add_argument('--models', dest='model', type=str, default=".output/models",help='Models path')
parser.add_argument('--images', dest='images', type=str,default=".outputs/images",help='Image path')
parser.add_argument('--logs', dest='logs', type=str,default=".output/logs" ,help='logs path')

args = parser.parse_args()
MODELPATH = args.models
IMAGESPATH = args.images
LOGSPATH = args.logs

###################################################################

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

print("Tensorflow version used: " + tf.__version__)

with suppress_stdout(): 
    fashion_mnist = tf.keras.datasets.fashion_mnist
with suppress_stdout():
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print (train_images.shape)

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.title("Image Sample")
plt.savefig(IMAGESPATH + '/image1.png', bbox_inches='tight')

train_images = train_images / 255.0

test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.savefig(IMAGESPATH + '/image2.png', bbox_inches='tight')

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
with suppress_stdout():
    model.fit(train_images, train_labels, epochs=10)
with suppress_stdout():
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)
