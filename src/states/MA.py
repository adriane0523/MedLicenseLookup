import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from interfaces.person import Person

def parseMA(browser, lastNameQuery, firstNameQuery):
    foundSearches = []
    link = 'http://profiles.ehs.state.ma.us/ProfilesV3'
    browser.get(link)
    time.sleep(3)
    lastNameKey = browser.find_element(By.XPATH,'//*[@id="LastName"]')
    firstNameKey = browser.find_element(By.XPATH,'//*[@id="FirstName"]')
    submit = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/form/div[4]/div/div[1]/input')
    lastNameKey.send_keys(lastNameQuery)
    firstNameKey.send_keys(firstNameQuery)
    submit.click()
    time.sleep(1)
    try:
        fifty = browser.find_element(By.XPATH, '/html/body/div[3]/form/div[2]/div/div[1]/div[2]/div/button[3]')
        fifty.click()
        time.sleep(0.2)
    except:
        pass
    findTdTable = browser.find_elements(By.XPATH,'/html/body/div[3]/form/div[2]/div/div[2]/table/tbody')
    if (len(findTdTable) > 0):
        tdTable = browser.find_element(By.XPATH,'/html/body/div[3]/form/div[2]/div/div[2]/table/tbody')
        namesTable = tdTable.find_elements(By.CLASS_NAME,'tabular')
        for i in namesTable:
            columns = i.find_elements(By.XPATH, 'td')
            link = i.find_elements(By.XPATH, 'td/a')
            profileLink = 'N/A'
            lastName =''
            for x in link:
                profileLink = x.get_attribute('href')
                lastName = x.text
            firstName1 = ''
            try:
                ipath = columns[1].find_element(By.XPATH, 'i')
                firstName = ipath.text
            except:
                firstName = columns[1].text
            state = 'MA'
            if (columns[6].text.strip() == ''):
                state = columns[6].text.strip()
            foundSearches.append(Person(firstName + " " + lastName , profileLink,state, columns[4].text, "N/A",link, columns[3].text))

    try:
        nextButton = browser.find_element(By.XPATH, '/html/body/div[3]/form/div[2]/div/div[1]/div[3]/div/button[6]')
        while(True):
            nextButton.click()
            time.sleep(1)
            tdTable = browser.find_element(By.XPATH,'/html/body/div[3]/form/div[2]/div/div[2]/table/tbody')
            namesTable = tdTable.find_elements(By.CLASS_NAME,'tabular')
            for i in namesTable:
                columns = i.find_elements(By.XPATH, 'td')
                link = i.find_elements(By.XPATH, 'td/a')
                profileLink = 'N/A'
                lastName =''
                for x in link:
                    profileLink = x.get_attribute('href')
                    lastName = x.text
                firstName = ''
                try:
                    ipath = columns[1].find_element(By.XPATH, 'i')
                    firstName = ipath.text
                except:
                    firstName = columns[1].text
                state = 'MA'
                if (columns[6].text.strip() == ''):
                    state = columns[6].text.strip()
                foundSearches.append(Person(firstName + " " + lastName , profileLink, state , columns[4].text, "N/A",link, columns[3].text))
            nextButton = browser.find_element(By.XPATH, '/html/body/div[3]/form/div[2]/div/div[1]/div[3]/div/button[6]')
    except:
        pass
    return foundSearches
