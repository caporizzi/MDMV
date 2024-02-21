import sys
import cv2 as cv
import matplotlib.pyplot as plt


class VideoSaver:
    def save(self):
        source = 0
        capture = cv.VideoCapture(source)
        if not capture.isOpened():
            print("Error opening video stream or file")

        ret, frame = capture.read()
        plt.imshow(frame[..., ::-1])
        frame_width = int(capture.get(3))
        frame_height = int(capture.get(4))
        #out_mp4 = cv.VideoWriter("me2.mp4", cv.VideoWriter_fourcc(*"XVID"), 10, (frame_width, frame_height))
        out_mp4 = cv.VideoWriter("me3.mp4", cv.VideoWriter_fourcc(*"H264"), 10, (frame_width, frame_height))
        while capture.isOpened():
            # Capture frame-by-frame
            ret, frame = capture.read()

            if ret:
                # Write the frame to the output files
                out_mp4.write(frame)

            # Break the loop
            else:
                break

        capture.release()
        out_mp4.release()

