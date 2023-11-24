import cv2
import numpy as np
# def preprocess_image(image):
#     # Resize the image
#     new_width = 128
#     new_height = 128
#
#     # Resize the image to match the input shape of the model
#     resized_image = cv2.resize(image, (new_width, new_height))
#
#     # Normalize pixel values to be between 0 and 1
#     preprocessed_image = resized_image / 255.0
#
#     # Add batch dimension
#     preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
#
#     return preprocessed_image
def preprocess_image(image):
    # Resize the image
    new_width = 128
    new_height = 128

    # Resize the image to match the input shape of the model
    resized_image = cv2.resize(image, (new_width, new_height))

    # If the image has four channels, discard the last channel (transparency or additional channel)
    if resized_image.shape[-1] == 4:
        resized_image = resized_image[:, :, :3]

    # Normalize pixel values to be between 0 and 1
    preprocessed_image = resized_image / 255.0

    # Add batch dimension
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)

    return preprocessed_image
