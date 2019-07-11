## Working with Python to Access a TeamWork Account
# Intro
The TeamWork API (https://www.teamwork.com) gives uses access to most features of teamwork assuming you have access and an API key.

# teamwork.py
To connect to your TeamWork account you need the subdomain (for me it was imcmanger) and an API key which can be found on the website under your profile. When the class is initialized it will read in account information, a list of people, and a list of projects. This is done by:
```
subdomain = "imcmanager"
api_key = "enter you API-KEY here"
imc = teamwork(subdomain, api_key)
```
This will print out the different `GET` calls that are made to get your account information.
