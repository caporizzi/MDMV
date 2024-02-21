import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image
from matplotlib import image as mpimg

from opencv_bootcamp.Annotation import Annotate
from opencv_bootcamp.VideoSaver.VideoSaver import VideoSaver
from opencv_bootcamp.camera.VideoCapture import VideoCapture
from opencv_bootcamp.edgeDetection import edgeDetection


class ImageDisplay:
    """
    cv2.IMREAD_GRAYSCALE or 0: Loads image in grayscale mode
    cv2.IMREAD_COLOR or 1: Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv2.IMREAD_UNCHANGED or -1: Loads image as such including alpha channel.
    """
    def checkerDisplay(self, path, flag):
        image_path = path
        if os.path.isfile(image_path):
            img = cv.imread(image_path, flag)
            #cv.cvtColor(img, cv.COLOR_BGR2RGB)
            """cv2.cvtColor() Converts an image from one color space to another."""
            plt.imshow(img, cmap='gray')
            plt.axis('off')  # Turn off axis
            plt.show()

        else:
            print(f"Image file '{image_path}' not found.")

    def splitMerge(self, path):
        # Split the image into the B,G,R components
        image_path = path
        img_NZ_bgr = cv.imread(image_path, 1)
        b, g, r = cv.split(img_NZ_bgr)

        # Show the channels
        plt.figure(figsize=[20, 5])
        plt.subplot(141);
        plt.imshow(r, cmap="gray");
        plt.title("Red Channel")
        plt.subplot(142);
        plt.imshow(g, cmap="gray");
        plt.title("Green Channel")
        plt.subplot(143);
        plt.imshow(b, cmap="gray");
        plt.title("Blue Channel")


        # Merge the individual channels into a BGR image
        imgMerged = cv.merge((b, g, r))
        # Show the merged output
        plt.subplot(144)
        plt.imshow(imgMerged[:, :, ::-1])
        """[:, :, ::-1]: This specifies slicing along all dimensions of the array. The first : indicates that we want to select all rows of the array, 
        the second : indicates that we want to select all columns, 
        and ::-1 indicates that we want to reverse the order along the last axis (which is typically the color channel axis in an image)."""

        plt.title("Merged Output")
        plt.show()
    def imageSaver(self, path):
        pass




def main():
    #imageDisplayer = ImageDisplay()
    #annotaterDisplayer = Annotate()
    #imageDisplayer.checkerDisplay(".\\img\\coca-cola-logo.png", 1)
    #imageDisplayer.checkerDisplay(".\\img\\coca-cola-logo.png", 0)
    #imageDisplayer.splitMerge(".\\img\\New_Zealand_Lake.jpg")
    #videoCapturer = VideoCapture()
    #videoSaver = VideoSaver().save()
    edgeDetector = edgeDetection().detector()




if __name__ == "__main__":
    main()