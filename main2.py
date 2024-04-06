# This is a sample Python script.
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import argparse

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


# course id's "
calculation = "131113"
opertionSystem_class = "131116"
opertionSystem_LAB = "131116"
DB = "131112"
practicalTools = "131150"
AWS = "150060"

devOps = "142216"
compattionCoding = "142202"


complexity = "131111"
valusCreation = "142209"
dataSecurity = "141120"
computerNetwork = "141418"
sysAnalysis = "141161"


# backups
kubernetes = "150066"
CSharp = "142169"
hacking_tech = "142223"
defenceFromAttacks = "142214"
computerVision = "142205"
memshakim = "141182"
NLP = "145005"

courseList = [devOps, defenceFromAttacks]

# what was before :
# courseList = [AWS, devOps, valusCreation, dataSecurity, calculation, opertionSystem_class, DB, compattionCoding, computerNetwork, sysAnalysis, kubernetes, CSharp, hacking_tech, complexity, defenceFromAttacks, practicalTools]

size_of_courseList = len(courseList)


FAST_REGISTER = True


def telegram_bot_sendtext(bot_message):
    bot_token = '**************************'
    bot_chatID = '**************************'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    res = requests.get(send_text)

    return res.json()


print("🦸 Starting Auto registration 🦸")

# Send a GET request to the URL
url = "https://mtamn.mta.ac.il/yedion/fireflyweb.aspx"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    # soup = BeautifulSoup(response.content, "html.parser")

    # Find and extract the desired data from the HTML structure

    # result = requests.get("http://www.example.com")
    # print(result.text)

    while True:

        for m in range(0, 35):

            # chromedriver = "chromedriver.exe"
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_extension('/home/eden/.config/google-chrome/Default/Extensions/klehggjefofgiajjfpoebdidnpjmljhb/1.6.0_0/')
            # driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)

            """
            # this is to duplicate tab
            action_chains = ActionChains(driver)
            action_chains.key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys('d').perform()
            action_chains.key_up(Keys.ALT).key_up(Keys.SHIFT).perform()
            """

            driver = webdriver.Chrome()
            driver.get(url)
            driver.implicitly_wait(0.5)

            # Find the username and password input fields
            username_field = driver.find_element(By.ID, "Ecom_User_ID")
            driver.implicitly_wait(0.5)
            password_field = driver.find_element(By.ID, "Ecom_Password")

            # Input your credentials
            username = "edenbr"
            password = "Qazwsx2131!"
            username_field.send_keys(username)
            password_field.send_keys(password)
            time.sleep(0.5)

            # Click the login button
            login_button = driver.find_element(By.ID, "loginButton")
            login_button.click()

            # Wait for the page to load
            time.sleep(2)

            i = 0

            # Open tabs
            for i in range(1, size_of_courseList):
                # Open a new tab
                driver.execute_script("window.open('');")
                # Switch to the new tab
                driver.switch_to.window(driver.window_handles[i])
                # Navigate to new URL in new tab
                driver.get(url)
                # Wait for the page to load
                time.sleep(0.2)
                # refresh the page
                driver.refresh()

            i = 0

            if FAST_REGISTER:
                print("Fast Register is On")
            else:
                print("Fast Register is Off")

            # if you want to debug - uncomment this line
            x = input("Press any key to continue ")
            start_time = time.time()

            while True:
            # Enter to "רישום לקורסים"
                try:
                    for i in range(0, size_of_courseList):
                        # Switch to the new tab - the i's tab
                        driver.switch_to.window(driver.window_handles[i])
                        # refresh the page
                        driver.refresh()
                        time.sleep(0.3)

                        # Go to the dsired page with xPath = //*[@id="#kt_header_menu"]/div/div[1]/a - this is click on "רישום לקורסים"
                        driver.find_element(By.XPATH, '//*[@id="#kt_header_menu"]/div/div[1]/a').click()
                        time.sleep(0.3)

                        # click on "רישום לקורסים "
                        # xPath = //*[@id="#kt_header_menu"]/div/div[1]/div/div[1]/a/span
                        driver.find_element(By.XPATH, '//*[@id="#kt_header_menu"]/div/div[1]/div/div[1]/a/span').click()
                        time.sleep(0.3)

                        # Go to xPath = //*[@id="SubjectCode"] and fill the course id
                        # xPath = //*[@id="SubjectCode"]
                        # driver.find_element(By.XPATH, '//*[@id="SubjectCode"]').send_keys()


                        # Go to xPath = //*[@id="SubjectCode"] and fill the course id
                        # xPath = //*[@id="SubjectCode"]
                        driver.find_element(By.XPATH, '//*[@id="SubjectCode"]').send_keys(courseList[i])
                        time.sleep(0.3)

                        # Go to xPath = //*[@id="searchButton"] and clock on "חפש לפי קורס"
                        # xPath = //*[@id="searchButton"]
                        driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
                        time.sleep(0.3)



                        # staring registration
                        start_reg_time = time.time()
                        if i == 0:
                            print("Registration starts after: " + str(start_reg_time - start_time) + " seconds")

                        if courseList[i] == calculation:
                            # now only for calculation
                            # switch to tab 0
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details3"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details2"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.5)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG3"] and click on it
                                    # xPath = //*[@id="REG3"]
                                    driver.find_element(By.XPATH, '//*[@id="REG3"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()
                            else:
                                # Go to xPath = //*[@id="Details3"] and click on it
                                # xPath = //*[@id="Details3"]
                                driver.find_element(By.XPATH, '//*[@id="Details3"]').click()
                                time.sleep(0.3)



                        elif courseList[i] == opertionSystem_class:
                            # now only for opertionSystem_class
                            # switch to tab 1
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details3"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details2"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG3"] and click on it
                                    # xPath = //*[@id="REG3"]
                                    driver.find_element(By.XPATH, '//*[@id="REG3"]').click()
                                    time.sleep(0.3)

                                    # register to the workshop
                                    scroll_element = driver.find_element(By.XPATH, '//*[@id="Details1"]')
                                    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                                    time.sleep(0.1)

                                    # xPath = //*[@id="REG2"]
                                    driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                    time.sleep(0.3)

                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details3"] and click on it
                                # xPath = //*[@id="Details3"]
                                driver.find_element(By.XPATH, '//*[@id="Details3"]').click()
                                time.sleep(0.3)



                        elif courseList[i] == DB:
                            # now only for DB_class
                            # switch to tab 2
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details3"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details2"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG3"] and click on it
                                    # xPath = //*[@id="REG3"]
                                    driver.find_element(By.XPATH, '//*[@id="REG3"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details3"] and click on it
                                # xPath = //*[@id="Details3"]
                                driver.find_element(By.XPATH, '//*[@id="Details3"]').click()
                                time.sleep(0.3)




                        elif courseList[i] == AWS:
                            # now only for AWS workshop
                            # switch to tab 3
                            driver.switch_to.window(driver.window_handles[i])

                            # # Scroll down to xPath = //*[@id="Details3"]
                            # scroll_element = driver.find_element(By.XPATH, '//*[@id="Details3"]')
                            # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]').click()
                                time.sleep(0.3)




                        elif courseList[i] == compattionCoding:
                            # now only for compattionCoding
                            # switch to tab 4
                            driver.switch_to.window(driver.window_handles[i])

                            # # Scroll down to xPath = //*[@id="Details3"]
                            # scroll_element = driver.find_element(By.XPATH, '//*[@id="Details3"]')
                            # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]').click()
                                time.sleep(0.3)




                        elif courseList[i] == opertionSystem_LAB:
                            # now only for opertionSystem_LAB
                            # switch to tab 5
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details10"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details9"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG3"] and click on it
                                    # xPath = //*[@id="REG3"]
                                    driver.find_element(By.XPATH, '//*[@id="REG10"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details3"] and click on it
                                # xPath = //*[@id="Details3"]
                                driver.find_element(By.XPATH, '//*[@id="Details10"]').click()
                                time.sleep(0.3)


                        elif courseList[i] == devOps:
                            # now only for DevOps
                            # switch to tab 6
                            driver.switch_to.window(driver.window_handles[i])

                            # # Scroll down to xPath = //*[@id="Details3"]
                            # scroll_element = driver.find_element(By.XPATH, '//*[@id="Details3"]')
                            # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]').click()
                                time.sleep(0.3)





                        elif courseList[i] == complexity:
                            # now only for Complexity
                            # switch to tab 7
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details4"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details2"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG4"] and click on it
                                    # xPath = //*[@id="REG4"]
                                    driver.find_element(By.XPATH, '//*[@id="REG3"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details4"] and click on it
                                # xPath = //*[@id="Details4"]
                                driver.find_element(By.XPATH, '//*[@id="Details3"]').click()
                                time.sleep(0.3)



                        elif courseList[i] == valusCreation:
                            # now only for ValueCreation
                            # switch to tab 8
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details4"]
                            # scroll_element = driver.find_element(By.XPATH, '//*[@id="Details3"]')
                            # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    try:
                                        # Go to xPath = //*[@id="REG1"] and click on it
                                        # xPath = //*[@id="REG1"]
                                        driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                        time.sleep(0.3)
                                        print("Successfully registered to " + courseList[i] + " second option!" + " after: " + str(time.time() - start_time) + " seconds")

                                    except:
                                        print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details2"]').click()
                                time.sleep(0.3)



                        elif courseList[i] == dataSecurity:
                            # now only for DataSceuirty
                            # switch to tab 9
                            driver.switch_to.window(driver.window_handles[i])

                            # # Scroll down to xPath = //*[@id="Details3"]
                            # scroll_element = driver.find_element(By.XPATH, '//*[@id="Details3"]')
                            # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]').click()
                                time.sleep(0.3)



                        elif courseList[i] == computerNetwork:
                            # now only for computerNetwork
                            # switch to tab 10
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details3"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details2"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG3"] and click on it
                                    # xPath = //*[@id="REG3"]
                                    driver.find_element(By.XPATH, '//*[@id="REG3"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:

                                    try:
                                        # Go to xPath = //*[@id="REG3"] and click on it
                                        # xPath = //*[@id="REG3"]
                                        driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                        time.sleep(0.3)
                                        print("Successfully registered to " + courseList[i] + " second time!" + " after: " + str( time.time() - start_time) + " seconds")
                                    except:

                                        print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details3"] and click on it
                                # xPath = //*[@id="Details3"]
                                driver.find_element(By.XPATH, '//*[@id="Details3"]').click()
                                time.sleep(0.3)


                        elif courseList[i] == kubernetes:
                            # now only for kubernetes
                            # switch to tab 11
                            driver.switch_to.window(driver.window_handles[i])

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]')
                                time.sleep(0.3)



                        elif courseList[i] == CSharp:
                            # now only for CSharp
                            # switch to tab 12
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details2"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details1"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG2"] and click on it
                                    # xPath = //*[@id="REG2"]
                                    driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:
                                    try:
                                        # Go to xPath = //*[@id="REG2"] and click on it
                                        # xPath = //*[@id="REG2"]
                                        driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                        time.sleep(0.3)
                                        print("Successfully registered to " + courseList[i] + " second time!" + " after: " + str(time.time() - start_time) + " seconds")
                                    except:
                                        print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details2"] and click on it
                                # xPath = //*[@id="Details2"]
                                driver.find_element(By.XPATH, '//*[@id="Details2"]')
                                time.sleep(0.3)



                        elif courseList[i] == hacking_tech:

                            driver.switch_to.window(driver.window_handles[i])

                            # # Scroll down to xPath = //*[@id="Details3"]
                            # scroll_element = driver.find_element(By.XPATH, '//*[@id="Details3"]')
                            # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:

                                    try:
                                        # Go to xPath = //*[@id="REG1"] and click on it
                                        # xPath = //*[@id="REG1"]
                                        driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                        time.sleep(0.3)
                                        print("Successfully registered to " + courseList[i] + " second option!" + " after: " + str(time.time() - start_time) + " seconds")
                                        telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                    except:
                                        print("The course " + courseList[i] + " is full")
                                        driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details2"]').click()
                                time.sleep(0.3)



                        elif courseList[i] == sysAnalysis:
                            # now only for CSharp
                            # switch to tab 12
                            driver.switch_to.window(driver.window_handles[i])

                            # Scroll down to xPath = //*[@id="Details2"]
                            scroll_element = driver.find_element(By.XPATH, '//*[@id="Details1"]')
                            driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
                            time.sleep(0.1)

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG2"] and click on it
                                    # xPath = //*[@id="REG2"]
                                    driver.find_element(By.XPATH, '//*[@id="REG2"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details2"] and click on it
                                # xPath = //*[@id="Details2"]
                                driver.find_element(By.XPATH, '//*[@id="Details2"]')
                                time.sleep(0.3)




                        elif courseList[i] == practicalTools:
                            # now only for practicalTools
                            driver.switch_to.window(driver.window_handles[i])

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                except:
                                    print("The course " + courseList[i] + " is full")

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]')
                                time.sleep(0.3)



                        elif courseList[i] == defenceFromAttacks:
                            # now only for practicalTools
                            driver.switch_to.window(driver.window_handles[i])

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]')
                                time.sleep(0.3)


                        elif courseList[i] == computerVision:
                            # now only for practicalTools
                            driver.switch_to.window(driver.window_handles[i])

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    # telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]')
                                time.sleep(0.3)



                        elif courseList[i] == memshakim:
                            # now only for practicalTools
                            driver.switch_to.window(driver.window_handles[i])

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")
                                    telegram_bot_sendtext("Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]')
                                time.sleep(0.3)

                        elif courseList[i] == NLP:
                            # now only for practicalTools
                            driver.switch_to.window(driver.window_handles[i])

                            if FAST_REGISTER:
                                try:
                                    # Go to xPath = //*[@id="REG1"] and click on it
                                    # xPath = //*[@id="REG1"]
                                    driver.find_element(By.XPATH, '//*[@id="REG1"]').click()
                                    time.sleep(0.3)
                                    print("Successfully registered to " + courseList[i] + " !" + " after: " + str(
                                        time.time() - start_time) + " seconds")
                                    # telegram_bot_sendtext( "Successfully registered to " + courseList[i] + " !" + " after: " + str(time.time() - start_time) + " seconds")

                                except:
                                    print("The course " + courseList[i] + " is full")
                                    driver.refresh()

                            else:
                                # Go to xPath = //*[@id="Details1"] and click on it
                                # xPath = //*[@id="Details1"]
                                driver.find_element(By.XPATH, '//*[@id="Details1"]')
                            time.sleep(0.3)





                    print("Total time: " + str(time.time() - start_time) + " seconds")

                    time.sleep(25)

                except:
                    print("Error in the main loop. Time " + str(time.time() - start_time))
                    time.sleep(1)
                    break

            i = 0


            i = 0

            if not FAST_REGISTER:

                # This is the actual click to register to the course
                for i in range(0, size_of_courseList):
                    # Switch to the new tab - the i's tab
                    driver.switch_to.window(driver.window_handles[i])

                    # Go to xPath = //*[@id="kt_content"]/div/div[2]/div/div/div/form/table[2]/tbody/tr[3]/td/a and click on it
                    # xPath = //*[@id="Details3"]
                    driver.find_element(By.XPATH, '//*[@id="kt_content"]/div/div[2]/div/div/div/form/table[2]/tbody/tr[3]/td/a').click()

                    print("Successfully registered to " + courseList[i] + " !")




            end_time = time.time()

            print("Total time: " + str(end_time - start_time) + " seconds")
            telegram_bot_sendtext("something went wrong. Total time: " + str(end_time - start_time) + " seconds, " + str(m))
            time.sleep(2)
            webdriver.Chrome.quit(driver)



        # if happend more than 35 times, that means we need to wait 30 min.
        telegram_bot_sendtext("Waiting 30 min")
        time.sleep(2100)



