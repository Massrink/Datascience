import streamlit as st
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
from pathlib import Path
import os
import numpy as np 

# recuperation du chemin relatif du fichier de répartition des salariés
lien = r"C:\Applications\Espace_Projet\Projet_Streamlit\.venv\DataFrame\Ubisoft_repartition_salaries_2022.xlsx"
chemin_absolu = os.path.abspath(lien)
dossier_actuel = os.getcwd()
chemin_relatif = os.path.relpath(chemin_absolu, dossier_actuel)

# recuperation des revenu net 2004-2022
lien_revenu_net = r"C:\Applications\Espace_Projet\Projet_Streamlit\.venv\DataFrame\Ubisoft_revenu_net_2004-2022.xlsx"
chemin_absolu = os.path.abspath(lien_revenu_net)
chemin_relatif_revenu_net = os.path.relpath(chemin_absolu, dossier_actuel)

# recuperation des ventes nettes annuelles 2004-2022
lien_ventes_net = r"C:\Applications\Espace_Projet\Projet_Streamlit\.venv\DataFrame\Ubisoft_ventes nettes_annuelles_2004-2022.xlsx"
chemin_absolu = os.path.abspath(lien_ventes_net)
chemin_relatif_ventes_net = os.path.relpath(chemin_absolu, dossier_actuel)


################################## Partie Repartition des salaires ####################################

# import du fichier provenant de statista qui importe le profil de personnes en fonction du sexe
df_repartition_salarie=pd.read_excel(chemin_relatif,
                            sheet_name='Data',
                            skiprows=4,
                            index_col=False,
                            usecols=['Unnamed: 1','Production','Business']
                            )

#Je renome le DF pour avoir le genre à la place de Unnamed
df_repartition_salarie=df_repartition_salarie.rename(columns={'Unnamed: 1':'Gender'})

#Titre de la section 
st.header("Repartition des salariés par sex")

#Je créé une Check box 
check=st.selectbox('Quel type de personnes vous voulez voir ?', df_repartition_salarie['Gender'].unique())

#je genere un DF à chaque selection de la checkbox
df_repartition_salarie_selected=df_repartition_salarie[df_repartition_salarie['Gender']==check]

st.write(df_repartition_salarie_selected)


#test=list(df_repartition_salarie_selected.iloc[:,1:].values)
#test3=test.reshape(-1, 1)
#test2=[3,2]
#st.write(test)
#fig1, ax1 = plt.subplots()
#ax1.pie(test3)

#st.pyplot(fig1)

################################## Partie Revenu net ####################################

st.header('Revenu net par mois')

df_revenu_net=pd.read_excel(chemin_relatif_revenu_net,
                            sheet_name='Data',
                            skiprows=4,
                            usecols=[1,2],
                            names=['Year-Month','Net revenu']
                             )


df_revenu_net[['Year', 'Month']] = df_revenu_net['Year-Month'].str.split("-", expand = True)

#Je créé une Check box 
check_revenu_net=st.selectbox('Quel année?', df_revenu_net['Year'].unique())
df_revenu_net_select=df_revenu_net[df_revenu_net['Year']==check_revenu_net]

st.write(df_revenu_net_select)

st.line_chart(data=df_revenu_net,y='Net revenu',x='Year-Month')


################################## Partie ventes net ####################################
st.header('Ventes net par mois')

df_ventes_net=pd.read_excel(chemin_relatif_ventes_net,
                            sheet_name='Data',
                            skiprows=4,
                            usecols=[1,2],
                            names=['Year-Month','Net ventes']
                             )

#st.write(df_ventes_net)

st.line_chart(data=df_ventes_net,y='Net ventes',x='Year-Month')
