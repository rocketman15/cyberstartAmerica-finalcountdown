###################################################
#code by rocketman 15. last change made on 12/8/22#
###################################################
#origional project can be found at https://github.com/rocketman15/cyberstartAmerica-finalcountdown 
import requests
import webbrowser
#Retrieve text information from endpoints
e1 = requests.get("https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
e2 = requests.get("https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
e3 = requests.get("https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
e4 = requests.get("https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
e5 = requests.get("https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
#combine information into the required secret key
secretKey = (e1.text + e2.text + e3.text + e4.text + e5.text)
print(secretKey)
#print the link to access the flag
finalLink = ("https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string="+secretKey)
print(finalLink)
