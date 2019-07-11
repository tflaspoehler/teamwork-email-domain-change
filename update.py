from teamwork import *

# =================================== #
#    read in account information      #
# =================================== #
domain, key = ([line.rstrip() for line in open("./../api_keys.dat", "r").readlines()][0].split())
# =================================== #

# =================================== #
#    read in my teamwork account      #
# =================================== #
team = teamwork(domain, key)
# =================================== #

# =================================== #
#   go   through  every  person  and  #
#   change  their  email  domain  to  #
#   @imcenters.com if it was already  #
#   @americasmart.com                 #
# =================================== #
for person in team.people:
    if ("americasmart" in person["email-address"].split("@")[1].lower()):
        email = person["email-address"].split("@")[0] + "@imcenters.com"
        uid   = person["id"]
        print "-----------------------------------"
        print " ... changing email address for " + person["full-name"] + "(" + uid + ")"
        print " ...                       from " + person["email-address"]
        print " ...                         to " + email
        changes = {"person": {"email-address": email}}
        user = "people/" + uid  + ".json"
        team.put(user, changes)
# =================================== #

