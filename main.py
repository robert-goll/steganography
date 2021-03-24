import cv2
import numpy as np
# from google.colab.patches import cv2_imshow

def messageToBinary(message):
    if type(message) == str:
        return "".join([format(ord(i),"08b") for i in message])

print(messageToBinary("Hello World!"))