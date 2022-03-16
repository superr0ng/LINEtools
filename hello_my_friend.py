import html5lib
import requests
import random
from bs4 import BeautifulSoup

#add your tokens in this list
#if you have more than one token, put them all in the list seperated by a comma(,)
myToken = ["replace_this_with_your_own_token"]
def lineNotify(token=myToken[0], msg='親愛的朋友，祝福你有美好的一天。', picURI=''):
    url = "https://notify-api.line.me/api/notify"
    headers = {
                "Authorization": "Bearer " + token,
                #"Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    if picURI:
        files = {'imageFile': open(picURI, 'rb')}
        r = requests.post(url, headers=headers, params=payload, files=files)
    else:
        r = requests.post(url, headers = headers, params = payload)
    return r.status_code

tgurl = 'https://chunting.me/elder-photos-good-morning/#google_vignette'

req = requests.get(tgurl)
page = req.content.decode('utf-8')
soup = BeautifulSoup(page, "html5lib")
#find img links
imglinks = soup.find_all('img')
#there's some srcs that aren't really src, I don't know why??? loop until the link is started with 'http'
img_id = random.randint(10, len(imglinks))
while imglinks[img_id].get('src')[:4] != 'http':
    img_id = random.randint(10, len(imglinks))
#download the img 
img = requests.get(imglinks[img_id].get('src'))
with open("./temp.jpg", "wb") as file:
    file.write(img.content)
#send img with line notify
for token in myToken:
    #you can modify the msg to whatever you want to send.
    #PLEASE DO NOT LEAVE msg WITH AN EMPTY STRING (i.e. '')!!!!!!! It will cause the msg unable to be sent. 
    lineNotify(token = token, msg = '親愛的朋友早安，祝福你有美好的一天。', picURI='./temp.jpg')