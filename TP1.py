import requests 
import pandas as pd
import json
"""Exo1:"""
"""3. produit marque Heudebert"""
"""3. pour le nom des produits on procédera comme suite """
"""url_api3 = "https://fr.openfoodfacts.org/api/v2/search?products=Heudebert"

req = requests.get(url_api3)
wb = req.json()
df = pd.json_normalize(wb["products"])

print(df["product_name"])"""


"""2."""
"""5449000131805: correspond au coca-cola zero"""
"""3155250358788: correspond a Primevere"""
"""5411188119098 Natur mit Kokosnuss"""
"""8715700407760: Tomato Ketchup BIO"""

"""4. le produit avec le meilleure nutriscore est le fanta"""
url_api4 = "https://fr.openfoodfacts.org/api/v2/search?categories_tags=sodas"

req = requests.get(url_api4)
wb = req.json()
df = pd.json_normalize(wb["products"])

a=df[["nutriscore_score", "product_name"]]
max_=max(df["nutriscore_score"])
# pour le savoir il a fallut procéder de la manière suivante:
# print(a[a["nutriscore_score"]==max_])
"""print(df["product_name"])"""
"""df.to_json("dat.json")"""




# Exo2:
#DANS CETTE PARTIE DE L'exo je reférence les différentes données permettant de réaliser la visualisation demandée
url_api83="https://archive-api.open-meteo.com/v1/archive?latitude=44.9254&longitude=2.4398&start_date=1983-01-01&end_date=1983-12-31&daily=weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,sunrise,sunset,daylight_duration,sunshine_duration"
req = requests.get(url_api83)
wb83 = req.json()
# print(wb)
df83 = pd.json_normalize(wb83["daily"])
df83= df83[["time","temperature_2m_max" ,"temperature_2m_min"]]
df83.to_json("weather83.json")
# print(df83)



url_api03 = "https://archive-api.open-meteo.com/v1/archive?latitude=44.9254&longitude=2.4398&daily=weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,sunrise,sunset,daylight_duration,sunshine_duration"
req = requests.get(url_api03)
wb03 = req.json()
# print(wb)
df03 = pd.json_normalize(wb03["daily"])
df03= df03[["time","temperature_2m_max" ,"temperature_2m_min"]]
df03.to_json("weather03.json")
# print(df03)



url_api13 = "https://archive-api.open-meteo.com/v1/archive?latitude=44.9254&longitude=2.4398&daily=weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,sunrise,sunset,daylight_duration,sunshine_duration"
req = requests.get(url_api13)
wb13 = req.json()
# print(wb)
df13 = pd.json_normalize(wb13["daily"])
df13= df13[["time","temperature_2m_max" ,"temperature_2m_min"]]
df13.to_json("weather13.json")
# print(df13)



url_api23 = "https://archive-api.open-meteo.com/v1/archive?latitude=44.9254&longitude=2.4398&daily=weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,sunrise,sunset,daylight_duration,sunshine_duration"
req = requests.get(url_api23)
wb23 = req.json()
# print(wb)
df23 = pd.json_normalize(wb23["daily"])
df23= df23[["time","temperature_2m_max" ,"temperature_2m_min"]]
df23.to_json("weather23.json")
# print(df23)

# exercice3:
# Artiste les plus représentés au Met Museum
url_object="https://collectionapi.metmuseum.org/public/collection/v1/objects"
req_ms= requests.get(url_object)          
wbmuse=req_ms.json()
# print(wbmuse)
# obtenons l'url de nos IDs
objet_ids=wbmuse["objectIDs"][:50]

objet_artis=[]  
for obj in objet_ids:
    obj_info=f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj}"
    req_obj= requests.get(obj_info)
    wbms = req_obj.json()
          
    # print(obj_info)

    if "artistDisplayName" in wbms:
        objet_artis.append({
            "objectID": wbms.get("objectID"),
            "artistDisplayName":wbms.get("artistDisplayName")  
        })



df_artistes= pd.DataFrame(objet_artis)
print(df_artistes)