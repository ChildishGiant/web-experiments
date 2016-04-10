import os.path
from urllib.parse import quote
from urllib import request
import json

if os.path.isfile("apikey.txt"):
    pass
else:
    with open("apikey.txt") as f:
        f.write(input("Please enter your google API Key. If you don't have one"\
    " visit https://console.developers.google.com/apis/api/geocoding_backend/"))
        f.close()

with open("apikey.txt") as f:
    key = f.read()
    f.close()


address = input("Address to search from: ")
ur = quote("https://maps.googleapis.com/maps/api/geocode/json?address="+address, safe = "&/:?=")
k = request.urlopen(ur).read().decode()
j = json.loads(k)
try:
    lat = j["results"][0]["geometry"]["location"]["lat"]
    lng = j["results"][0]["geometry"]["location"]["lng"]
    print("Searching for cases from",j["results"][0]["formatted_address"])
    year = input("What year?:")
    month = input("What month?:")

    nur = quote("https://data.police.uk/api/crimes-street/all-crime?lat="+str(lat)+"&lng="+str(lng)+"&date="+year+"-"+month, safe = "&/:?=")
    nk = request.urlopen(nur).read().decode()

except IndexError or TypeError:
    print("I can't find that place.")



nj = json.loads(nk)
if nj == []:
    print("No cases were found in the given month.")
caseCounter = 0
categoryCounter = []
for i in nj:
    caseCounter += 1
    print("Case ID:",i["persistent_id"])
    print("Month:",i["month"])
    print("Category:",i["category"])
    categoryCounter.append(i["category"])
    print("Street:",i["location"]["street"]["name"])
    try:
        print("Outcome:",i["outcome_status"]["category"])
    except TypeError:
        print("Outcome: N/A")
    print("-~==~-")
print("Summary:")

printedCategories = []
for category in categoryCounter:
    m = "Counts of {0}: {1}".format(category,categoryCounter.count(category))
    if m not in printedCategories:
        print(m)
    printedCategories.append(m)

print("Number of cases in {0} on {1}-{2}: {3}".format(j["results"][0]["formatted_address"],month,year,caseCounter))
