import os
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn import MTCNN
import cv2
import numpy as np

class FaceLandmarkDetection:

    def __init__(self, dataset, path_save_dataset, image_names):
        self.dataset = dataset
        self.path_save_dataset = path_save_dataset
        self.image_names = image_names

    def draw_image_boxes(self, image, faces, name):
        # plot the image
        plt.imshow(image)
        # get the context for drawing boxes
        ax =  plt.gca()

        # plot landmark
        for face_landmark in faces:
            # get the coordinates
            x, y, width, height = face_landmark['box']

            # create shape
            rectangle = Rectangle((x, y), width, height, fill=False, color='red')

            # draw box
            ax.add_patch(rectangle)

            # draw dot
            for key, value in face_landmark['keypoints'].items():
                # create and draw dots
                dot = Circle(value, radius=2, color='red')
                
                ax.add_patch(dot)
        plt.axis('off')
        plt.savefig(os.path.join(self.path_save_dataset, name))

    def face_landmark_detection(self):

        for id, image in enumerate(self.dataset):

            detector = MTCNN()
            faces_landmark = detector.detect_faces(image)

            self.draw_image_boxes(image, faces_landmark, self.image_names[id])

