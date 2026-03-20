# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:13:35 2026

@author: anais
"""




import pandas as pd

# Charger le fichier CSV
df = pd.read_csv(r"C:\Users\anais\Downloads\sales_dataset.csv")

# Afficher les premières lignes
print(df.head())

# Convertir la date
df['Date'] = pd.to_datetime(df['Date'])

# Supprimer les valeurs manquantes
df = df.dropna()

# Supprimer les doublons
df = df.drop_duplicates()

# Créer une colonne revenue si elle n'existe pas
df['Revenue'] = df['Quantité'] * df['Prix']

print(df.describe())
print(df['Produit'].value_counts())
print(df['Région'].value_counts())

print(df.describe())
print(df['Produit'].value_counts())
print(df['Région'].value_counts())

product_sales = df.groupby('Produit')['Revenue'].sum().sort_values(ascending=False)
print(product_sales)
region_sales = df.groupby('Région')['Revenue'].sum()
print(region_sales)
monthly_sales = df.resample('M', on='Date')['Revenue'].sum()
print(monthly_sales)

import matplotlib.pyplot as plt

product_sales.plot(kind='bar')
plt.title("Ventes par produit")
plt.show()

monthly_sales.plot()
plt.title("Tendance des ventes")
plt.show()

monthly_sales.plot()
plt.title("Tendance des ventes")
plt.show()

import seaborn as sns

pivot = df.pivot_table(values='Revenue', index='Région', columns='Produit')

sns.heatmap(pivot, annot=True, fmt=".0f")
plt.title("Heatmap des ventes")
plt.show()
df.to_csv("clean_sales_data.csv", index=False)

