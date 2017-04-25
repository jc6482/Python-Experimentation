# Juan Carlos Ramirez
# Compares image files for matching images.
import argparse
import os
import sys
from skimage.measure import compare_ssim as ssim
import numpy as np
import cv2


parser = argparse.ArgumentParser(description="Compares image files for matching images.")
parser.add_argument("-D", default=".", help="Directory to search")
parser.add_argument("-sf", type=float, default=".5", help="Filter for similarity. Default is 50%")

args = parser.parse_args()

fileObjs = []
validExtensions = [".jpg", ".jpeg", ".bmp"]
fileComparisons = []

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare(imagePath1, imagePath2):
    image1 = cv2.imread(imagePath1)
    image2 = cv2.imread(imagePath2)

    image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

    if(image1.size != image2.size):
        image2 = cv2.resize(image2,(image1.shape[1],image1.shape[0]))

    m = mse(image1, image2)
    s = ssim(image1,image2)

    return ("{} and {} have a similarity of (-1 ~ [{:03.2f}] ~ 1). With a {:03.2f} mean squared error.".format(os.path.basename(imagePath1),os.path.basename(imagePath2),s, m),s)

def compareImages(imageSet):
    imageSet = list(imageSet)
    for x in range(0,len(imageSet)):
        for y in range(x,len(imageSet)):
            if not x == y:
                fileComparisons.append(compare(imageSet[x],imageSet[y]))
        
def storeImage(filePath):
    fileName, file_extension = os.path.splitext(filePath)
    if file_extension in validExtensions:
        fileObjs.append(filePath)

def processDir(dirPath):
    for root, dirs, filenames in os.walk(dirPath):
        for d in dirs:
                processDir(d)
        for f in filenames:
            storeImage(os.path.abspath(os.path.join(root,f)))
    
def main():
    
    if not os.path.isdir(args.D):
        print "Bad Directory"
        os._exit(-1)
    else:
        processDir(args.D)
        compareImages(set(fileObjs))
        fileComparisons.sort(key=lambda x:x[1])
        print "Results: "
        for comp in fileComparisons:
            if comp[1] >= args.sf:
                print comp[0]

main()

