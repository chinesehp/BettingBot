from module import *

class Match:
    def __init__(self, a, b, odds_a, odds_b, bookie_a, bookie_b):
        self.a = a
        self.b = b
        self.odds_a = odds_a
        self.odds_b = odds_b
        self.bookie_a = bookie_a
        self.bookie_b = bookie_b
        self.arb = (1 / odds_a + 1 / odds_b) * 100

    def print(self):
        if(self.arb<=100 or True):
            result = "ARB|A|BET A|BOOKIE A|B|BET B|BOOKIE B|\n"+str(self.arb) + "|" + self.a.name + "|"+ str(self.odds_a) + "|"+ self.bookie_a + "|" + self.b.name + "|" + str(self.odds_b) + "|" + self.bookie_b
            print(result)
            #send_mail(result)
    def calc_arb(self):
        self.arb = (1 / self.odds_a + 1 / self.odds_b) * 100



class Fighter:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = last_name

class Team:
    def __init__(self,name):
        self.name = name

class Bookie:
    def __init__(self, name, website):
        self.name = name
        self.website = website

    def collect_mma(self):
        return []
