
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from csv import reader
driver = webdriver.Chrome(executable_path=r'/path/to/chromedriver')
driver.implicitly_wait(30)

def v2_user():
    # Login to NR1 and enter username and password
    driver.get("https://login.newrelic.com/login")
    driver.find_element(By.ID,"login_email").click()
    driver.find_element(By.ID,"login_email").clear()
    driver.find_element(By.ID,"login_email").send_keys("useremail@email.com")
    driver.find_element(By.ID,"login_submit").click()
    driver.find_element(By.ID,"login_password").click()
    driver.find_element(By.ID,"login_password").clear()
    driver.find_element(By.ID,"login_password").send_keys("somepassword")
    driver.find_element(By.ID,"login_submit").click()
    time.sleep(2)
    # Going to the user management page to start adding users
    driver.get("<ENTER USER MANAGEMENT URL HERE>")
    time.sleep(2)
    driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='SCIM Users'])[1]/following::span[1]").click()
    driver.find_element(By.XPATH,"//div[contains(text(),'Default')]").click()
    
    with open('userlist.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            time.sleep(2)
            # Click on the Add user button to add users then start adding information
            driver.find_element(By.XPATH,"//*/text()[normalize-space(.)='Add user']/parent::*").click()
            driver.find_element(By.XPATH,"//input[contains(@placeholder, 'Type the user na')]").click()
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/span/input").clear()
            # Add user Name
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/span/input").send_keys(row[0])
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/span/input").click()
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/span/input").clear()
            # Add email
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/span/input").send_keys(row[1])
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/button/span/span[1]").click()
            # Check if user is a basic or full user then add that
            if 'Full platform' in row[2]:
                driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Add user'])[2]/following::div[10]").click()
            elif 'Basic' in row[2]:
                driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Add user'])[2]/following::div[11]").click()
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/h3/div/div/div/div/button/span/span[1]").click()
            # Check what groups the user is assigned to and add accordingly
            if  'User' in row[3] and 'Admin' in row[3]:
                driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/section/div[1]/div/div/div[1]/div/div/div/div/div/input").click()
                driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/section/div[1]/div/div/div[2]/div/div/div/div/div/input").click()
            elif 'Admin' in row[3]:
                driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/section/div[1]/div/div/div[1]/div/div/div/div/div/input").click()
            elif 'User' in row[3]:
                driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/section/div[1]/div/div/div[2]/div/div/div/div/div/input").click()
            driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[1]/div/div").click()         
            driver.find_element(By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::span[1]").click()

v2_user()