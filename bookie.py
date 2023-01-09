from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from classes import Bookie
from classes import Fighter
from classes import Match
from module import moneyline_to_frac
from pybet365 import Bet365
from pybet365 import Bet365SportId
class Bet365Bookie(Bookie):
    def collect_mma(self):
        matches =[]
        #figure out how to make API calls
        client = Bet365(api_host="someHost", api_key="someKey")
        upcoming_events = client.upcoming_events(sport_id=Bet365SportId.BOXING_UFC)
        print(upcoming_events)

        return matches

class EightEightEightSports(Bookie):
    def collect_mma(self, driver):
        matches = []
        driver.implicitly_wait(3)
        driver.get(self.website)
        cards = driver.find_elements(By.CLASS_NAME, "bet-card")
        for card in cards:
            fighters = card.find_elements(By.CLASS_NAME, "featured-matches-widget__competitor-wrapper")
            match_fighters = []
            for fighter in fighters:
                full_name = fighter.text.split(', ')
                match_fighters.append(Fighter(full_name[1], full_name[0]))
            bets = card.find_elements(By.CLASS_NAME, "bb-sport-event__selection")
            matches.append(FightMatch(match_fighters[0], match_fighters[1], float(bets[0].text), float(bets[1].text), self.name,
                           self.name))
        return matches

class DraftKings(Bookie):
    def collect_mma(self,driver):
        matches = []
        driver.implicitly_wait(3)
        driver.get(self.website)
        cards = driver.find_elements(By.CLASS_NAME, "sportsbook-event-accordion__children-wrapper")
        for card in cards:
            fighters = card.find_elements(By.CLASS_NAME, "sportsbook-outcome-cell__label-line-container")
            match_fighters = []
            for fighter in fighters:
                full_name = fighter.text.split()
                match_fighters.append(Fighter(full_name[0], full_name[1]))
            bets = card.find_elements(By.CLASS_NAME, "sportsbook-outcome-cell__element")
            bet_a = moneyline_to_frac(bets[1].text)
            bet_b = moneyline_to_frac(bets[3].text)
            matches.append(FightMatch(match_fighters[0], match_fighters[1], bet_a, bet_b, self.name, self.name))
        return matches

class PointsBet(Bookie):
    def collect_mma(self,driver):
        matches = []
        driver.implicitly_wait(3)
        driver.get(self.website)
        cards = driver.find_elements(By.CLASS_NAME, "f1oyvxkl")
        for card in cards:
            fighters = card.find_elements(By.CLASS_NAME, "f5rl2hl")
            match_fighters = []
            for fighter in fighters:
                full_name = fighter.text.split()
                match_fighters.append(Fighter(full_name[0], full_name[1]))
            bets = card.find_elements(By.CLASS_NAME, "fsuivmx")
            bet_a = moneyline_to_frac(bets[0].text)
            bet_b = moneyline_to_frac(bets[1].text)
            matches.append( FightMatch(match_fighters[0], match_fighters[1], bet_a, bet_b, self.name, self.name))
        return matches
class SportsInteractive(Bookie):
    def collect_mma(self,driver):
        matches =[]
        driver.implicitly_wait(3)
        driver.get(self.website)
        cards = driver.find_elements(By.CLASS_NAME, "Game__events")
        for card in cards:
            fighters = card.find_elements(By.CSS_SELECTOR,
                                          ".BetButton--row .BetButton__runnerNameHandicap[data-v-b4e8dc7c]")
            match_fighters = []
            for fighter in fighters:
                full_name = fighter.text.split()
                match_fighters.append(Fighter(full_name[0], full_name[1]))
            bets = card.find_elements(By.CSS_SELECTOR, ".BetButton__price[data-v-b4e8dc7c]")
            bet_a = moneyline_to_frac((bets[0].text))
            bet_b = moneyline_to_frac((bets[1].text))
            matches.append(FightMatch(match_fighters[0], match_fighters[1], bet_a, bet_b, self.name, self.name))
        return matches
