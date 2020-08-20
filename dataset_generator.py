import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

class DataGenerator:

    def __init__(self, path_dataset):

        self.path_dataset = path_dataset

    def get_dataset(self):

        image_names = os.listdir(self.path_dataset)
        images = []

        for img_name in image_names:

            img = plt.imread(os.path.join(self.path_dataset, img_name))
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            images.append(img)

        images_arr = np.array(images)

        return images_arr, image_names

        
