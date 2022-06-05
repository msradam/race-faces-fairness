import boto3
import json
import pandas as pd
from rff_preprocess import white_faces, black_faces, asian_faces
from rff_setup import white_faces_df_dict, black_faces_df_dict, asian_faces_df_dict, df_cols

def rekog_classify_gender(faces, faces_df_dict, client): 
    img_path = 'UTKFace/'
    for face in faces: 
        imageFile = img_path + face[0]
        gender    = face[1]
        with open(imageFile, 'rb') as image: 
            response    = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
            rekog_label = response['FaceDetails'][0]['Gender']['Value']
            conf        = float(response['FaceDetails'][0]['Gender']['Confidence'])

        if rekog_label == 'Male':
             male_conf     = conf
             female_conf   = 100.0 - male_conf
        elif rekog_label == 'Female':
             female_conf   = conf
             male_conf     = 100.0 - female_conf
        else: 
            male_conf   = float('nan')
            female_conf = float('nan')

        print(rekog_label, male_conf, female_conf)

        faces_df_dict["filename"].append(face[0])
        faces_df_dict["gender label"].append(gender)
        faces_df_dict["rekognition label"].append(rekog_label)
        faces_df_dict["rekognition male"].append(male_conf)
        faces_df_dict["rekognition female"].append(female_conf)

    return faces_df_dict
