#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
BASE_FOLDER = "C:/Users/Alvaro/PycharmProjects/scientificProject"
path = BASE_FOLDER + "data/titanic.csv"

df = pd.read_csv

#%%
data_np = np.ones((1, 1, 6, 6))

plt.imshow(np.squeeze(data_np), cmap='gray')
plt.axis('off')
plt.show()