import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Skywalker\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://cis.ncu.edu.tw/iNCU/academic/course/courseEvaluate?groupName=wpsNone&loginName=07B707BE05F90152064B011F0240082D064B07BE0721062E&sn=454080071&systemId=57&verifyName=MTEwNDAzNTI1")
time.sleep(3)

login = driver.find_element(By.XPATH, "//*[@class = 'btn btn-primary']")
login.click()
time.sleep(1)
go_to = driver.find_element(By.XPATH, "//*[@class = 'btn btn-primary']")
go_to.click()
time.sleep(3)
forms = driver.find_elements(By.XPATH, "//*[@class = 'btn btn-default']")

for i in range(len(forms)):
    forms = driver.find_elements(By.XPATH, "//*[@class = 'btn btn-default']")
    forms[i].click()
    time.sleep(1)

    try:
        radios = driver.find_elements(By.XPATH, "//input[@type='radio' and @value='A']")
        for radio in radios:
            if not radio.is_selected():
                radio.click()
    except:
        pass

    try:
        textarea = driver.find_element(By.XPATH, "//*[@class = 'form-control']")
        textarea.send_keys("謝謝老師！")
    except:
        pass
    time.sleep(1)
    submit = driver.find_element(By.XPATH, "//*[@class = 'btn btn-light btn-default']")
    submit.click()
    time.sleep(1)


time.sleep(5)
driver.quit()