import os

raw_imgs = os.listdir('UTKFace/')
# female_count = 0
# male_count = 0
# white_count = 0
# black_count = 0
# asian_count = 0 
# age_count = 0

# # [age] is an integer from 0 to 116, indicating the age
# # [gender] is either 0 (male) or 1 (female)
# # [race] is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).

# for img in raw_imgs:
#     labels = img.split('_')
#     if int(labels[0]) in range(18,36):
#         age_count += 1
#         if labels[1] == '0': 
#             male_count += 1
#         if labels[1] == '1':
#             female_count += 1
#         if labels[2] == '0':
#             white_count += 1
#         if labels[2] == '1':
#             black_count += 1
#         if labels[2] == '1':
#             asian_count += 1
#         print(labels)

# print("Female: " + str(female_count))
# print("Male: " + str(male_count))
# print("White: " + str(white_count))
# print("Black: " + str(black_count))
# print("Asian: " + str(asian_count))


# Classification lists to populate with triples of the form
# (filename, gender, race)
# to feed into commercial APIs later 
black_female = []
black_male   = []

asian_female = []
asian_male   = []

# indian_female = []
# indian_male   = [] 

white_female = []
white_male = []

for img in raw_imgs:
    filename = img
    labels = img.split('_')
    gender = int(labels[1])
    if int(labels[0]) in range(18,36):
        gender = int(labels[1])
        race = int(labels[2])
        dtuple = (filename, gender, race)
        if gender == 0:
            if race == 0:
                white_male.append(dtuple)
            elif race == 1:
                black_male.append(dtuple)
            elif race == 2:
                asian_male.append(dtuple)
            # elif race == 3:
            #     indian_male.append(dtuple)
            else:
                pass

        if gender == 1:
            if race == 0:
                white_female.append(dtuple)
            elif race == 1:
                black_female.append(dtuple)
            elif race == 2:
                asian_female.append(dtuple)
            # elif race == 3:
            #     indian_female.append(dtuple)
            else:
                pass

# white_faces = white_female[168:251] + white_male[168:251]
# black_faces = black_female[168:251] + black_male[168:251]
# asian_faces = asian_female[168:251] + asian_male[168:251]

white_faces = white_female[168:251] + white_male[168:251]
black_faces = black_female[168:251] + black_male[168:251]
asian_faces = asian_female[168:251] + asian_male[168:251]

print(len(white_faces), len(black_faces), len(asian_faces))

