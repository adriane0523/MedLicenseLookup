import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from interfaces.person import Person
from config import states

def parseWY(browser, lastNameQuery, firstNameQuery):
    foundSearches = []
    link = 'https://wybomprod.glsuite.us/GLSuiteWeb/Clients/WYBOM/Public/LicenseeSearch.aspx?SearchType=Physician'
    browser.get(link)
    time.sleep(3)
    lastNameKey = browser.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtLastName"]')
    firstNameKey = browser.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_txtFirstName"]')
    submit = browser.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnSubmit"]')
    lastNameKey.send_keys(lastNameQuery)
    firstNameKey.send_keys(firstNameQuery)
    submit.click()
    time.sleep(1)

    tdTable = browser.find_elements(By.XPATH,'//*[@id="ContentPlaceHolder1_dtgResults"]/tbody/tr')
    index = 0
    for i in tdTable:
        if (index > 0):
            tdStuff = i.find_elements(By.XPATH, 'td')
            name = tdStuff[0].text.replace(', MD', '')
            stateIndex = 0
            flag = True
            state = 'WY'
            while (stateIndex < len(states)-1 and flag):
                if states[stateIndex] in tdStuff[1].text:
                    flag = False
                    state = states[stateIndex]
                stateIndex += 1
            status = 'N/A'
            if 'Emeritus' in tdStuff[6].text:
                status = 'Emeritus'
            elif 'Expired' in tdStuff[6].text:
                status = 'Expired'
            elif 'Active' in tdStuff[6].text:
                status = 'Active'
            foundSearches.append(Person(name, 'N/A', state, status,"N/A", link, tdStuff[8].text))
            pass
        index += 1
    return foundSearches