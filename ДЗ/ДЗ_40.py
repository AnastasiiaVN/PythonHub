from bs4 import BeautifulSoup
import requests
import pandas as pd
base_url = 'https://www.marvel.com'

def get_chars():
    char_list = []
    limit = 10#ліміт отриманих реультатів
    offset = 2500#починає з
    resp  = requests.get(base_url + f'/v1/pagination/grid_cards?offset={offset}&limit={limit}&entityType=character&sortField=title&sortDirection=asc')
    result = resp.json()#обєкt преобразований в строку
    if result['code'] != 200: return #провірка чи получені данні
    for idx, c in enumerate(result['data']['results']['data']):
        character = {}
        print(f"{offset + idx }: {c['link']['title']}  ( {c['link']['link']} )")
        character['Name'] = c['link']['title']
        character['Link'] = base_url + c['link']['link']
        cm = requests.get(base_url + c['link']['link'] + '/in-comics' )
        if cm.status_code != 200:
            cm = requests.get(base_url + c['link']['link'])

        soup = BeautifulSoup(cm.content, 'html.parser')
        for info in soup.find_all('div', class_ = 'bioheader__charInfo'):
            for s in info.find_all('div', class_ = 'bioheader__stats'):
                l = s.find('p', 'bioheader__label')
                v = s.find('p', 'bioheader__stat')
                character[l.getText().capitalize()] = v.getText()
        char_list.append(character)
    return char_list

try:
    df = pd.read_csv('chars', index_col=[0])
except:
    df = pd.DataFrame(get_chars())
    df.to_csv('chars')

df.fillna('-', inplace=True)
print(df[['Name', 'Gender', 'Hair', 'Eyes', 'Weight']])