#%%
import requests,pprint, json, time,re,shutil

#%%
url = 'https://api.scryfall.com/cards/search?q=set%3Asld+number>1570'
forest_info = requests.get(url).json()


#%%
response = requests.get(url)
print(response.status_code)


#%%
