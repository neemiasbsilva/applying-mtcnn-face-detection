import os
import argparse
import numpy as np
import cv2
from dataset_generator import DataGenerator
from mtcnn_application import FaceLandmarkDetection

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Applying MTCNN for Face Detection")

    parser.add_argument("-path_dataset", action="store",
                        help="folder of dataset", dest="path_dataset")
    parser.add_argument("-path_save_dataset", action="store",
                        help="forder of save the mtcnn result", dest="path_save_dataset")


    arguments = parser.parse_args()

    path_dataset = arguments.path_dataset
    path_save_dataset = arguments.path_save_dataset


    dataset_generator = DataGenerator(path_dataset)

    dataset, image_names = dataset_generator.get_dataset()

    mtcnn = FaceLandmarkDetection(dataset, path_save_dataset, image_names)

    mtcnn.face_landmark_detection()