import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
 url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/flights.csv"
 return pd.read_csv(url)

flights = load_data()

st.title("Données sur les vols")


choix_date=st.slider("Selectionnez une date", min_value=1949, max_value=1960, value=(1949, 1960))
debut, fin=choix_date
filtre_annee_debut=flights["year"]>= debut
filtre_annee_fin=flights["year"]<= fin
flights2=flights[filtre_annee_debut & filtre_annee_fin]

mois_choisi = st.selectbox("Choisissez un mois", ["Tous les mois", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                                    "November", "December"], index=None)



if mois_choisi=="Tous les mois":
 flights3=flights2
else:
    flights3=flights2[flights2["month"]==mois_choisi]
st.dataframe(flights3)

st.metric("Nombre de passagers sur cette période", value=flights3['passengers'].sum())
passagers_annee=flights3.groupby("year")["passengers"].sum()


st.line_chart(passagers_annee)

if st.checkbox("Afficher la Heatmap"):
    tableau=flights3.pivot(index="month", columns="year", values="passengers")

    fig,ax=plt.subplots()
    sns.heatmap(tableau, ax=ax)
    st.pyplot(fig)