from plyer import notification,vibrator
import requests
from bs4 import BeautifulSoup
import time

myState = "Maharashtra"

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "virus.ico",
        timeout = 15
    )

def getData(url):
    temp = requests.get(url)
    return temp.text

while True:
    if __name__ == "__main__":
        myHTMLData = getData("https://www.mohfw.gov.in/")
        soup = BeautifulSoup(myHTMLData, 'html.parser')

        myDataStr = ""
        num = 0
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            num += 1
            myDataStr +=  tr.get_text()

        totalItems = []
        for item in myDataStr.split("\n\n")[:num-2]:
            totalItems += [item.split("\n")]

        for item in totalItems:
            if item[1] == "Maharashtra":
                showMsg = "number of confirmed cases : "+item[2]+"\nnumber of cured : "+item[3]+"\nnumber of deaths : "+item[4]
                notifyMe("status of Maharashtra",showMsg)
                time.sleep(2)

        mytemp = ""
        for item in myDataStr.split("\n\n")[num-2:num+1]:
            mytemp += item
        
        showMsg = "number of confirmed cases : "+mytemp[41:46]+"\nnumber of cured : "+mytemp[47:51]+"\nnumber of deaths : "+mytemp[52:55]
        notifyMe("status of India",showMsg)

    time.sleep(3600)