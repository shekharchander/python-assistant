import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import pyttsx3
import webbrowser
engine = pyttsx3.init()
  
print("████████████████████████████████████████████████████████████████████████████████████████████")
print("█▄─▄▄─█▄─█─▄█─▄─▄─█─█─█─▄▄─█▄─▀█▄─▄████▀▄─██─▄▄▄▄█─▄▄▄▄█▄─▄█─▄▄▄▄█─▄─▄─██▀▄─██▄─▀█▄─▄█─▄─▄─█")
print("██─▄▄▄██▄─▄████─███─▄─█─██─██─█▄▀─█████─▀─██▄▄▄▄─█▄▄▄▄─██─██▄▄▄▄─███─████─▀─███─█▄▀─████─███")
print("▀▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Ask Questions. I will be Happy to Answer !!")
    speech = r.listen(source)
get = r.recognize_google(speech)
print(get)
soup =''
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64'
headers = {'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
search = requests.get("https://google.com/search?q="+get+"&num=3",headers=headers)
soup = BeautifulSoup(search.content, 'html.parser')
data = soup.find("div", {"data-tts":"answers"})
print("at 1")
answer = ""
if not data:
    data = soup.find("div", {"class": 'kp-header'})
    print("at 2")
    try:
        if(len(data.text)>20):
            data = soup.find("div", {"class": 'kno-rdesc'})
            print("at 3")
            if not data:
                reply = "Here are some of the top results"
            print("at 4")
            engine.say(reply)
            head = soup.find_all('h3')
            body = soup.find_all('span',{'class':'st'})
            link = soup.find_all('div',{'classs':'s'})
            for i in range(3):
                print(head[i].text)
                print(body[i].text)
                print(link[i].text)
                print("------------------------------------------------------------------------")
            else:
                data = data.find('div')
                data = data.find('span')
                answer = data
    except:
        pass
    if not data:
        reply = "Here are some of the top results"
        print("at 4")
        engine.say(reply)
        head = soup.find_all('h3')
        body = soup.find_all('span',{'class':'st'})
        link = soup.find_all('div',{'classs':'s'})
        for i in range(3):
            print(head[i].text)
            print(body[i].text)
            print(link[i].text)
            print("------------------------------------------------------------------------")
    else:
        answer = data.text
else:
    answer = data['tts-text']  
engine.say(answer)
engine.setProperty('rate',140)
engine.runAndWait()
