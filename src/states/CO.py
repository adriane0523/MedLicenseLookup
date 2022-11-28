import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from interfaces.person import Person

def parseCO(browser,lastNameQuery, firstNameQuery ):
    foundSearches = []
    link = 'https://apps.colorado.gov/dora/licensing/Lookup/LicenseLookup.aspx'
    browser.get(link)
    time.sleep(3)
    dropdown = browser.find_element(By.XPATH,'//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_ctl03_lbMultipleCredentialTypePrefix"]')
    dropdownSelect = Select(dropdown)
    dropdownSelect.select_by_visible_text('Medical')
    lastName = browser.find_element(By.XPATH, '//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_ctl03_tbLastName_Contact"]')
    firstName = browser.find_element(By.XPATH, '//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_ctl03_tbFirstName_Contact"]')
    submit = browser.find_element(By.XPATH, '//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_btnLookup"]')
    lastName.send_keys(lastNameQuery)
    firstName.send_keys(firstNameQuery)
    submit.click()
    time.sleep(2)
    header = browser.find_elements(By.XPATH,'//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_gvSearchResults"]/thead/tr/td/ul/li')
    indexes = []
    for i in header:
        indexes.append(i.text)
    index = 0
    for i in indexes:    
        if (index > 0):
            path = '//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_gvSearchResults"]/thead/tr[1]/td/ul/li[' + i + ']/a'
            browser.find_element(By.XPATH, path).click()
            time.sleep(1)
        namesTable = browser.find_elements(By.XPATH,'//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_gvSearchResults"]/tbody/tr')
        for i in namesTable:
            columns = i.find_elements(By.TAG_NAME, 'td')
            foundSearches.append(Person(columns[1].text, 'N/A', columns[6].text.strip(), columns[3].text, columns[2].text, link, 'N/A'))
        index += 1

    if (len(indexes) == 0 ):
        namesTable = browser.find_elements(By.XPATH,'//*[@id="ctl00_MainContentPlaceHolder_ucLicenseLookup_gvSearchResults"]/tbody/tr')
        for i in namesTable:
            columns = i.find_elements(By.TAG_NAME, 'td')
            state = 'CO'
            if (columns[6].text.strip() == ''):
                state = columns[6].text.strip()
            foundSearches.append(Person(columns[1].text, 'N/A', state , columns[3].text, columns[2].text, link, 'N/A'))
    return foundSearches