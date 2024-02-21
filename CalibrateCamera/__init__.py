import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import image

img = cv.imread(".\pictures\chocobo.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0)