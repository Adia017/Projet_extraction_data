import requests 
import pandas as pd 
import bs4

#On recupere le contenu brut de la page
# url_api= " https://fr.wikipedia.org/wiki/Liste_des_pays_par_population"
# req = requests.get(url_api)

# # On utilise beautifulsoup pour formater le code source
# page = bs4.BeautifulSoup(req.text, "html.parser")

# #On recupere le tableau
# tab = page.find("table")

# #Puis on traite chaque ligne 
# res = []
# for line in tab.find_all("tr"):
#     elems = line.find_all("td")
#     resline = [] 
#     for elem in elems:
#         resline = resline +[elem.text.strip()]
#     res = res+[resline]
# print(res)


# EXO1:
#  pr afficher la liste des liens prépsents on exécutera:
# url = " https://fr.wikipedia.org/wiki/Liste_des_pays_par_population"
# req1 = requests.get(url)
# page1 = bs4.BeautifulSoup(req1.text, "html.parser")
# link= page1.find_all("a") # recherche toute les balises <a>


# for line in link:
#     href = line.get('href')
#     if href: #si href trouvé
#         print(href)
    
#NB: L'élément HTML <a> (pour ancre ou anchor en anglais), 
# avec son attribut href, crée un lien hypertexte vers des pages web, 
# des fichiers, des adresses e-mail, des emplacements se trouvant dans la même page, 
# ou tout ce qu'une URL peut adresser   





# EXO2:
#  liste des rois de france  avec leur date de règne.
# url_k = "https://fr.wikipedia.org/wiki/Liste_des_monarques_de_France"
# req2 = requests.get(url_k)
# page2 = bs4.BeautifulSoup(req2.text, 'html.parser')

# data = page2.find_all('table') # retourne une liste de toutes les tables


# # print(df.columns) nous montre les différentes colonnes de notre table 
# # print(df)

# # liste pour stocker tous les data frames
# dfs=[]

# for table in data:
#     df = pd.read_html(str(data))[0]
#     df = df[['Nom', 'Début du règne', 'Fin du règne']] # Sélectionner les colonnes désirées
#     dfs.append(df) #ajouter la table à la liste
    
#     # concaténer les df en un seul 
#     final_df = pd.concat(dfs, ignore_index=True)
#     final_df.to_csv("Monarque_France_1.csv")

    
    
    
    
    
    
    
    
    
    
# Exo3:
# Programme permettant de vérifier
#api_key=2ad3ae343017d22fb20ae9368381ee5f
# automatiquement si deux acteurs donnés ont déjà joué ensemble.
# url_m = "https://fr.wikipedia.org/wiki/Filmographie_de_John_Wayne" 
# req_m = requests.get(url_m)
# # print(req_m)
# page_m = bs4.BeautifulSoup(req_m.text, 'html.parser')
# data_m = page_m.find_all('table') # retourne une liste de toutes les tables
# dfs_m=[]
# for table in data_m:
#     df_m = pd.read_html(str(table))[0]
#     df_m = df_m[['Titre français']] # Sélectionner les colonnes désirées
#     # print(df_m.columns) # Sélectionner les colonnes désirées
#     dfs_m.append(df_m) #ajouter la table à la liste
# # print(dfs_m)

# # liens wiki des films 
# wiki=[]
# for df in dfs_m:    
#     for title in df['Titre français'].dropna(): #drop.na(): est une méthode retirant les valeurs manquantes 
#         dfs_m_rep = title.replace(" ", "_")
#         wiki_ = f"https://fr.wikipedia.org/wiki/{dfs_m_rep}"
#         wiki.append(wiki_)

# # print(wiki[:5])
# films_acteurs = {}
# for film in wiki:
#     req = requests.get(film)
#     page = bs4.BeautifulSoup(req.text, "html.parser")
#     for th in page.find_all("th"):
#          if th.get_text()== "Acteurs principaux":
#              td = th.find_next_sibling('td')
#              acteurs= [a.get_text() for a in td.find_all('a')]
#              titre = page.find('h1').get_text()
#              films_acteurs[titre] = acteurs
# # print(films_acteurs.items())

# # fonction pour vérifier si deux acteurs on joués ensemble
# def ont_il_joué(acteur1,acteur2,dico):
#     for film , acteurs in dico.items():
#         if  acteur1 in acteurs and acteur2 in acteurs:
#             return True, film # retourne le film ou ils ont joué 
#     return False, None # Si pas de film trouvé

# res = ont_il_joué('John Wayne', 'Aaron Pierre', films_acteurs)
# print(res)
# for line in link:
#     href = line.get('href')
#     if href: #si href trouvé
#         print(href)
    


#  concaténer les df en un seul 
    # final_df_m = pd.concat(dfs_m, ignore_index=True)
    # final_df_m.to_csv("Movie_James_Wayne.csv")

# trouver les co-acteurs de chaque film.
# pour cela il nous faudra visiter les wikipedia de chaque film afin de pouvoir les récupérer.


#Exo4:
#Récupérer des données sur trois sites d’info de votre choix, proposez un programme permettant de
#générer un fichier csv affichant les titres et les liens vers les infos du jour.


# SYstème d'infos choisis
BBC_url = "https://www.bbc.com/news"

#Requête HTTP pour récupérer le contenu de la page
BBC_req = requests.get(BBC_url)
BBC_page = bs4.BeautifulSoup(BBC_req.text, "html.parser")
# On utilise beautifulsoup pour formater le code source

recup = BBC_page.find_all('ul',class_='gs-c-promo-heading')
# fonction pour chaque site qui récupère les titres et les liens des articles du jour.

data_BBC = []
for article in recup:
    title = article.get_text(strip=True)
    lien = "https://www.bbc.com/" + article['href'] # construis le lien
    data_BBC.append((title,lien)) # les ajoute à la liste 

for link in data_BBC:
    print (link)

print(data_BBC)

