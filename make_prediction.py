import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from save_and_load import load_file
from convert_to_array import create_image_array
import os
from config import *

model = load_file('logistic_reg_model_trained100.pkl')
test_frame = pd.DataFrame(create_image_array('test_plate2.png').reshape(1,-1))


predicted_label = model.predict(test_frame)

print(predicted_label)
