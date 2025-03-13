import csv
import requests 
import pandas as pd 
import bs4


# https://www.procyclingstats.com/
# c'est un site qui presente les stats sur le cyclisme
# Les données qu'on doit récupérer : 
# les top 10 de chaque course, 
# les infos des courses (distance, vitesse moyenne, dénivelé), 
# et les infos des coureurs (pays, taille poids, age, equipe, notes, 
# classements mondiaux)
# note : pas d'utilisation d'api, juste scraper


# extraction des liens des courses de 2024
url_course = "https://www.procyclingstats.com/races.php?year=2024"
res= requests.get(url_course)
page = bs4.BeautifulSoup(res.text, 'html.parser')

liste_course = page.find('table', class_ = "basic") # retourne une liste de toutes les tables

if not liste_course:
    print("Tableau des résultats introuvable")
    exit()
    
#lignes du tableau
rows = liste_course.find_all('tr')


l_liens=[]
for link_course in rows[1:]:
    
    cols_=  link_course.find_all('td')
    lien=cols_[2].find('a', href=True)
    
    if lien:
        full_url= f"https://www.procyclingstats.com/{lien['href']}"
        l_liens.append(full_url)


# for l in l_liens: 
#     print(l)

#de ces liens nous allons extraire le top10 des cyclistes


#fichier csv pour enregistrer les résultats
with open('top_10_races_.csv', 'w', newline='',encoding='utf-8' ) as file:
    writer = csv.writer(file)
    writer.writerow(['Race' , 'Rank' , 'Rider' , 'Age' , 'Team' , 'Time' ]) # sont les en-tête
    

    # création d'une boucle pour l'extraction 
    for li in l_liens: 
        response  = requests.get(li)
        page = bs4.BeautifulSoup(response.text, "html.parser")
        table = page.find('table', class_ = 'results basic moblist10')

        #Vérification de l'existence du tableau
        if not table:
            print("Tableau des résultats introuvable")
            continue

        # lignes du tableau
        rows = table.find_all('tr')

    # Extraire le nom des courses  à partir des liens
        race_name = li.split('/')[-3].replace('-', ' ')
        race_name = race_name.title()


    #Liste pour stocker les résultats
        top_10 = []
            
        for row in rows[1:]:
            cols = row.find_all('td')
            
            if len(cols)<10: 
                continue
            
            rnk = cols[0].get_text(strip=True)
            
            # BIB = 1
            # H2H= 2
            # Speciality = 3
            
            #Vérifions si le nom du cycliste existe
            if cols[4].find('a') :
                rider = cols[4].find('a').get_text(strip=True) 
            elif cols[4].get_text(strip=True): 
                rider = cols[4].get_text(strip=True) or "NA"


            age = cols[5].get_text(strip=True)
            # Vérifier si l'age est un nombre 
            if not age.isnumeric():
                age = "NA"
                
            team = cols[6].find('a').get_text(strip=True) if cols[6].find('a') else "NA"
            # UCI= 7
            # Pnt = 8
            time=  cols[9].get_text(strip=True) if cols[9].find('a') else "NA"
            
            top_10.append((race_name , rnk , rider , age , team , time))
            
            if len(top_10)>= 10:
                break
            
            for result in top_10:
                writer.writerow([race_name,result[0],result[1],result[2],result[3],result[4]])
print("Fin du scraping!")

        
            
        
        
        
        
        
