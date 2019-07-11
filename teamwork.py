import json
import urllib2, base64


# =================================== #
#      TeamWork class that loads      #
#   your teamwork instance and sends  #
#  put / get calls through the TW API #
# =================================== #
class teamwork:
    def __init__(self, company, key):
        print "==================================="
        print "loading company " + company
        print
        self.company = company
        self.key = key
        self.account  = self.get("account.json")["account"]
        self.people = []

        i = 1
        while 1:
            people = self.get("people.json?page={0}".format(i))["people"]
            if (len(people) > 0):
                self.people += people
                i += 1
            else:
                break

        self.projects = self.get("projects.json")["projects"]
        
        print "    there are {0} people in this group".format(len(self.people))
        print "==================================="
        print

    # ----------------------- #
    #  generic  GET  request  #
    #  converts  json string  #
    #  to  python dictionary  #
    # ----------------------- #
    def get(self, action):
        print "-----------------------------------"
        print "sending GET request"
        print "    https://{0}.teamwork.com/{1}".format(self.company, action)
        request = urllib2.Request("https://{0}.teamwork.com/{1}".format(self.company, action))
        request.add_header("Authorization", "BASIC " + base64.b64encode(self.key + ":xxx"))
        response = urllib2.urlopen(request)
        print "-----------------------------------"
        print
        read = response.read()
        return json.loads(read)
    # ----------------------- #

    # ----------------------- #
    #  generic POST request   #
    # ----------------------- #
    def post(self, action, data):
        print "-----------------------------------"
        print "sending POST request"
        print "    https://{0}.teamwork.com/{1}".format(self.company, action)
        request = urllib2.Request("https://{0}.teamwork.com/{1}".format(self.company, action), data=json.dumps(data))
        request.add_header("Authorization", "BASIC " +  base64.b64encode(self.key + ":xxx"))
        request.add_header("Content-Type", "application/json")
        request.get_method = lambda: "POST"

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        response = opener.open(request)
        print "-----------------------------------"
        print
        return json.loads(response.read())
    # ----------------------- #


    # ----------------------- #
    #  generic  PUT  request  #
    # ----------------------- #
    def put(self, action, data):
        print "-----------------------------------"
        print "sending PUT request"
        print "    https://{0}.teamwork.com/{1}".format(self.company, action)
        request = urllib2.Request("https://{0}.teamwork.com/{1}".format(self.company, action), data=json.dumps(data))
        request.add_header("Authorization", "BASIC " +  base64.b64encode(self.key + ":xxx"))
        request.add_header("Content-Type", "application/json")
        request.get_method = lambda: "PUT"
        response = urllib2.urlopen(request)
        print "-----------------------------------"
        print
        return json.loads(response.read())
    # ----------------------- #
# =================================== #
