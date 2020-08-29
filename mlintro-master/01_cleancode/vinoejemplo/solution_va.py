
import pandas as pd

#Lectura de los datos
df = pd.read_csv('winequality-red.csv', sep=';')

#Se reciben los datos almacenados de los arreglos
def info(median_data, column_data, data):
    for i, d in enumerate(column_data):
        if d >= median_data:
            df.loc[i, data] = 'alto'
        else:
            df.loc[i, data] = 'bajo'
    result = df.groupby(data).quality.mean()
    return print (result)


