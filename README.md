# Overview
This repository is a playground for building a "grocery decider" application, which will generate a handful of recipes for the week and list out all the ingredients required for them. Such applications certainly already exist, but I wanted to try my hand at it for funsies.

# Structure
## Database
Relational H2 database to hold recipe and ingredient data (Not yet implemented). Might use Hibernate/JPA for this, because it's fun.
## Scraper
Python BeautifulSoup scraper for reading HelloFresh recipes into a digestible data format.
## "Business" Logic
This will be Java in Spring - various endpoints for retrieving ingredient data with optional parameters, e.g. if you already have some ground beef in the freezer.
## UI
Angular Material will allow me to slap together a UI that looks alright with barely any CSS, and I'll go from there.

# Open Questions
How will I gather the list of recipes that I want? Perhaps by using my HelloFresh account and retrieving a list of recipes I ordered in the past? But I wouldn't want to strictly limit this app to only recipes I've made before. Perhaps there is some "see all recipes" page on HelloFresh's website that I could scrape and then go from there. Worst case, I can input a repository of recipe links by hand.

