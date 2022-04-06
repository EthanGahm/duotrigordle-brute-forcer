from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

first_word = ""

while len(first_word) != 5 or not first_word.isalpha:
    first_word = input("Choose an initial 5-leter word: ")

s = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=s, chrome_options=options)

driver.get("https://duotrigordle.com/")

driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Practice')]").click()

while True:
    actions = ActionChains(driver)
    actions.send_keys(first_word)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    actions.reset_actions()
    if "0/32" in driver.page_source:
        driver.find_element(by=By.XPATH, value="//*[contains(text(), 'New')]").click()
        alert = Alert(driver)
        alert.accept()
    else:
        print("Done!")
        break
    
