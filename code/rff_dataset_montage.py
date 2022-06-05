# import the necessary packages
from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2

from rff_preprocess import asian_faces, black_faces, white_faces

asian_male_female = asian_faces[:3] + asian_faces[-3:]
black_male_female = black_faces[:3] + black_faces[-3:]
white_male_female = white_faces[:3] + white_faces[-3:]

img_path = 'UTKFace/'
asian_face_paths = [img_path + face[0] for face in asian_male_female]
black_face_paths = [img_path + face[0] for face in black_male_female]
white_face_paths = [img_path + face[0] for face in white_male_female]

asian_images = [cv2.imread(path) for path in asian_face_paths]
black_images = [cv2.imread(path) for path in black_face_paths]
white_images = [cv2.imread(path) for path in white_face_paths]

asian_montage = build_montages(asian_images, (200,200), (6,1))
black_montage = build_montages(black_images, (200,200), (6,1))
white_montage = build_montages(white_images, (200,200), (6,1))
for montage in white_montage:
	cv2.imshow("Montage", montage)
	cv2.waitKey(0)