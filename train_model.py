import pandas as pd
from sklearn.linear_model import LogisticRegression
from convert_to_array import create_image_array


df_data = pd.DataFrame(create_image_array('test_plate.png'))
df_label = pd.DataFrame(['A'])

df_data = pd.concat([df_data, pd.DataFrame(create_image_array('test_plate2.png'))], axis=0)
df_label = pd.concat([df_label, pd.DataFrame(['B'])], axis=0)

model = LogisticRegression()
model.fit(df_data, df_label.values.ravel())
