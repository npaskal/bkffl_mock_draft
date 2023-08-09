import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_fantasy_pros_adp_data(use_ppr = False):
    if not use_ppr:
        url = 'https://www.fantasypros.com/nfl/adp/half-point-ppr-overall.php'
        headers = ['RANK','PLAYER','POS','YAHOO','SLEEPER','RTSPORTS','AVG']
    else:
        url = 'https://www.fantasypros.com/nfl/adp/ppr-overall.php'
        headers = ['RANK','PLAYER','POS','ESPN','SLEEPER','NFL','RTSPORTS','FFC','AVG']
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table_rows = soup.find_all('tr')
    all_data = []
    for row in table_rows[:]:  # Skip the header rows
        columns = row.find_all('td')
        data = [col.text.strip() for col in columns]
        all_data.append(data)


    num_cols = len(headers)
    all_data = [row for row in all_data if len(row) == num_cols ]
    df = pd.DataFrame({column: row for column, row in zip(headers,zip(*all_data))}).set_index('RANK')
    df['POS'] = df['POS'].str[:2]
    df = df.loc[df['POS'].isin(['QB','RB','WR','TE'])]
    return df

def get_fantasy_pros_rankings_data():
    url = 'https://www.fantasypros.com/nfl/rankings/half-point-ppr-superflex-cheatsheets.php'
    headers = ['RK','TIERS','PLAYER NAME','TEAM','POS','BEST','WORST','AVG.','STD.DEV','ECR VS. ADP']
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')
    big_string = str(soup)
    rankings_str = big_string.split('var ecrData = {',1)[1].split('\"WR200\"',1)[0].split("\"players\":[",1)[1]
    pattern = r'\{(.*?)\}'
    matches = re.findall(pattern, rankings_str)
    def parse_field(header, str):
        return str.split("\"{}\":".format(header),1)[1].split(',',1)[0].replace('\"','').replace('null','-')
    players = [(
                parse_field('rank_ecr', row),
                parse_field('tier', row),
                parse_field('player_name', row),
                parse_field('player_team_id', row),
                parse_field('pos_rank', row),
                parse_field('rank_min', row),
                parse_field('rank_max',row),
                parse_field('rank_ave', row),
                parse_field('rank_std', row),
                parse_field('player_ecr_delta',row)
                )
               for row in matches]
    df = pd.DataFrame({column: row for column, row in zip(headers,zip(*players))})
    df['ECR VS. ADP'] = '-'
    for col_name in ['RK','TIERS','BEST','WORST']:
        df[col_name] = df[col_name].astype(int)
    for col_name in ['AVG.','STD.DEV']:
        df[col_name] = df[col_name].astype(float)
    return df







def scrape_espn_player_projections():
    url = 'https://www.espn.com/fantasy/football/story/_/page/21RanksPreseason300-PPR/mike-clay-2021-fantasy-football-preseason-projections-top-300-ppr'


    url = 'https://fantasy.espn.com/football/players/projections'
    # Configure Selenium to use a headless Chrome browser
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    # Wait for the dynamic content to load (you might need to adjust the waiting time)
    driver.implicitly_wait(10)

    # Find the elements containing the player data using appropriate XPath or CSS selectors
    player_elements = driver.find_elements_by_xpath('//table[@class="inline-table"]//tr')

    players = []
    positions = []
    projections = []

    for element in player_elements[1:]:  # Skip the header row
        columns = element.find_elements_by_tag_name('td')
        if len(columns) == 7:
            player_name = columns[1].text.strip()
            player_position = columns[2].text.strip()
            player_projection = float(columns[3].text.strip())

            players.append(player_name)
            positions.append(player_position)
            projections.append(player_projection)

    driver.quit()

    data = {'Player': players, 'Position': positions, 'Projection': projections}
    df = pd.DataFrame(data)
    return df




if __name__ == '__main__':
    adp_half = get_fantasy_pros_adp_data(use_ppr = False)
    adp_ppr= get_fantasy_pros_adp_data(use_ppr = True)
