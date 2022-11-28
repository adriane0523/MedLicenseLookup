
<h1 align="center">Medical License Lookup API (w/ JWT AUTH)</h1>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  MedLookupAPI 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##
The purpose of this API is to identify doctors who have mutiple licenses in different states. Legally they are only allowed one in one state. Having mutiple could be a sign of malpratice since they could of "moved" to a different state after getting their licenses oringally revoked and not filling the removal of their licensing.


This is a Webscraping script that will for a given seach query, iterate through different state endorsed medical licensing websites and parse their medical licences.

It will create a report of all the names found from each website and anaylze if any name is seen commonly in each of the states. Currently the script
scrapes the licenses of the following states: Arizona, Colorado, Wyoming, Alaska and Massachusetts (deprecated for now). 

An API with JWT Authentication is wrapped around this webscraping algo and will create a background task (thread) to run the web scraping. 

API Endpoints: <br><br>
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
