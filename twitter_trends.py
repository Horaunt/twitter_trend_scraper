from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pymongo import MongoClient
from datetime import datetime, timezone
import uuid
import requests
import cred


# proxy = "http://Horaunt:Barsati@19@us-wa.proxymesh.com:31280"
options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % proxy)

driver = webdriver.Chrome(options=options)
driver.get('https://x.com/login')

time.sleep(5)


username = driver.find_element(By.NAME, 'text')
username.send_keys(cred.tusername)
username.send_keys(Keys.RETURN)
time.sleep(5)
password = driver.find_element(By.NAME, 'password')
password.send_keys(cred.tpassword)
password.send_keys(Keys.RETURN)


time.sleep(5)


driver.get('https://x.com/explore/tabs/keyword')
time.sleep(6)  


trend1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[4]/div/div/div/div/div[2]")
trend2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[5]/div/div/div/div/div[2]")
trend3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[6]/div/div/div/div/div[2]")
trend4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[7]/div/div/div/div/div[2]")
trend5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[8]/div/div/div/div/div[2]")

trending_topics = [
    trend1.text,
    trend2.text,
    trend3.text,
    trend4.text,
    trend5.text
]

driver.quit()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_trends']
collection = db['trends']

# Create a unique ID and insert the trends into the collection
document = {
    "unique_id": str(uuid.uuid4()),
    "trend1": trending_topics[0] if len(trending_topics) > 0 else "",
    "trend2": trending_topics[1] if len(trending_topics) > 1 else "",
    "trend3": trending_topics[2] if len(trending_topics) > 2 else "",
    "trend4": trending_topics[3] if len(trending_topics) > 3 else "",
    "trend5": trending_topics[4] if len(trending_topics) > 4 else "",
    "date_time": datetime.now(timezone.utc),
    "ip_address": requests.get('https://api.ipify.org').text  
}

collection.insert_one(document)
