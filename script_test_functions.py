import pandas as pd
from devModel.eda import Eda

df = pd.read_csv(r'C:\Users\ALEJANDRO\Desktop\Projects\Virtual_Analyzer\Datas Corridas\test.csv')
eda = Eda(df)
print(eda.describe())