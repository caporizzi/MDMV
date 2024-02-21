import cv2 as cv
import matplotlib.pyplot as plt
class Annotate:

    def drawline(self):
        img = cv.imread(".\\img\\Apollo_11_Launch.jpg", 1)

        plt.imshow(img)
        plt.show()
        imageLine = img.copy()
        cv.line(imageLine, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv.LINE_AA);
        plt.imshow(imageLine)
        plt.show()


