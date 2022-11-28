import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from interfaces.person import Person

def parseAK(browser,lastNameQuery,firstNameQuery):
    foundSearches = []
    link = 'https://www.commerce.alaska.gov/cbp/main/search/professional'
    browser.get(link)
    time.sleep(3)
    dropdown = browser.find_element(By.XPATH,'//*[@id="ProgramId"]')
    dropdownSelect = Select(dropdown)
    dropdownSelect.select_by_visible_text('Medical')
    name = browser.find_element(By.XPATH, '//*[@id="OwnerEntityName"]')
    submit = browser.find_element(By.XPATH, '//*[@id="search"]')
    fullname = ''
    if (firstNameQuery != ''):
        fullname = firstNameQuery + " " + lastNameQuery
    else:
        fullname = lastNameQuery
    name.send_keys(fullname)
    submit.click()
    time.sleep(2)
    namesTable = browser.find_elements(By.XPATH, '/html/body/div/div[1]/main/article/form/div[2]/table/tbody/tr')
    for i in namesTable:
        tdStuff = i.find_elements(By.XPATH, 'td')
        link = tdStuff[1].find_elements(By.XPATH, 'a')
        profileLink = ''
        for x in link:
            profileLink = x.get_attribute('href')
        foundSearches.append(Person(tdStuff[3].text, 'N/A', 'AK', tdStuff[4].text ,"N/A",link, 'N/A'))
    nextButtonIsThere = browser.find_elements(By.XPATH, '/html/body/div/div[1]/main/article/form/div[2]/div/a[3]')
    if (len(nextButtonIsThere) > 0):
        totalPage = browser.find_element(By.XPATH, '/html/body/div/div[1]/main/article/form/div[2]/div/a[4]')
        total = 0
        if (totalPage.get_attribute('data-pagenum') != None):
            total = int(totalPage.get_attribute('data-pagenum'))
        index = 1
        while(index < total):
            nextButton = browser.find_element(By.XPATH, '/html/body/div/div[1]/main/article/form/div[2]/div/a[3]')
            nextButton.click()
            time.sleep(5)
            namesTable = browser.find_elements(By.XPATH, '/html/body/div/div[1]/main/article/form/div[2]/table/tbody/tr')
            for i in namesTable:
                tdStuff = i.find_elements(By.XPATH, 'td')
                link = tdStuff[1].find_elements(By.XPATH, 'a')
                profileLink = ''
                for x in link:
                    profileLink = x.get_attribute('href')
                foundSearches.append(Person(tdStuff[3].text, 'N/A', 'AK', tdStuff[4].text ,"N/A",link, 'N/A'))
            index += 1
    return foundSearches