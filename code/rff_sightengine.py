# rff_sightengine.py

def sightengine_classify_gender(faces, faces_df_dict, client):
    img_path = 'UTKFace/'
    for face in faces:
        face_path = img_path + face[0]
        response = client.check('face-attributes').set_file(face_path)
        print(response)
        try:
            female_conf = float(response['faces'][0]['attributes']['female'])
        except:
            female_conf = float("nan")
        try:
            male_conf = float(response['faces'][0]['attributes']['male'])
        except:
            male_conf = float("nan")
        if male_conf > female_conf:
            sightengine_label = 'Male'
        elif female_conf > male_conf:
            sightengine_label = 'Female'
        else:
            sightengine_label = 'undetermined'    
        print(sightengine_label, male_conf, female_conf)
        faces_df_dict["sightengine label"].append(sightengine_label)
        faces_df_dict["sightengine male"].append(male_conf)
        faces_df_dict["sightengine female"].append(female_conf)

    return faces_df_dict