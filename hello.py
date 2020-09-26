import numpy as np
import cv2


def world(event, context):
    print("Start of function")
    print("OpenCV version:", cv2.__version__)
    print("NumPy version:", np.__version__)
    print("End of function")
