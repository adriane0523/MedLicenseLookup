
<h1 align="center">Medical License Lookup</h1>

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

Webscraping script that will for a given seach query, iterate through different state endorsed medical licensing websites and parse their medical licences.
It will create a report of all the names found from each website and anaylze if any name is seen commonly in each of the states. Currently the script
scrapes the licenses of the following states: Arizona, Colorado, Wyoming, Alaska and Massachusetts. 

There is an excel sheet where you can input first and last names which the script will go through and create a report for. The final report will be a txt file named
report.txt

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

## :checkered_flag: Starting ##

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
