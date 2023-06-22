## l'histoire de Ubisoft
import streamlit as st
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path
import os

st.set_page_config(
    page_title="Analyse ubisoft",
    page_icon="👋",
)

# recuperation du chemin relatif du fichier de répartition des salariés
lien = r"C:\Applications\Espace_Projet\Projet_Streamlit\.venv\Images\Logo_Ubisoft.PNG"
chemin_absolu = os.path.abspath(lien)
dossier_actuel = os.getcwd()
chemin_relatif_logo_ubisoft = os.path.relpath(chemin_absolu, dossier_actuel)

#Affichage de l'image Logo Ubisoft
image = Image.open(chemin_relatif_logo_ubisoft)
st.image(image, caption='Logo Ubisoft')

st.markdown("""Pour notre projet nous avons décidé de nous focaliser sur l’éditeur UBISOFT et plus précisément sur la franchise à succès Assasin's Creed """ )

st.markdown( """Ubisoft est une entreprise française de développement, d’édition et de distribution de jeux video. En 30 ans, elle est devenue l’un des leaders mondiaux du jeu video en développant des jeux connus dans le monde entier et utilisés par des millions de joueurs, comme Just Dance, Prince of Persia, Assassin’s Creed ou encore Lapins Crétins.""")

st.markdown( 
"""
- UBISOFT développe des jeux multi plateformes (Playstation , Nintendo, Xbox, Mobile, …)
- UBISOFT est un developpeur et éditeur qui utilise son propre moteur graphique
- 6 franchises à succès , 11 titres , avec pour chacun plus de 10 millions d’unités vendus dans le monde
- UBISOFT est un éditeur français à rayonnement internationale (analyse comparative avec d’autres boites mondiales ET  francaises , salariés, …)
"""
)


def main():
    toggle_text = st.button("Vous voulez en savoir plus ? ")

    if toggle_text:
        if "text_visible" not in st.session_state:
            st.session_state.text_visible = True
        else:
            st.session_state.text_visible = not st.session_state.text_visible

    if "text_visible" in st.session_state and st.session_state.text_visible:
        st.write("""L’histoire d’Ubisoft commence dans les années 80 en Bretagne. Les cinq frères Guillemot (Claude, Michel, Yves, Gérard et Christian) veulent diversifier les activités de l’entreprise familiale spécialisée dans les produits agricoles. Ils se tournent alors vers la vente de petits ordinateurs. Lors d’un voyage en Angleterre, Michel Guillemot découvre que les jeux vidéo y sont moins chers qu’en France. De retour en France, il lance un service de distribution de jeux. Les ventes dépassant largement ses attentes,  il se rend compte de tout le potentiel de ce marché.
                 -En 1988, Yves Guillemot devient le PDG de la société en croissance exponentielle.
- 1990, la société sort son premier jeu, basique mais novateur, Zombi, sur Amstrad, premier succès commercial
- Rayman en 1994 connait un succès mondial. En 10 ans, le jeu se vendra à 15 millions d’exemplaires
- Tom Clancy en 2002 connait un tel succès que les stocks européens sont épuisés en moins de 24h
- Prince of Persia : 1,1 millions de jeux vendus en trois mois
- Lapins Crétins en 2006
- Assassin’s Creed en 2007 est salué par la critique pour son ambition, son audace et son esthétique. Le jeu se vend à 3 millions d’exemplaires en moins de deux mois. Le jeu deviendra une des franchises les plus populaires de tous les temps, avec plus de 150 millions d’exemplaires vendus à ce jour.
- Just Dance en 2009 : plus de 40 millions de jeux vendus à ce jour
 - Watch Dogs lancé en 2014 rencontre un succès commercial avec 4 millions d’exemplaires en une semaine, le jeu le plus vendu au monde à son lancement
""")

if __name__ == "__main__":
    main()

df=pd.read_excel("C:\Applications\Espace_Projet\Projet_Streamlit\.venv\DataFrame\statistic_id1366802_ubisoft-all-time-game-title-unit-sales-worldwide-2022.xlsx",
                 sheet_name='Data',
                 header=4,
                 usecols=[1,2],
                 index_col=False,
                 names=["Jeux","ventes"])
df['ventes']=df["ventes"].str.split(pat='m',expand=True)[0]
df['ventes']=df['ventes'].astype('int64')
st.header("Volume de ventes de jeux Ubisoft depuis 2022")

st.bar_chart(data=df,x='Jeux',y='ventes')
###################


from streamlit_timeline import st_timeline

items = [
    {"id": 1, "content": "Assasin's creed", "start": "2007","style": "color: black; background-color: #a9a9a98F;"},
    {"id": 2, "content": "Assassin's Creed II", "start": "2009"},
    {"id": 3, "content": "Assassin's Creed: Brotherhood", "start": "2010"},
    {"id": 4, "content": "Assassin's Creed: Revelations", "start": "2011"},
    {"id": 5, "content": "Assassin's Creed III", "start": "2012"},
    {"id": 6, "content": "Assassin's Creed IV: Black Flag", "start": "2013"},
    {"id": 7, "content": "Assassin's Creed: Rogue", "start": "2014"},
    {"id": 8, "content": "Assassin's Creed: Unity", "start": "2014"},
    {"id": 9, "content": "Assassin's Creed: Syndicate", "start": "2015"},
    {"id": 10, "content": "Assassin's Creed Origins", "start": "2017"},
    {"id": 11, "content": "Assassin's Creed Odyssey", "start": "2018"},
    {"id": 12, "content": "Assassin's Creed Valhalla", "start": "2018"},
    {"id": 13, "content": "Assassin's Creed Odyssey", "start": "2020"},
    {"id": 14, "content": "Assassin's Creed: Mirage", "start": "2023"}]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)


