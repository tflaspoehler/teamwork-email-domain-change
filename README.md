# Working with Python to Access a TeamWork Account
## intro
The [TeamWork API](https://developer.teamwork.com/projects/introduction) ([https://www.teamwork.com](https://www.teamwork.com)) gives users access to most features of teamwork assuming you have access and an API key.

## teamwork.py
To connect to your TeamWork account using attached `teamwork.py` class you need the subdomain (for me it was "imcmanger") and an API key which can be found on the website under your profile. When the class is initialized it will read in account information, a list of people, and a list of projects. This is done by:
```
from teamwork import *

subdomain = "imcmanager"
api_key = "enter you API-KEY here"
team = teamwork(subdomain, api_key)
```
This will print out the different `GET` calls that are made to get your account information. Now we can loop through our users and print out information with something like ...
```
for person in team.people:
    print "{0} ({1})".format(person["full-name"], person["email-address"])
```
From here, you have all of the functionality in TeamWork at your fingertips assuming you can follow their API documentation and properly format your PUTs. To create a new user you would do something along these lines (add as much information as you would like):
```
user = {"person": {"first-name": "Timothy",
                   "last-name":  "Flaspoehler",
                   "email-address": "tflaspoehler@gmail.com",}}
team.post("people.json", user)
```
With a similar approach, it is easy to edit an existing user but you have to send the post request with the user ID.
```
uid = 335457
user = "people/{0}.json".format(uid)
changes = {"person": {"first-name": "Tim"}}
team.put(user, changes)
```
This should be the same with adding and editing projects, tasks, etc.

