import streamlit as st
import pandas as pd 
from PIL import Image

chemin_contenu="C:\Applications\Espace_Projet\Projet_Streamlit\.venv\DataFrame\Les_jeux.xlsx"

df=pd.read_excel(chemin_contenu,index_col=None, header=1)

tab1, tab2, tab3 ,tab4 ,tab5  = st.tabs([
   "Assassin's Creed", "Assassin's Creed 2", "Assassin's creed Brotherhood",
   "Assassin creed revelations","Assassin’s creed 3"])


#creation des onglets 
tab6 ,tab7 = st.tabs(["Assassin's creed Black flag",
   "Assassin creed Rogue"])

#creation de colonnes
col1, col2, col3 = st.columns(3)

with tab1:
   st.header("L'histoire du jeu")
   img_assassin1 = Image.open("C:\Applications\Espace_Projet\Projet_Streamlit\.venv\Images\Assassin's creed 1.jpg")
   st.image(img_assassin1,width=200) 
   st.write(df.iloc[0,1])
   st.header("Les retours")
   st.write(df.iloc[0,3])
   st.header("Quelques chiffres")
   st.write("Le jeux à vendu :",df.iloc[0,4], "de copies et obtenu une note de",df.iloc[0,5],"sur Metactritic :sunglasses:")
   st.header("Analyse des sentiments")


with tab2:
   st.header("L'histoire du jeu")
   img_assassin2 = Image.open("C:\Applications\Espace_Projet\Projet_Streamlit\.venv\Images\Assassin's Creed 2.jpg")
   st.image(img_assassin2,width=200) 
   st.write(df.iloc[1,1])
   st.header("Les retours")
   st.write(df.iloc[1,3])
   st.header("Analyse des sentiments")

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab5:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab6:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab7:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)