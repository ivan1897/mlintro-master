
import pandas as pd 
from solution_va import info

#Lectura de los datos
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

#Se lleva a cabo la mediana de los datos
median_alcohol = df.alcohol.median()
median_pH = df.pH.median()
median_ResidualSugar = df.residual_sugar.median()
median_CitricAcid = df.citric_acid.median()

#Definimos las entidades de los datos
alcohol_e = 'alcohol'
pH_e = 'Ph'
residual_sugar_e= 'residual_sugar'
citric_acid_e = 'citric_acid'

#Se envian los datos a la funcion info
alcohol = info(median_alcohol, df.alcohol, alcohol_e)
ph = info(median_pH, df.pH, pH_e)
Residual_sugar = info(median_ResidualSugar, df.residual_sugar, residual_sugar_e)
Citric_acid = info(median_CitricAcid, df.citric_acid, citric_acid_e)
