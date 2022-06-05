import json
import boto3
import pandas as pd
from sightengine.client import SightengineClient

from rff_preprocess import asian_faces, black_faces, white_faces
from rff_rekognition import rekog_classify_gender
from rff_setup import (asian_faces_df_dict, black_faces_df_dict, df_cols,
                       white_faces_df_dict)
from rff_sightengine import sightengine_classify_gender

if __name__ == "__main__":
    boto3_client = boto3.client('rekognition')
    se_client = SightengineClient('184910388', 'XKG63KMNwoWQTBcDW84k')
    black_faces_df = pd.DataFrame(sightengine_classify_gender(black_faces, 
                                  rekog_classify_gender(black_faces, black_faces_df_dict, boto3_client),
                                  se_client))
    asian_faces_df = pd.DataFrame(sightengine_classify_gender(asian_faces, 
                                  rekog_classify_gender(asian_faces, asian_faces_df_dict, boto3_client),
                                  se_client))    
    white_faces_df = pd.DataFrame(sightengine_classify_gender(white_faces, 
                                  rekog_classify_gender(white_faces, white_faces_df_dict, boto3_client),
                                  se_client))
    black_faces_df.to_csv('black_faces3.csv')
    asian_faces_df.to_csv('asian_faces3.csv')
    white_faces_df.to_csv('white_faces3.csv')