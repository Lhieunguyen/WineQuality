import pandas as pd

path_1 = 'D:\studygit1\WineQuality\Data set\winequality-red.csv'
path_2 = 'D:\studygit1\WineQuality\Data set\winequality-white.csv'
red_df = pd.read_csv(path_1)
white_df = pd.read_csv(path_2)
red_df = pd.DataFrame(red_df)
white_df = pd.DataFrame(white_df)
print(red_df.head())
print(white_df.head())
