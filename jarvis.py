import datetime
import os
import random
import sys
import webbrowser as wb
from time import sleep
from plyer import notification
import PyPDF2
import keyboard
from requests import get
import instaloader
import psutil
import pyautogui
import pyjokes
import pyttsx3
#import speedtest
#import pywhatkit as kit
import speech_recognition as sr
import wikipedia
from playsound import playsound

engine = pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

newvoicerate=180
engine.setProperty('rate',newvoicerate)
#engine.say("hello world")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("hello ")

def time():
    #Time=datetime.datetime.now().strftime("%I:%M:%S")
    Time= datetime.datetime.now().strftime("%I:%M %p")
    speak("the current Time is")
    print(Time)
    speak(Time)

def date():
    import time
    Year=int(datetime.datetime.now().year)
    # Month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    m=time.strftime("%B")
    speak(f"Today's date is: {date} and it's {m} {Year} ")
    # tt=time.strftime("%A:%d:%B%Y")
    # print(tt)
    # speak(tt)

def wishme():

#     speak("initializing the system")
#     speak("Starting all systems applications")
#     speak("Installing and checking all driver and hardware")
#     speak("caliberating and exmamining all the core processors")
#     speak("checking the internet connection")
#     speak("wait a moment sir")
#     speak("All drivers are up and running")
#     speak("All systems have been activated")
#     speak("Now i am online")
#     speak("I am jarvis virtual A I Assistant. Online and ready sir. Please tell me how may i help you")

    speak("Welcome back sir!")

    playsound("arnold_audio\\Jarvis Start Up.wav")
    hour = datetime.datetime.now().hour
    Time = datetime.datetime.now().strftime("%I:%M %p")

    if hour >=0 and hour<=12:
        print(f"Good Morning Sir ,its {Time}")
        speak(f"Good Morning Sir, its {Time}")
    elif hour >=12 and hour <=18:
        print(f"Good Afternoon ,Sir its {Time}")
        speak(f"Good Afternoon ,its {Time}")
    else:
        print(f"Good night Sir ,its {Time}")
        speak(f"Good Night ,its {Time}")
 
def youtubeautomation():
    query= takecommand().lower()
    if "skip" in query or "forward " in query:
        pyautogui.press('l')
    elif "back" in query or "backward " in query:
        pyautogui.press('j')
    elif "restart " in query:
        pyautogui.press('O')
    elif "pause " in query:
        pyautogui.press('space bar')
    elif "resume" in query:
        pyautogui.press('space bar')
    elif "full screen " in query:
        pyautogui.press('f')
    elif "film mode" in query:
        pyautogui.press('t')
    elif "increase" in query or "volume increase":
        pyautogui.hotkey('shift','.')
    elif "decrease" in query or "low" in query or "volume low" in query:
        pyautogui.hotkey('shift',',')
    elif "previous " in query:
        pyautogui.hotkey('shift','p')
    elif "next" in query or "play next" in query:
        pyautogui.hotkey('shift','n')
    elif "search " in query:
        pyautogui.click(x=667,y=146)
        speak("what to search")
        search= takecommand()
        pyautogui.typewrite(search)
        pyautogui.press('enter')

    elif "mute" in query or "volume mute" in query:
        pyautogui.press('m')
    elif "unmute" in query or "volume unmute"in query:
        pyautogui.press('m')
    elif 'bye'in query or "go" in query:
        exit()
        #sys.exit()

def temperature():
    import bs4 #pip install beautifulsoup4
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r= get(url)
    data= BeautifulSoup(r.text,"html.parser")
    temperature= data.find("div",class_="BNeawe").text
    speak(f"the temperature outside is {temperature} celcius")

    speak("do i have to tell you another place temperature ?")
    next = takecommand()
    if "yes" in next:
        speak("tell me the name of the place")
        name = takecommand()
        search= search =f"temperature in {name}"
        url= f"https://www.google.com/search?q={search}"
        r=get(url)
        data =BeautifulSoup(r.text,"htnl.parser")
        temperature= data.find("div",class_="BNeawe").text
        speak(f"the temperature in {name} is {temperature} celcius")
    else:
        pass

def chromeauto():
    while True:
        query = takecommand().lower()
        #query=input("hello")
        if"new tab" in query or "open new tab " in query:
            pyautogui.hotkey('ctrl','t')
        elif"close tab" in query or "close this tab " in query:
            pyautogui.hotkey('ctrl','w')
        elif"new window" in query or "open new window " in query:
            pyautogui.hotkey('ctrl','n')
        elif"history" in query or "show me history " in query:
            pyautogui.hotkey('ctrl','h')
        elif "download" in query or "show me downlaod " in query:
            pyautogui.hotkey('ctrl', 'j')
        elif "bookmarks" in query or "crate bookmarks " in query:
            pyautogui.hotkey('ctrl','d')
        elif "incognito mode" in query:
            keyboard.press_and_release('ctrl+shift+n')
            # pyautogui.hotkey('ctrl', 'shift','n')
        elif "restore tabs" in query or "restore " in query:
            keyboard.press_and_release('ctrl+shift+t')

        elif "switch tab" in query or "switch the tab" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('tab')
            sleep(0.2)
            pyautogui.keyUp('ctrl')

        elif "break" in query or "bye" in query or "exit" in query:
            sys.exit()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)#,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said: {query}")
    except Exception as e:
        print(e)
        #speak("Say that again please..")
        return "none"
    return query

def sendmail(to,content):
    # noinspection PyUnresolvedReferences
    server =smtlib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    #here enter your email id and password
    server.login("xxxxxx@gmail.com","password")
    #here enter sender email id 
    server.sendmail("abc701@gmail.com",to,content)
    server.close()

def pdfreader():
    book = open('bookname.pdf','rb')
    reader= PyPDF2.PdfFileReader(book)
    pages= pdfReader.numPages
    speak(f"Total numbers of pages in this book  {pages}")
    speak("sir olease enter page number i have to read")
    pagenumber=int(input("enter page number:"))
    page= pdfReader.getPages(pagenumber)
    text= page.extractText()
    speak("sir i am start to read this book wait a second")
    speak(text)

def youtube_video_downloader():
    from pytube import YouTube
    speak("enter url of video ")
    link =input("Enter URL of Youtube video here..")
    url_of_video=YouTube(link)
    s=url_of_video.streams.first()
   #download video in highest resolution 
   # s=url_of_video.streams.get_highest_resolution()
    speak("sir video is downloading.. wait few seconds")
    s.downlaod()
    print("done sir")

    speak("done sir")
   
def setalarm(text):
    import alarm
    with open("alarm.txt",'a')as f:
        f.write(text)
        f.close()
    speak("sir alarm is set")
    alarm.alarm(text)
    os.startfile("alarm.py")
def screenshot():
    speak("Tell me the name for this screenshot file")
    name=takecommand().lower()
    name=input()
    speak("taking screenshot")
    img= pyautogui.screenshot()
    img.save(f"C:\\Users\\abc\\Music\\{name}.png")
    speak("done sir")
def cpu():
    usage= str(psutil.cpu_percent())
    speak(f"CPU is at { usage } percent usage")
def batteryb():
    battery = psutil.sensors_battery()
    
    speak(f"sir our system have {battery.percent} percent battery")
def jokes():
    print(pyjokes.get_joke())
    speak(pyjokes.get_joke())

def maincode():
    notification.notify(title="Start ",
                        message="I am online and ready to do task ",
                        app_icon=None,
                        timeout=3)
    playsound("arnold_audio\powerup.mp3")
    wishme()

    battery = psutil.sensors_battery()
    plug=p.power_plugged
    bb=battery.percent
    while True:

        #from win10 import 
        if plug==True:
            notification.notify(title="Charging",
                                message="Battery chargeing wait sometime to fill the battery",
                                app_icon=None,
                                timeout=5)
        if bb >20 and bb <=30 :
            notification.notify(title="battery",
                                message=f"battery status low please charge {bb} ",
                                app_icon=None,
                                timeout=2)
            speak(f'sir battery low , charge me its {bb} percent battery')
        elif bb>=12 and bb<=20:
            notification.notify(title="batter",
                                message=f"battery status low please charge and Remainig battery is {bb} ",
                                app_icon=None,
                                timeout=2)
            speak(f"we have very low power, please connect to charging the system will shutdown very soon")
        elif bb ==11 :
            speak(f'sir battery low,  please charge me we have very low power its {bb} percent battery')

        query = takecommand().lower()
        #query = input("eneter command")
        print(query)
        
        
        if "time" in query or "tell me the time"in query:
            time()
        elif "date" in query:
            date()

        elif"calendar"in query or "show me calendar" in query:
            import calendar
            c=calendar.TextCalendar().formatyear(2021)
            speak("sir now calendar are display on console you can go and check")
            print(c)

        elif "wikipedia" in query:
            speak("Searching...")
            query= query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences = 2)
            speak(result)
            print(result)
        elif "sendmail" in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="amit100lanki701@gmail.com"
                sendmail(to,content)
                speak("email send sucessfully")
            except Exception as e:
                speak(e)
                print(e)
                speak("unable to send the email")
        elif "search in chrome" in query:
            speak("what should i search?")
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            search= takecommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif "shutdown" in query or "shutdown the system" in query:
            os.system("shutdown /s /t 5")
        elif "logout" in query or "logout the system" in query:
            os.system("shutdown /r /t 5")
        elif "restart" in query or "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep" in query or "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "music" in query or "play music" in query:
            song_dir = "F:\\music\\new"
            songs= os.listdir(song_dir)
            rd= random.choice(songs)
            os.startfile((os.path.join(song_dir,rd)))
            #os.startfile(os.path.join(song_dir,songs[0]))
        elif "video" in query or "play video" in query:
            video_dir = "F:\\video"
            video= os.listdir(video_dir)
            rd= random.choice(video)
            os.startfile((os.path.join(video_dir,rd)))
            #os.startfile(os.path.join(song_dir,songs[0]))

        elif "play online music" in query or "play music online" in query:
            song = query.replace("play","")
            speak("playing..."+song)
            try:
                kit.playonyt(song)
            except Exception as e:

                print(e)

        elif "remember that" in query:
            speak("what should i remember?")
            data = takecommand()
            speak("you said me to remember" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you remember anything" in query:
            remember = open("data.txt","r")
            speak("you said me to remember that" + remember.read())
        elif "screenshot" in query or "ss" in query or "take a screenshot" in query:
            screenshot()
        elif "cpu" in query:
            cpu()
        elif "battery status" in query or "how much power left" in query:
            batteryb()
        elif "joke" in query or "tell me a joke" in query:
            jokes()

        # elif "tell me internet speed" or "what is my internet speed" in query:
        #     st= speedtest.Speedtest()
        #     d=st.download()
        #     dinmb=d/8000000
        #     up=st.upload()
        #     upinmb=up/8000000
        #     #speak(f"sir we have {d} bits per second downlading speed")
        #     #speak(f"and {up} bit per second uploading speed")
        #     speak(f"sir we have {dinmb} M B per second downloading speed")
        #     speak(f"and {upinmb} M B per second uploading speed")

         # elif"speed" in query:
        #     try:
        #         os.system('cmd /k "speedtest"')
        #     except:
        #         speak("error")

        #webbrowser
        elif "open facebook" in query or "facebook" in query:
            wb.open("https://www.facebook.com")
        elif "open olx" in query or "olx" in query:
            wb.open("https://www.olx.in")
        elif "open google" in query or "google" in query:
            wb.open("https://www.google.com")
        elif "open ebay" in query or "ebay" in query:
            wb.open("https://www.ebay.com")
        elif "open twitter" in query or "twitter" in query:
            wb.open("https://www.twitter.com")

        elif "open amazon" in query or "amazon" in query:
            wb.open("https://www.amazon.in")
        elif "open flipkart" in query or "flipkart" in query:
            wb.open("https://www.flipkart.com")
        elif "open instagram" in query or "instagram" in query:
            wb.open("https://www.instagram.com")
        elif "open youtube" in query or "youtube" in query:
            wb.open("https://www.youtube.com")
            youtubeautomation()
        elif "open stackoverflow" in query or "stackoverflow" in query:
            wb.open("https://www.stackoverflow.com")
        elif "open investing" in query or "investing" in query:
            wb.open("https://www.investing.com")
        elif "open gmail" in query or "gmail" in query:
            wb.open("https://www.gmail.com")
        #apps
        elif"open chrome" in query or "chrome" in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening Chrome")
            os.startfile(path)
    
        elif"open vscode" in query or "vscode" in query:
            path = "C:\\Program Files\\Microsoft VS Code\\code.exe"
            speak("opening Chrome")
            os.startfile(path)
    
        elif "open command prompt" in query or "cmd" in query:
            speak("opening CMD")
            os.system("start cmd")
        elif "open notepad" in query or "notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("opening Notepad")
            os.startfile(path)

        #close apps
        elif "close chrome" in query or "chrome close" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "close cmd" in query:
            speak("ok sir, closing... cmd")
            os.system("TASKKILL /f /im cmd.exe")

        elif "close notepad" in query:
            speak("ok sir, closing...notepad")
            os.system("TASKKILL /f /im notepad.exe")
        elif"close vscode" in query:
            speak("ok sir , closing .. vscode")
            os.system("taskkill /f /im code.exe")

        #computer automation

        elif "open my computer" in query or "my computer" in query:
            speak("opening my computer...")
            pyautogui.hotkey('win','e')
        elif "open setting" in query:
            speak("open settings")
            pyautogui.hotkey('win', 'i')
        elif "show display setting" in query or "display setting" in query:
            pyautogui.hotkey('win', 'u')
        elif "show start" in query:
            pyautogui.press('win')
        elif "minimize" in query or "desktop" in query:
            pyautogui.hotkey('win','m')
        elif "maximize" in query or "restore window" in query:
            #pyautogui.hotkey('win','shift','m')
            pyautogui.hotkey('win','d')
        elif "open search" in query or "search" in query:
            pyautogui.hotkey('win','s')

        elif "magnifier" in query:
            pyautogui.hotkey('ctrl','+')

        elif "show magnifier" in query:
            keyboard.press_and_release('ctrl+win+m')
        elif "volume up" in query:
            pyautogui.press('volumeup')
        elif "volume down" in query:
            pyautogui.press('volumedown')
        elif "mute" in query:
            pyautogui.press('volumemute')
        elif "what is my ip" in query:
            speak("wait sir, let me check")
            ip = get('https://api.ipify.org').text
            speak(ip)
        elif"where i am" in query or "tell me my location" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ip=get('https://api.ipify.org').text
                print(ip)
                url= 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
                geo_request= get(url)
                geo_data=geo_request.json()
                #print(geodata)
                city= geo_data['city']
                #state =geo_data['state']
                country =geo_data['country']
                speak(f"sir i am not sure ,but i think we are in {city} city of {country} country")
            except Exception as e:
                print("sorry sir ,due to network issue i am not abke to find where we are")
                pass
        elif "tell me temperature" in query or "what is the temperature" in query:
            speak("wait sir, let me check")
            temperature()

        elif "instagram profile" in query or "show instagram profile" in query:
            speak("sir please enter the user name correctly")
            name = input("enter username :")
            wb.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            sleep(2)
            speak("sir would you like to download profile picture of the account.")
            usercondition = takecommand()

            if "yes" in usercondition:
                mod= instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("i am done sir! , profile picture is saved")
            else:
                pass

        elif"locate" in query:
            speak("wait i sir")
            query=query.replace('locate ',"")
            url=f"https://googlemap.com/{query}"
            wb.open(url)
            

        elif "audio book" in query or "read book" in query:
            speak("reading book ")
            pdfreader()
        elif "set alarm" in query:
            setalarm(query)
        elif"camera" in query or "open camera"in query:
            speak("opening camera")
            subprocess.run("start microsoft.windows.camera:",shell=True)

        elif 'find location' in query or "show me the location of this number" in query :
            import phonenumbers
            from phonenumbers import geocoder,carrier,timezone
            speak("enter phone number to check location")
            number= input("enter phone number to check location: ")
            #ch_number=phonenumbers.parse("enter mobile number")
            ch_number= phonenumbers.parse(number,'CH')
            #print the country name
            print(geocoder.description_for_number(ch_number,"en"))
            #print the servie provider
            print(carrier.name_for_number(ch_number,"en"))
            #print the timezone
            print(timezone.time_zones_for_number(ch_number))
        
            serial_num=phonenumbers.parse(number,'RO')
            print(carrier.name_for_number(serial_num,"en"))
        
        elif"video downloader" in query or "youtube video downlaod" in query:
            speak("wait sir")
            youtube_video_downloader()

        elif"activate how to do mode" in query or "how to do mode" in query:
            #from pywikihow import search_wikihow
            speak("How to do mode in activated please tell me what you want to how ")
            tell=takecommand()
            max_result =1
            how_to= search_wikihow(tell,max_result)
            assert len(how_to) ==1
            how_to[0].print()
            speak(how_to[0].summary)

        elif "exit" in query or "gooffline" in query or "go offline" in query:
            speak("ok sir!!")
            speak("closing all system application")
            speak("disconectiong to server")
            #speak("disconnecting to internet")
            speak("i am going offline")
            playsound("arnold_audio\\power down.mp3")
            sys.exit()

        elif "visible all files" in query or "visible this folder" in query:
            os.system("attrib -h /s /d")
            speak("sir , all the files in this folder are now visible to everyone")

        elif "switch" in query or "switch the window"in query:
            pyautogui.hotkey('alt','tab')
        elif "create new folder" in query:
            pyautogui.hotkey('ctrl','shiftleft','n')
       
        elif "hide all files" in query or "secure this folder"in query:
            os.system("attrib +h /s /d")
            speak("sir , all the files in this folder are now hidden")

        # elif "switch the window" or "switch" in query:
        #     pyautogui.keyDown("alt")
        #     pyautogui.press("tab")
        #     sleep(0.2)
        #     pyautogui.keyUp("alt")

        elif "fun" in query or "lets do fun" in query:
            wb.open("https://www.youtube.com/feed/trending")
        else:
            var= query.replace(' '," ")
            url= f"https://www.google.com/search?q=+{temp}"
            speak("sorry sir i can't understand but i searchfrom internet to give your answer? okay")
            speak("wait a few second")
            wb.open(url)



if __name__ == "__main__":
    maincode()
