import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from convert_to_array import create_image_array
from save_and_load import save_to_file
import os
from config import *


df_data = pd.DataFrame()
df_label = pd.DataFrame()

folders = os.listdir(FOLDER_PATH)
for folder in folders:
    files = os.listdir(FOLDER_PATH + folder)
    for file in files:
        df_data = pd.concat([df_data, pd.DataFrame(create_image_array(FOLDER_PATH + folder + "\\" + file).reshape(1,-1))], axis=0)
        df_label = pd.concat([df_label, pd.DataFrame([folder])], axis=0)


# print(df_data)
# print(df_label)


# model = LogisticRegression()
model = LogisticRegression(solver='lbfgs', max_iter=1010)

model.fit(df_data, df_label.values.ravel())

save_to_file(model, 'logistic_reg_model_trained1000')

