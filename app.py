import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Analyse des facteurs influençant le prix des logements en Californie")

@st.cache_data
def load_data():
    data = pd.read_csv("housing.csv")
    return data

data_load_state = st.text('Chargement des données...')
data = load_data()
data_load_state.text('Données chargées avec succès!')

st.header("Aperçu des données")
st.write(data.head())

st.header("Statistiques descriptives")
st.write(data.describe())

st.header("Distribution des prix des logements")
fig, ax = plt.subplots(figsize=(10,5))
sns.histplot(data['median_house_value'], bins=50, kde=True, ax=ax)
ax.set_xlabel("Prix médian des logements")
ax.set_ylabel("Fréquence")
st.pyplot(fig)

st.header("Boxplot des prix des logements")
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(x=data['median_house_value'], ax=ax)
ax.set_xlabel("Prix médian des logements")
st.pyplot(fig)

st.header("Carte de corrélation des caractéristiques")
numeric_data = data.select_dtypes(include=[np.number])
corr = numeric_data.corr()

fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.header("Analyse des facteurs influençant le prix")

corr_target = corr['median_house_value'].drop('median_house_value').sort_values(ascending=False)
st.write("Corrélation des caractéristiques avec le prix médian des logements :")
st.write(corr_target)

st.header("Recommandations stratégiques")
st.markdown("""
- Se concentrer sur les caractéristiques ayant la plus forte corrélation positive avec le prix, telles que la superficie moyenne des pièces, le revenu moyen des ménages, et la proximité des commodités.
- Utiliser ces facteurs pour affiner les stratégies marketing et les évaluations immobilières.
- Surveiller les tendances du marché en fonction des variations de ces caractéristiques.
""")
