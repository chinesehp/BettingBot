from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from classes import *
from module import *
from bookie import *
from selenium.webdriver.support.wait import WebDriverWait

bookie_draftkings = "https://sportsbook.draftkings.com/leagues/basketball/nba"
bookie_888sports = "https://www.888sport.ca/basketball/nba/"
bookie_betvictor = "https://www.betvictor.com/en-ca/sports/227/meetings/367476010/all"
bookie_sportsinter="https://on.sportsinteraction.com/basketball/nba-betting-lines/"



service = Service(executable_path=r'C:\browserdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)



driver.get(bookie_draftkings)
players = driver.find_elements(By.CLASS_NAME,"event-cell__name-text")
tables = driver.find_elements(By.CLASS_NAME,"sportsbook-table__body")
rows =[]
for table in tables:
    rows.extend(table.find_elements(By.TAG_NAME,"tr"))
count =1

names =[] #temp holds team names
matches = []
temp_teams = []
temp_bets = []
for row in rows:
    team = row.find_element(By.CLASS_NAME,"event-cell__name-text")
    bet = row.find_elements(By.CLASS_NAME,"sportsbook-table__column-row")[-1]
    temp_teams.append(Team(team.text))
    temp_bets.append(moneyline_to_frac(bet.text))
    if(count%2==0):
        matches.append(Match(temp_teams[0],temp_teams[1],temp_bets[0],temp_bets[1],"DraftKings","DraftKings"))
        temp_teams = []
        temp_bets= []
    count += 1

print(len(matches))
for match in matches:
    match.print()


matches =[]
driver.get(bookie_sportsinter)
games = driver.find_elements(By.CLASS_NAME,"MainMarketTable")
for game in games:
    players = game.find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"ul").find_elements(By.CLASS_NAME,"MainMarketTable__team")
    moneyline = game.find_element(By.CLASS_NAME,"MainMarketTable__events").find_elements(By.CLASS_NAME,"MainMarketTable__event")[1]
    bets = moneyline.find_element(By.CSS_SELECTOR,".MainMarketTable .MainMarketTable__eventButtons[data-v-ac214938], .MainMarketTable .MainMarketTable__teams[data-v-ac214938]").find_elements(By.TAG_NAME,"div")
    for i in range(2):
        print(players[i].text,bets[2*i].text)
    print("----------")





"""
driver.get(bookie_888sports)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_elements(By.CLASS_NAME,"bet-card"))
cards = driver.find_elements(By.CSS_SELECTOR,".featured-matches-widget .c-widgetcontainer .bet-card")

for card in cards:
    players =card.find_element(By.TAG_NAME,"div").find_elements(By.CLASS_NAME,"featured-matches-widget__competitor-wrapper")
    moneyline = card.find_element(By.CLASS_NAME,"bet-card__bet-buttons").find_elements(By.TAG_NAME,"div")[2]
    print(moneyline.text)
    bets = moneyline.find_elements(By.TAG_NAME,"div")
    for player in players:
        print(player.text)
    for bet in bets:
        print(bet.text)
    print("----------")
"""
driver.quit()