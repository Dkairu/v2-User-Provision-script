# v2-User-Provision-script

This script helps you to add your v2 users to NR from a csv file. It will read a csv file similar to the one attached `users.csv`. 

Please note that using this script to manage your v2 users in New Relic will disable you from managing them in the New Relic UI. 
## How to use:
###### This code uses Python 3.

- Download a chromedriver from  https://chromedriver.chromium.org/downloads and enter the path of the unzipped binary in line 7 `driver = webdriver.Chrome(executable_path=r'/path/to/chromedriver')`

- Update the username and password section. If using Okta or any other MFA interact with the chrome window that pops up, just enter the email address to enter Authenticate details. (Please make sure you add extra time for you to authenticate under line 16 `time.sleep(2)` right now it is set for 2 secs)

- Update this line with your url that takes you to the user mangement UI section `driver.get("<ENTER USER MANAGEMENT URL HERE>")`

- Run the script as `python3 seleniumv2user.py`


P.S Note you might have to update some of the xpaths or element IDs used to reflect your environment. 