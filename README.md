
<h1 align="center">Medical License Lookup API</h1>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  MedLookupAPI 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#api-endpoints">API Endpoints</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##
The purpose of this API is to identify doctors who have multiple licenses in different states. Legally they are only allowed one in one state. Having multiple could be a sign of malpractice since they could of "moved" to a different state after getting their licenses originally revoked and not filling the removal of their licensing.

This is a Web-scraping script that will for a given search query, iterate through different state endorsed medical licensing websites and parse their medical licenses.

It will create a report of all the names found from each website and anaylze if any name is seen commonly in each of the states. Currently the script
scrapes the licenses of the following states: Arizona, Colorado, Wyoming, Alaska and Massachusetts (deprecated for now). 

An API with JWT Authentication is wrapped around this webscraping algo and will create a background task (thread) to run the web scraping. 

Matching algothrim when anaylzing similar names among each states database is a <a href="https://epydoc.sourceforge.net/stdlib/difflib.SequenceMatcher-class.html#:~:text=SequenceMatcher%20is%20a%20flexible%20class,name%20%22gestalt%20pattern%20matching%22.">Sequence Matcher</a>

## API Endpoints ##
POST <endpoint>/parse - Starts web scraping algo <br>
Needs x-access-token Header<br>
Body:
{
	"name": string,
	"email": string,
	"username": string,
	"password": string
}

GET <endpoint>/get_all_users - send back list of users <br>
Needs x-access-token Header<br>
	
POST <endpoint>/login <br>
Body:
{
	"username": string,
	"password": string
}

POST <endpoint>/signup <br>
Body:
{
	"name": string,
	"email": string,
	"username": string,
	"password": string
}

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [JWT](https://pyjwt.readthedocs.io/en/stable/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

## :checkered_flag: Starting ##

1. Add names to excel sheet
2. Run python main.py
3. View report.txt

```bash
# Clone this project
$ git clone git@github.com:adriane0523/MedLicenseLookup.git

# Access
$ cd medlookupapi

# Install dependencies and start the virtual env
$ python -m venv venv

#For Mac
$ source venv/bin/actvate
#For PC
$ venv/Scripts/activate

$ pip install -r requirements.txt

# Add first names and last names to the excel sheet
# Run the script
$ python main.py

```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/adriane0523" target="_blank">Adriane Inocencio</a>

&#xa0;

<a href="#top">Back to top</a>
