
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
print (df.head())

ma = df.alcohol.median()
for i, alcohol1 in enumerate(df.alcohol):
    if alcohol1 >= ma:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

mpH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= mpH:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

ma = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= ma:
        df.loc[i, 'residual_sugar'] = 'alto'
    else:
        df.loc[i, 'residual_sugar'] = 'bajo'
df.groupby('residual_sugar').quality.mean()

mca = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= mca:
        df.loc[i, 'citric_acid'] = 'alto'
    else:
        df.loc[i, 'citric_acid'] = 'bajo'
df.groupby('citric_acid').quality.mean()