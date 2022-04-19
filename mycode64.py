# 81
# request module for http requests
# http methods
# get>> fetch data from the server
# post>> create the resources
# put>> update the resources
# delete>> delete the resources
# http methods are used in web and api

import requests
# r=requests.get("https://site.financialmodelingprep.com/")
# print(r.text)

# post request which will check some api with passwords and usernames

url="http://www.facebook.com"
data={
    "phone number":9900621605,
    "password":24121999
}
r2=requests.post(url=url,data=data)
print(r2)


