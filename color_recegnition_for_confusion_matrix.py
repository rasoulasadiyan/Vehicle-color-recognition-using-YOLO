import cv2
import os
import os.path
import sys
import csv
import random
import math
import operator
from PIL import Image

# calculation of euclidead distance
def calculateEuclideanDistance(variable1, variable2, length):
    distance = 0
    for x in range(length):
        distance += pow(variable1[x] - variable2[x], 2)
    return math.sqrt(distance)


# get k nearest neigbors
def my(training_feature_vector, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(training_feature_vector)):
        dist = calculateEuclideanDistance(testInstance,
                training_feature_vector[x], length)
        distances.append((training_feature_vector[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# votes of neighbors
def responseOfNeighbors(neighbors):
    all_possible_neighbors = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in all_possible_neighbors:
            all_possible_neighbors[response] += 1
        else:
            all_possible_neighbors[response] = 1
    sortedVotes = sorted(all_possible_neighbors.items(),
                         key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def r_main(No):
    training_feature_vector = []  # training feature vector
    test_feature_vector = []  # test feature vector

####
    
    with open('train.data') as csvfile:
        lines = csv.reader(csvfile)
        
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(3):
                dataset[x][y] = float(dataset[x][y])
            training_feature_vector.append(dataset[x])

    filename='test'+ str(No)+ '.data'
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(3):
                dataset[x][y] = float(dataset[x][y])
            test_feature_vector.append(dataset[x])



####

    classifier_prediction = []  # predictions
    k = 4  # K value of k nearest neighbor
    for x in range(len(test_feature_vector)):
        neighbors = my(training_feature_vector, test_feature_vector[x], k)
        result = responseOfNeighbors(neighbors)
        classifier_prediction.append(result)

    return classifier_prediction[0]		


#


from PIL import Image
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq

def color_histogram_of_test_image(test_src_image,No):

    # load the image
    image = test_src_image

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            # print(feature_data)

    filename='test'+str(No)+'.data'
    with open(filename, 'w') as myfile:
        myfile.write(feature_data)


def color_histogram_of_training_image(img_name):

    # detect image color by using image file name to label training data
    if 'red' in img_name:
        data_source = 'red'
    elif 'yellow' in img_name:
        data_source = 'yellow'
    elif 'green' in img_name:
        data_source = 'green'
    elif 'orange' in img_name:
        data_source = 'orange'
    elif 'white' in img_name:
        data_source = 'white'
    elif 'black' in img_name:
        data_source = 'black'
    elif 'blue' in img_name:
        data_source = 'blue'
    elif 'violet' in img_name:
        data_source = 'violet'
    elif 'brown' in img_name:
        data_source = 'brown'
    elif 'grey' in img_name:
        data_source = 'grey'
    

    # load the image
    image = cv2.imread(img_name)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue

    with open('train.data', 'a') as myfile:
        myfile.write(feature_data + ',' + data_source + '\n')


def training():

    # red color training images
    for f in os.listdir('./colors/training2/red'):
        color_histogram_of_training_image('./colors/training2/red/' + f)

    # yellow color training images
    for f in os.listdir('./colors/training2/yellow'):
        color_histogram_of_training_image('./colors/training2/yellow/' + f)

    # green color training images
    for f in os.listdir('./colors/training2/green'):
        color_histogram_of_training_image('./colors/training2/green/' + f)

    # orange color training images
    for f in os.listdir('./colors/training2/orange'):
        color_histogram_of_training_image('./colors/training2/orange/' + f)

    # white color training images
    for f in os.listdir('./colors/training2/white'):
        color_histogram_of_training_image('./colors/training2/white/' + f)

    # black color training images
    for f in os.listdir('./colors/training2/black'):
        color_histogram_of_training_image('./colors/training2/black/' + f)

    # blue color training images
    for f in os.listdir('./colors/training2/blue'):
        color_histogram_of_training_image('./colors/training2/blue/' + f)

    # brown color training images
    for f in os.listdir('./colors/training2/brown'):
        color_histogram_of_training_image('./colors/training2/brown/' + f)		

    # grey color training images
    for f in os.listdir('./colors/training2/grey'):
        color_histogram_of_training_image('./colors/training2/grey/' + f)

    # voilet color training images
    for f in os.listdir('./colors/training2/violet'):
        color_histogram_of_training_image('./colors/training2/violet/' + f)		



def recegnizion_color(num):

    prediction = 'n.a.'

    PATH = './train.data'

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print ('training data is ready, classifier is loading...')
    else:
        print ('training data is being created...')
        open('train.data', 'w')
        training()
        print ('training data is ready, classifier is loading...')

    # get the prediction
    prediction=[]
    i=1
 
    with open('croped_images_coordinates.txt') as csvfile:
        data = csv.reader(csvfile)
        crds=list(data)
        for k in range(0,len(crds)):

            name='croped'+str(k+1)
            path=f'static/detect_car_images/{name}.jpg'
            source_image = Image.open(path)
            croped_image = source_image.crop((float(crds[k][0]), float(crds[k][1]), float(crds[k][2]), float(crds[k][3])))
            color_histogram_of_test_image(croped_image,k)
            p=r_main(k)
            prediction.append(p)
            i+=1 
        

    return prediction