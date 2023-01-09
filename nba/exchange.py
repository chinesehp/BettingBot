from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


exchange = "https://smarkets.com/listing/sport/basketball/nba"


service = Service(executable_path=r'C:\browserdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(exchange)

WebDriverWait(driver, timeout=10).until(lambda d: d.find_elements(By.XPATH,"//*[@id='main-content']/main/div[2]/ul/li"))
list_size = len(driver.find_elements(By.XPATH,"//*[@id='main-content']/main/div[2]/ul/li"))
for i in range(1,list_size+1):
    cur_string ="//*[@id='main-content']/main/div[2]/ul/li["+str(i)+"]/div[2]"
    data = driver.find_element(By.XPATH,cur_string)
    try:
        items = data.find_elements(By.CLASS_NAME,"contract-item ")
        for item in items:
            team = item.find_element(By.CLASS_NAME,"contract-label")
            print("Team:",team.text)

            back = float(item.find_element(By.CLASS_NAME,"offer").find_element(By.TAG_NAME,"span").text)
            lay= float(item.find_element(By.CLASS_NAME,"bid").find_element(By.TAG_NAME,"span").text)
            true_odds = (back+lay)/2.0
            print("True Odds:",true_odds,"||","Chances of Win:",1/true_odds *100)
    except:
        print("TEAM UNAVAILABLE")


    print("----")



driver.quit()




