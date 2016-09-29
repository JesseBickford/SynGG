import pandas as pd
from cassiopeia import riotapi
from cassiopeia.type.api.exception import APIError

data = pd.read_csv('/Users/Starshine/DSI/Sandbox/SynGG/top1000.csv', encoding='utf-8')
data.dropna(inplace=True) #drop missing values
data = data[data.Realm.str.contains("JP") == False]    #for some reason the riot api thinks "jp" isn't a region

def getid():
    riotapi.set_api_key("Your Key Here")
    idlist = []
    for realm, name in zip(data.Realm, data.Names):
        try:
            riotapi.set_region(realm)
            summoner = riotapi.get_summoner_by_name(name)
            idlist.append(summoner.id)
            print summoner, summoner.id
        except APIError as error:       #if there's a 404, it skips and moves on
            if error.error_code in [400, 404]:
                continue
    iddf = pd.DataFrame({'IDs': idlist})
    return iddf

getid()
