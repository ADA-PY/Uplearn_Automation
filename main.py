import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

usr = "" 
pwd = "" 

# Improvements to code:
# 1) - Add other quizes to make the Xp dashboard more "believeable"
# 2) - find way to watch videos
# 3) - Research the console devtools JavaScript - utilisng the VAR functions and smthn to do with the wishquizlet network post request
# 4) - Research to see if the requesting the API is a better method
                                               
def loginmacro():
    driver.get("https://web.uplearn.co.uk/login")
    driver.maximize_window()
    usrlogin = driver.find_element(By.XPATH, '//*[@id="userEmail"]')
    pwdlogin = driver.find_element(By.XPATH, '//*[@id="userPassword"]')
    usrlogin.send_keys(usr)
    pwdlogin.send_keys(pwd)
    clicklogin = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/button')
    clicklogin.click()
    time.sleep(4)
    macroecon = driver.find_element(By.XPATH, '//*[@id="continue-button"]')
    macroecon.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(3)


loginmacro()

driver.get('https://app.uplearn.co.uk/learn/macroeconomics-1/circular-flow-of-income/practice-exam-quiz-3-quizzes')
time.sleep(4)

ade = 0


def quiz_run():
    driver.get('https://app.uplearn.co.uk/learn/macroeconomics-1/circular-flow-of-income/practice-exam-quiz-3-quizzes')
    global ade
    ade = ade + 1
    begin = driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[6]/div/button')
    begin.click()
    time.sleep(2)
    q1a = driver.find_element(By.XPATH, '//*[@id="optionsRadios4"]')
    q1a.click()
    time.sleep(2)
    ikit = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[1]/form/div[6]/div/button[1]')
    ikit.click()
    time.sleep(2)
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[1]/form/div[6]/button')
    submit.click()
    time.sleep(2)
    cont = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[1]/form/div[1]/button')
    cont.click()
    time.sleep(2)
    q1a = driver.find_element(By.XPATH, '//*[@id="optionsRadios2"]')
    q1a.click()
    time.sleep(2)
    ikit = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[2]/form/div[6]/div/button[1]')
    ikit.click()
    time.sleep(2)
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[2]/form/div[6]/button')
    submit.click()
    time.sleep(2)
    cont = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[2]/form/div[1]/button')
    cont.click()
    time.sleep(2)
    q1a = driver.find_element(By.XPATH, '//*[@id="optionsRadios1"]')
    q1a.click()
    time.sleep(2)
    ikit = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[3]/form/div[6]/div/button[1]')
    ikit.click()
    time.sleep(2)
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[3]/form/div[6]/button')
    submit.click()
    time.sleep(2)
    cont = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[3]/form/div[1]/button')
    cont.click()
    time.sleep(2)
    q1a = driver.find_element(By.XPATH, '//*[@id="input1"]')
    q1a.send_keys("320")
    time.sleep(2)
    ikit = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[4]/form/div[3]/div/button[1]')
    ikit.click()
    time.sleep(2)
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[4]/form/div[3]/button')
    submit.click()
    time.sleep(2)
    cont = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[4]/form/div[1]/button')
    cont.click()
    time.sleep(2)
    q1a = driver.find_element(By.XPATH, '//*[@id="optionsRadios3"]')
    q1a.click()
    time.sleep(2)
    ikit = driver.find_element(By.XPATH,
                               '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[5]/form/div[6]/div/button[1]')
    ikit.click()
    time.sleep(372)
    submit = driver.find_element(By.XPATH,
                                 '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[5]/form/div[6]/button')
    submit.click()
    time.sleep(3)
    cont = driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div[2]/div/div[1]/div/div/div[5]/form/div['
                                         '1]/button')
    cont.click()
    time.sleep(3)

    print(ade)


while ade != 17:                                       # 4hours of econ = ade=40 (looks legit w XP etc)
    quiz_run()
