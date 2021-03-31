import cv2
import numpy as np
# from google.colab.patches import cv2_imshow

def messageToBinary(message):
    if type(message) == str:
        return "".join([format(ord(i),"08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i,"08b") for i in message]
    else:
        raise TypeError("Input type not supported")


def hideData(image,message):
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8

    if len(message) > n_bytes:
        raise ValueError("Error message too long")

    message += "#####"

    data_index = 0

    binary_message = messageToBinary(message)

    data_len = len(binary_message)

    for row in image:
        for pixel in row:
            if data_index >= data_len:
                break
            r,g,b = messageToBinary(pixel)
            if data_index < data_len:
                pixel[0] = r([:-1] + binary_message[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = g([:-1] + binary_message[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = b([:-1] + binary_message[data_index], 2)
                data_index += 1
    return image


print(messageToBinary("Hello World!"))