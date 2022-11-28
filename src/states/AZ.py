import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from interfaces.person import Person

def parseAZ(browser,lastNameQuery, firstNameQuery ):
    foundSearches = []
    link =  "https://azbomprod.azmd.gov/glsuiteweb/clients/azbom/public/webverificationsearch.aspx"
    browser.get(link)
    time.sleep(3)
    lastName = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txtLastName"]')
    firstName = browser.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txtFirstName"]')
    submit = browser.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnName"]')
    lastName.send_keys(lastNameQuery)
    firstName.send_keys(firstNameQuery)
    submit.click()
    time.sleep(2)
    namesTable = browser.find_elements(By.XPATH,'//*[@id="ContentPlaceHolder1_dtgList"]/tbody/tr/td')
    index = 0
    name = ''
    link = ''
    count = 0
    for row in namesTable:
        if (index > 1):
            if (count == 3):
                speciality = name.split('Specialty')
                firstname = speciality[0].strip()
                specialityname = 'N/A'
                if (len(speciality) > 1):
                    specialityname = speciality[1].strip()
                foundSearches.append(Person(firstname , link, 'AZ', 'N/A', '',link, specialityname ))
                name = ''
                link = ''
                count = 0
            if (row.text != 'Show Profile'):
                name = row.text
            else:
                link = row.find_element(By.TAG_NAME, 'a')
                link = link.get_attribute('href')
            count += 1
        index += 1
    if (len(namesTable) > 0):
        speciality = name.split('Specialty')
        foundSearches.append(Person(speciality[0].strip(), link, 'AZ', 'N/A', '', link,speciality[1].strip() ))
    return foundSearches