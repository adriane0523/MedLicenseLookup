from interfaces.person import Person
from util import similar, anyalze, createReport, parseExcel
from states.AZ import parseAZ
from states.CO import parseCO
from states.WY import parseWY
from states.AK import parseAK
from states.MA import parseMA
from config import config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#TODO:
#Ask about state pratice place vs state licenses

def startWebparse(lastNames, firstNames, username):
    foundSearches = []
    lastNameArr = lastNames
    firstNameArr = firstNames

    scriptFailed = False

    #-----------------------Start of Script-----------------------
    #call parse excel function
    # parseExcel(firstNameArr,lastNameArr)

    #open chrome driver
    option = webdriver.ChromeOptions()
    option.Proxy = None
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    # option.add_argument("--headless") 
    #option.add_argument("disable-gpu")

    #Creates instance of browser and links to all the websites to parse
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)


    '''
    Below showscases all the webparsing elements of the websites. It will go through each website as if it was a user browsing it.
    Once the website hits a data page it will parse that information and anayalze it for the report
    '''
    try:
        print('STARTING')
        print('This will take a bit...')
        #Iterates through names to get first name and last name
        for nameIndex in range(0,len(lastNameArr)):
            lastNameQuery = lastNameArr[nameIndex]
            firstNameQuery = firstNameArr[nameIndex]
            #Iterates through websites to get individual website link
            for c in config:
                print(c)
                if c['enabled']:
                    if c['state'] == 'AZ':
                        foundSearches += parseAZ(browser,lastNameQuery,firstNameQuery )
                    elif c['state'] == 'CO':
                        foundSearches += parseCO(browser,lastNameQuery,firstNameQuery )
                    elif c['state'] == 'WY':
                        foundSearches += parseWY(browser,lastNameQuery,firstNameQuery )
                    #This website has change URL would need to update
                    # elif c['state'] == 'MA':
                    #     foundSearches += parseMA(browser,lastNameQuery,firstNameQuery )
                    elif c['state'] == 'AK':
                        foundSearches += parseAK(browser,lastNameQuery,firstNameQuery )
                        
    except Exception as e:
        print('Error Has Occured')
        print(e)
        scriptFailed = True
        browser.close()

    #Calls create report function
    createReport(foundSearches, username)

    if (not scriptFailed):
        browser.close()
        print('DONE :)')
        print('Full report written in report.txt')


# if __name__ == "__main__":
#     startWebparse()
