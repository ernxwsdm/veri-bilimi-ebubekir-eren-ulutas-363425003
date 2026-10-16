import pandas as pd
import numpy as np

df_demografi = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Grup': ['Kontrol', 'Tedavi', 'Kontrol', 'Tedavi']
})

df_olcumler = pd.DataFrame({
    'ID': [1, 1, 2, 2, 3, 4, 4],
    'Zaman': ['T0', 'T1', 'T0', 'T1', 'T0', 'T0', 'T1'],
    'Skor': [55, 60, 40, 50, 58, 42, 48]
})

df_birlesik = pd.merge(df_demografi, df_olcumler, on='ID', how='inner')

df_pivot = df_birlesik.pivot_table(
    index=['ID', 'Grup'],
    columns='Zaman',
    values='Skor'
).reset_index()

df_pivot.columns.name = None

df_pivot['T1'] = df_pivot['T1'].fillna(df_pivot['T0'])

df_pivot['Gelisim_Farki'] = df_pivot['T1'] - df_pivot['T0']

print(df_pivot)