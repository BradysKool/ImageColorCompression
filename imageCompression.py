import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt

image = Image.open('murphy.jpg')

npImage = np.array(image)
originalHight = npImage.shape[0]
originalWidth = npImage.shape[1]
npImage = np.reshape(npImage,(npImage.shape[0]*npImage.shape[1],npImage.shape[2]))
npImage = npImage/255

def findClosestCentroid(X,centroid):
    xClosest = np.zeros(X.shape[0],dtype=int)
    for i in range(X.shape[0]):
        closest = float('inf')
        for j in range(centroid.shape[0]):
            if np.linalg.norm(X[i]-centroid[j]) < closest:
                closest = np.linalg.norm(X[i]-centroid[j])
                xClosest[i] =  j
    return xClosest

def updateCentroids(X,xClosest,K):
    centroids = np.zeros((K,X.shape[1]))
    for k in range(K):
        points = []
        for i in range(len(xClosest)):
            if xClosest[i] == k:
                points.append(X[i])
        if len(points) > 0:
            centroids[k] = np.mean(points,axis=0)
    return centroids
def initilizeCentroids(X,K):
    numbers = random.sample(range(0,X.shape[0]),K)
    centroids = X[numbers]
    return centroids

def runClassification(X,centroids,maxIterations,K):
    prevCentroid = centroids
    for i in range(maxIterations):
        xClosest = findClosestCentroid(X,centroids)
        centroids = updateCentroids(X,xClosest,K)
        if np.array_equal(prevCentroid,centroids):
            break
        prevCentroid= centroids
        print('finised ' +str(i + 1) + ' iterations')
    return xClosest,centroids

k = 3
initialCentroids = initilizeCentroids(npImage,k)
xClosest,centroids = runClassification(npImage,initialCentroids,100,k)
print(xClosest)

compresedPhoto = np.zeros((npImage.shape))
for i in range(len(xClosest)):
    compresedPhoto[i] = centroids[xClosest[i]]
compresedPhoto = np.reshape(compresedPhoto,(originalHight,originalWidth,3))
plt.imshow(compresedPhoto)
plt.axis('off')
plt.show()