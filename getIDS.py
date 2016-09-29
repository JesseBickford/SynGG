import pandas as pd
from cassiopeia import riotapi
from cassiopeia.type.api.exception import APIError

data = pd.read_csv('/Users/Starshine/DSI/Sandbox/SynGG/top1000.csv', encoding='utf-8')
data.dropna(inplace=True) #drop missing values
data = data[data.Realm.str.contains("JP") == False]    #for some reason the riot api thinks "jp" isn't a region
data

idsdf = pd.DataFrame()   #create a dataframe to store the IDs

def getid(df):
    riotapi.set_api_key("Your Key Here")     #set your API key here
    idlist = []         #create an empty list to store the IDs
    for realm, name in zip(data.Realm, data.Names):          #for loop calling two series of the data dataframe
        try:                                                 #try allows for exceptions
            riotapi.set_region(realm)
            summoner = riotapi.get_summoner_by_name(name)
            idlist.append(summoner.id)
        except APIError as error:       #if there's a 404, it skips and moves on
            if error.error_code in [400, 404]:
                continue
        except AttributeError, UnicodeEncodeError:  #if there's an AttributeError or UnicodeEncodeError, move on
            continue
    iddf = pd.DataFrame({'IDs': idlist})
    return iddf

idsdf = getid(idsdf)

idsdf.to_csv('IDs.csv', index=False)
