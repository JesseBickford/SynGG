from bs4 import BeautifulSoup
import urllib
import pandas as pd

#create an empty dataframe to be filled
master_df = pd.DataFrame()

#create a function to grab the names on a page
def getnames(url, df):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")
    names = [] #set an empty list to fill with the names
    realm = [] #sent an empty list to till the realms
    for user in soup.findAll('i', {'class': 'show-for-small-down-custom'}):
        names.append(user.parent.findChildren()[0].renderContents()) #append the names to names list
        realm.append(user.parent.findChildren()[2].renderContents()) #append the realm to realm list
    data = pd.DataFrame({'Names': names, 'Realm': realm}) #create a dataframe joining the lists
    concat_df = pd.concat([df, data], ignore_index = True) #add this dataframe with the other dataframes that have been created
    return concat_df

#set the url head for building the complete url later
url_head = 'http://www.leagueofgraphs.com/rankings/summoners/page-'

#this range will mine 10 pages
url_tail = range(1,11)

#this loop builds the url and runs the getnames function, mining 10 pages of names and adding to a master dataframe
for i in url_tail:
    url = url_head + str(i)
    master_df = getnames(url, master_df)

#save to csv if desired
master_df.to_csv('top1000.csv', index=False, encoding='utf-8')
