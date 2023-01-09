from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from classes import *
from module import *
from bookie import *

class SoccerMatch:
    def __init__(self):
        self.TeamA =""
        self.TeamB =""
        self.betA = 0
        self.betB = 0
        self.betDraw =0

service = Service(executable_path=r'C:\browserdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

bookie_bet365 ="file://D:/Users/steve/Downloads/Bet with bet365 – Live Online Betting Sportsbook – Latest Bets and Odds.html"
driver.get("https://canada.sportsbook.fanduel.com/en/sports/navigation/7287.1/9886.3")
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME,"gl-MarketGroupContainer "))
table = driver.find_element(By.CLASS_NAME,"gl-MarketGroupContainer ")

teams = driver.find_elements(By.CLASS_NAME,"rcl-ParticipantFixtureDetailsTeam_TeamName ")
num_teams = len(teams)
num_matches = num_teams/2
bets = driver.find_elements(By.CLASS_NAME,"sgl-ParticipantOddsOnly80_Odds")




bookie_si = "file://D:/Users/steve/Downloads/China Superleague Soccer Betting at Sports Interaction Sportsbook.html"
bookie_dk ="file://D:/Users/steve/Downloads/Chinese - Super League Betting Odds & Lines _ DraftKings Sportsbook.html"

