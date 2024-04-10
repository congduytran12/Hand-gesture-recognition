# Hand Gesture Recognition Using Background Ellimination and Convolution Neural Network

## About the Project

This involves utilizing Convolutional Neural Networks along with background elimination to reconize various hand gestures. A background elimination technique is implemented to extract the hand image from a webcam feed, which is then utilized for both training and predicting the gesture type. Further details about the algorithm are provided below.

## Requirements

* Python3
* Tensorflow 
* TfLearn
* Opencv 
* Numpy
* Pillow (PIL)
* Imutils

## File Description

* palm_tracker.py : Run this file to generate custom datasets. Access the file and modify the directory name, as well as any other necessary changes.

* resize.py : Run this file after palm_tracker.py in order to resize the images, enabling compability with the Conolutional Neural Network using tensorflow. The network is designed to accept 89 x 100 dimensional image.

* train.ipynb : This is the model trainer file. Run this file if you want to retrain the model using your custom dataset.

* predictor.py : Running this file opens up your webcam and takes continuous frames of your hand image and then predicts the class of your hand gesture in real time.

## Some key architectural insights into the project

### Background Ellimination Algorithm

Employ opencv to compute a running average of the background for 30 frames. This running average is subsequently used to detect the hand, which is introduced once the background has been accurately recognized.

### The Deep Convolution Neural Network

The network includes **7** hidden convolution layers with **Relu** as the activation function and **1** Fully connected layer.

The network is trained across **50** iterations with a batch size of **64**.

50 iterations kind of trains the model well and there is no change in validation accuracy along the lines so that should be enough.

The model achieves an accuracy of **91%** on the validation dataset.

The ratio of training set to validation set is **1000 : 100**.

## How to run the real-time prediction

Run the **predictor.py** file and you will see a window named **Video Feed** appear on the screen. Wait for a while until a window named **Thresholded** appears.

The next step involves pressing **"s"** on your keyboard in order to start the real-time prediction.

Bring your hand in the **Green Box** drawn inside **Video Feed** window in order to see the predictions.


