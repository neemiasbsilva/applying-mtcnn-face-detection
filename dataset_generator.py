import os
import numpy as np
import cv2

class DataGenerator:

    def __init__(self, path_dataset):

        self.path_dataset = path_dataset

    def get_dataset(self):

        image_names = os.listdir(path_dataset)
        images = []

        for img_name in image_names:

            img = cv2.imread(img_name)
            images.append(img)

        images_arr = np.array(images)

        return images_arr

        