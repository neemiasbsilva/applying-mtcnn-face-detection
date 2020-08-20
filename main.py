import os
import argparse
import numpy as np
import cv2
from dataset_generator import DataGenerator

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Applying MTCNN for Face Detection")

    parser.add_argument("-path_dataset", action="store",
                        help="folde of dataset", dest="path_dataset")

    arguments = parser.parse_args()

    path_dataset = arguments.path_dataset

    dataset_generator = DataGenerator(path_dataset)

    dataset = dataset_generator.get_dataset()
    
    print(dataset.shape)