import pandas as pd
from cassiopeia import riotapi
from cassiopeia.type.api.exception import APIError

data = pd.read_csv('/Users/Starshine/DSI/Sandbox/top1000.csv')
data.dropna(inplace=True) #drop missing values
data = data[data.Realm.str.contains("JP") == False]    #for some reason the riot api thinks "jp" isn't a region

data
def getid():
    riotapi.set_api_key("RGAPI-1974219A-1DD3-4D8E-8035-D4A89C9A75DA")
    idlist = []
    for realm, name in zip(data.Realm, data.Names):
        riotapi.set_region(realm)
        summoner = riotapi.get_summoner_by_name(name)
        idlist.append(summoner.id)

    iddf = pd.DataFrame({'IDs': idlist})
    return iddf

getid()
