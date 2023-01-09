import ssl

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from classes import *
from module import *
from bookie import *


bookie_draftkings = "https://sportsbook.draftkings.com/leagues/mma/ufc"
bookie_888sports = "https://www.888sport.ca/mma/"
bookie_pointsbet ="https://on.pointsbet.ca/sports/mma/UFC"
bookie_sportsinter="https://on.sportsinteraction.com/mma-betting/"
bookie_fanduel  ="https://canada.sportsbook.fanduel.com/en/sports/navigation/7287.1/"
bookie_bodog ="https://www.bodog.eu/sports/ufc-mma"
bookie_unibet ="https://on.unibet.ca/sports#sports-hub/ufc_mma"
bookie_caesars= "https://sportsbook.caesars.com/ca/on/bet/ufcmma/events/all"

service = Service(executable_path=r'C:\browserdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)


matches = []
final = []
BookieA = DraftKings("DraftKings",bookie_draftkings)
BookieB = EightEightEightSports("888Sports",bookie_888sports)
BookieC = PointsBet("PointsBet",bookie_pointsbet)
BookieD = SportsInteractive("Sports Interactive",bookie_sportsinter)

final = BookieA.collect_mma(driver)

matches =BookieB.collect_mma(driver)
for finalMatch in final:
    for match in matches:
        if(is_in(finalMatch,match)):
            finalMatch=(compare_matches(finalMatch,match))

matches=(BookieC.collect_mma(driver))
for finalMatch in final:
    for match in matches:
        if(is_in(finalMatch,match)):
            finalMatch=(compare_matches(finalMatch,match))

matches=((BookieD.collect_mma(driver)))
for finalMatch in final:
    for match in matches:
        if(is_in(finalMatch,match)):
            finalMatch=(compare_matches(finalMatch,match))




matches=[]
driver.get(bookie_bodog)
cards = driver.find_elements(By.TAG_NAME,"sp-coupon")
for event in cards:
    try:
        fighters = event.find_element(By.CLASS_NAME,"event-title").find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"div").find_elements(By.TAG_NAME,"h4")
        match_fighters = []
        for fighter in fighters:
            full_name = fighter.text.split()
            match_fighters.append(Fighter(full_name[0],full_name[1]))
        bets = event.find_element(By.CLASS_NAME,"markets-container").text.split("\n")
        match_bets =[]
        for bet in bets:
            if(bet=="EVEN"):
                match_bets.append(1)
            else:
                match_bets.append(moneyline_to_frac(bet))

        matches.append(FightMatch(match_fighters[0],match_fighters[1],match_bets[0],match_bets[1],"Bodog","Bodog"))

    except:
       print("INVALID")
for finalMatch in final:
    for match in matches:
        if(is_in(finalMatch,match)):
            finalMatch=(compare_matches(finalMatch,match))

matches =[]
driver.get(bookie_fanduel)
cards = driver.find_elements(By.CLASS_NAME,"event")
for card in cards:
    try:
        match_fighters =[]
        fighters = card.find_elements(By.CSS_SELECTOR,".coupon-event.twoselections .names.participants .name")
        match_fighters = []
        for fighter in fighters:
            full_name = fighter.text.split()
            match_fighters.append(Fighter(full_name[0], full_name[1]))
        bets = card.find_elements(By.CSS_SELECTOR,".selection .selection-wapper .value .selectionprice[data-v-7f128c6a]")
        match_bets =[]
        for bet in bets:
            match_bets.append(moneyline_to_frac(bet.text))
        matches.append(FightMatch(match_fighters[0], match_fighters[1], match_bets[0], match_bets[1], "FanDuel", "FanDuel"))
    except:
        print("INVALID")

for finalMatch in final:
    for match in matches:
        if(is_in(finalMatch,match)):
            finalMatch=(compare_matches(finalMatch,match))

matches = []
driver.get(bookie_unibet)
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"KambiBC-sandwich-filter__list"))
cards = driver.find_element(By.CLASS_NAME,"KambiBC-sandwich-filter__list").find_elements(By.TAG_NAME,"li")

for card in cards:
    try:

        buttons = card.find_element(By.CLASS_NAME,"KambiBC-bet-offer__outcomes").find_elements(By.TAG_NAME,"button")
        match_fighters =[]
        match_bets = []
        for button in buttons:
            data = button.text.split("\n")
            fighter = data[0].split()
            if fighter[0][-1]==",":
                fighter[0] = fighter[0][0:len(fighter[0])-1]
            match_fighters.append(Fighter(fighter[1],fighter[0]))
            match_bets.append(moneyline_to_frac(data[1]))
        matches.append(FightMatch(match_fighters[0],match_fighters[1],match_bets[0],match_bets[1],"UNIBET","UNIBET"))
    except:
        print("invalid")
for finalMatch in final:
    for match in matches:
        if(is_in(finalMatch,match)):
            finalMatch=(compare_matches(finalMatch,match))
"""
driver.get(bookie_caesars)
cards = driver.find_elements(By.CLASS_NAME,"teamNameSection")
for card in cards:
    print(card.text)
    
    
"""
for i in final:
    i.print()

driver.quit()

