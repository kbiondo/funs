import email
from numpy import append
from pyparsing import restOfLine
import requests
import json
print('hello world')
people = []
peoples = {}
m = []
with open("people.txt") as people_list:
    people.append(people_list.readlines())
    print(people_list.read())
print(people)
urls = []
links = {}
emails = {}
bemsIDs = {}
n = []
team = {}
templist = {}
for i in people:
    for z in i:
        l = z[:-1]
        p = l.replace(" ","%20")
        n.append(l)
        m.append(p)
for k in range(len(n)):
    if k < 10:
        api_url = "https://insite.web.boeing.com/culture/service/boeingUserWebServiceJSON/name?query=" + str(m[k])    
        print(api_url)
        urls.append(api_url)        
        response = requests.get(api_url)
        keys_list = response.json()
        with open("response.txt","w") as f:
            print(json.dumps(keys_list),file=f)
        with open("response.txt") as f:
            bemsid = json.load(f)
            resultholder = bemsid["resultholder"]
            totalResults = resultholder["totalResults"]

            #lastName = resultholder[profiles[profileholder[user["lastName"]]]]
            lastName = user["lastName"]
            #bemsId = resultholder[profiles[profileholder[user["bemsId"]]]]
            bemsId = user["bemsId"]
            if totalResults != 1:
                profiles = resultholder["profiles"]
                profileholder = profiles["profileholder"]
                zero = profileholder["0"]
                user = zero["user"]
                lastName = user["lastName"]
                bemsId = user["bemsId"]
#        elif totalResults == "1":
            else:
                profiles = resultholder["profiles"]
                profileholder = profiles["profileholder"]
                #user = profileholder["user"]
                lastName = user["lastName"]
                bemsId = user["bemsId"]
                emailaddress = user["emailAddress"]
                insite = "https://insite.web.boeing.com/culture/displayBluesInfo.do?bemsid="+str(bemsId)
                team.update({str(n[k]): {"bemsID" : str(bemsId), "email": str(emailaddress), "insite-profile": str(insite)}})
                team.update({str(n[k]): {"bemsID" : str(bemsId), "email": str(emailaddress), "insite-profile": str(insite)}})
                templist.update({str(n[k]): {"bemsid" : str(bemsId), "email":str(emailaddress), "insite":str(insite), "jsonapi":str(api_url) }})
                links.update({str(n[k]): str(api_url)})
                emails.update({str(n[k]): str(emailaddress)})
                bemsIDs.update({str(n[k]): str(bemsId)})
    #            peoples.update(str(n[k]): templist)

        with open("bems.txt","a") as f:
            print(bemsId,file=f)
        with open("bemsIDs.txt","a") as f:
            print(bemsId,file=f)
        with open("n.txt","a") as f:
            print(n,file=f)
        with open("urls.txt","a") as f:
            print(urls,file=f)
        with open("links.txt","a") as f:
            print(links,file=f)
        with open("templist.txt","a") as f:
            print(templist,file=f)
        with open("team.txt","a") as f:
            print(team,file=f)
    


