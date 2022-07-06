import json
import time
import urllib.request
import webbrowser
from pydoc import text
from webbrowser import get
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
import wikipedia
import pywhatkit as kit
import smtplib
import sys
import winshell as winshell
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#convert voice into text


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception:
        speak("say that again please...")
        return "none"
    query = query.lower()
    return query


def TaskExecution():
    wish()
    while True:
        query = takecommand()

        def xpath(param):
            pass


def xpath(param):
    pass


def pizza():
    driver = webdriver.Chrome("C:\\Users\\hp\\Desktop\\chromedriver.exe")

    driver.maximize_window()
    speak("opening dominos")

    driver.get('https://www.dominos.co.in/')
    sleep(2)

    speak("getting ready to order")
    driver.find_element(by=By.LINK_TEXT, value='ORDER ONLINE NOW').click()

    speak("finding your location")
    driver.find_element(by=By.CLASS_NAME, value='srch-cnt-srch-inpt').click()
    sleep(2)

    location = "a b c"

    speak("entering your location")
    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input'
                        ).send_keys(location)
    sleep(2)

    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div[2]/span[1]'
                        ).click()
    sleep(2)

    try:
        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]'
                            ).click()
        sleep(2)

    except:
        speak("your location could not be found. Please try again later")
        exit()

        speak("logging in")

        phone_num = "7030144323"

        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]'
                            ).send_keys(phone_num)
        sleep(2)

        speak("what is you OTP")

        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input'
                            ).click()
        sleep(2)

        speak("do you want to order from your favourites")
        query_fav = rec_audio()

        if "yes" in query_fav:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/button/span'
                                    ).click()
                sleep(2)

            except:
                speak("the entered OTP is not correct")
                exit()

            speak("do you want to add extra cheese to your pizza")
            ex_cheese = rec_audio()
            if "yes" in ex_cheese:
                speak("extra cheese added")
                driver.find_element(by=By.XPATH, value='').click()
            elif "no " in ex_cheese:
                driver.find_element(by=By.XPATH, value='').click()
            else:
                speak("i dont know that")
                driver.find_element(by=By.XPATH, value=''
                                    ).click()
                sleep(1)
                driver.find_element(by=By.XPATH, value='').click()
                sleep(10)

                speak("would you like to increase the quantity?")
                qty = rec_audio()
                qty_pizza = 0
                qty_pepsi = 0
                if "yes" in qty:
                    speak("would you like to increase the quantity of pizza?")
                    wh_qty = rec_audio()
                    if "yes" in wh_qty:
                        speak("how many more pizzas would you like to add?")
                        try:
                            qty_pizza = rec_audio()
                            qty_pizza = int(qty_pizza)
                            if qty_pizza > 0:
                                talk_piz = f"adding {qty_pizza} more pizzas"
                                speak(talk_piz)
                                for i in range(qty_pizza):
                                    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div'
                                                        ).click()
                        except:
                            speak(" i dont know that")

                    else:
                        pass

                    speak("would you like to increase the quantity of pepsi")
                    pep_qty = rec_audio()
                    if "yes " in pep_qty:
                        speak("How many pepsis would you like to add")
                        try:
                            qty_pepsi = rec_audio()
                            qty_pepsi = int(qty_pepsi)
                            if qty_pepsi > 0:
                                talk_pep = f"adding {qty_pepsi} more pepsis"
                                speak(talk_pep)
                                for i in range(qty_pepsi):
                                    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[1]/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div'
                                                        ).click()
                        except:
                            speak("i dont know that")
                    else:
                        pass
                elif "no " in qty:
                    pass

                    total_pizza = qty_pizza + 1
                    total_pepsi = qty_pepsi + 1
                    total_num = f"this is your list of orders {total_pizza} pizzas and {total_pepsi} pepsis. Do you want to checkout?"
                    speak(total_num)
                    check_order = rec_audio()
                    if "yes" in check_order:
                        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
                                            ).click()
                        sleep(1)
                        total = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[5]/span[2]/span'
                                                    )
                        total_price = f'total price is {total.text}'
                        speak(total_price)
                        sleep(1)
                    else:
                        exit()

                    speak("placing your order")
                    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button'
                                        ).click()
                    sleep(2)
                    try:
                        speak("saving your location")
                        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input'
                                            ).click()
                        sleep(2)
                    except:
                        speak("the store is currently offline")

                    speak("do you want to confirm your order")
                    confirm = rec_audio()
                    if "yes" in confirm:
                        speak("placing your order")
                        driver.find_element(by=By.XPATH, value='yespqgtes//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button/span'
                                            ).click()
                        sleep(2)
                        speak(
                            "your order is placed successfully, wait for dominos to deliver your order. Enjoy your dat")
                    else:
                        exit()
                else:
                    exit()

#wish


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yashg.cse20@sbjit.edu.in', 'prateek2002')
    server.sendmail('yashgiradkar02@gmail.com', to, content)
    server.close()


def call(text):
    action_call = "assistant"

    text = text.lower()
    if action_call in text:
        return True

    return False


def say_hello(text):
    greet = {"hi", "hola", "greetings", "wassup", "hey there"}

    response = {"hi", "hey", "greetings", "howdy"}

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + ","

    return ""


def rec_audio():
    pass


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand()
        # if "wake up" in permission:
        #     TaskExecution()
        # elif "sleep" in permission:
        #     speak("thanks for using me sir")
        #     sys.exit()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:/Windows/system32/notepad.exe"
            os.startfile(npath)

        # for closing any application
        # elif "close notepad" in query:
        #     speak("okay sir, closing notepad")
        #     os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "shut down the system" in query:
            os.system("shutdown /s /t ")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(
                    f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak(
                    "sorry sir, due to network issue i am not able to find where we are")
                pass

        elif "news" in query:
            url = ('https://newsapi.org/v2/everything?'
                   'country=in&'  # country api here
                   'q=Apple&'
                   'from=2022-06-03&'
                   'sortBy=popularity&'
                   'apiKey=3f14f4cfd0cd4cc8ad6da425bc2de3f7')

            try:
                response = requests.get(url)
            except:
                speak("please check your connection")

            news = json.loads(response.text)

            for news in news['articles']:
                print(str(news["description"]), "\n")
                speak(str(news["description"]))
                engine.runAndWait()

        elif "open camera" in query:
            vid = cv2.VideoCapture(0)
            while (True):
                ret, frame = vid.read()
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            vid.release()

            cv2.destroyAllWindows()

        elif "open mobile camera" in query:
            import requests
            import cv2
            import numpy as np
            import imutils
            url = "http://192.168.0.103:8080/shot.jpg"

            # While loop to continuously fetching data from the Url
            while True:
                img_resp = requests.get(url)
                img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                img = imutils.resize(img, width=1000, height=1800)
                cv2.imshow("Android_cam", img)

                # Press Esc key to exit
                if cv2.waitKey(1) == 27:
                    break

            cv2.destroyAllWindows()

        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptyed")

        elif "play music" in query:
            music_dir = "E:\\Music\\Bollywood Songs\\Albums\\New Songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak("your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "http://www.youtube.com/results?search_query=" +
                "+".join(search)
            )
            speak = speak + "opening " + str(search) + "on youtube"

        elif "search" in query:
            ind = text.lower().split().index("search")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "http://www.google.com/search?q=" + "+".join(search)
            )
            speak = speak + "searching" + str(search) + "on google"

        # elif "google" in query:
        #     ind = text.lower().split().index("google")
        #     search = text.split()[ind + 1:]
        #     webbrowser.open(
        #         "http://www.google.com/search?q=" + "+".join(search)
        #     )
        #     speak = speak + "searching" + str(search) + "on google"

        elif "dont listen" in query or "shut up" in query:
            speak("for how many seconds do you want me to sleep")
            a = int(rec_audio())
            time.sleep(a)
            speak = speak + str(a) + \
                "seconds completed. how can i help you sir "

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google chrome" in query:
            speak("opening google chrome")
            os.startfile(
                "C:\\Users\hp\AppData\Local\Google\Chrome\Application\chrome.exe")

        # elif "open google" in query:
        #     speak("sir, what should i search on google")
        #     cn = takecommand().lower()
        #     webbrowser.open(f"{cn}")

        elif "send message" in query:
            kit.sendwhatmsg("+917030144323", "this is testing protocol", 20, 4)

        elif "play song on youtube" in query:
            kit.playonyt(("Believer"))

        elif "who are you " in query or "define yourself" in query:
            speak("""Hello, i am your assistant. your assistant. I am here to make your life easier. you can command me to 
            perform various tasks """)

        elif "your name" in query:
            speak("my Name is Jarvis")

        elif "how are you " in query:
            speak("i am fine, thank you")

        elif "order a pizza" in query or "pizza" in query:
            pizza()

        elif "email to yash" in query:
            try:
                speak("what should i write")
                content = takecommand().lower()
                to = "yashgiradkar02@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to yash")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send the email")

        elif "no thanks" in query:
            speak("happy to help you sir")
        sys.exit()
