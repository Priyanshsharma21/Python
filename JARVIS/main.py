# -----------------Use to setup voics from windows---------------------------
import pyttsx3
# -----------------Datetime-----------------------------------
from datetime import datetime
# ----------------------SpeechRecognition--------------------------------
import subprocess as sp
import speech_recognition as sr
# ---------------------To work with wikipedia---------------------------------------
import wikipedia
# --------------------------To open any site-------------------------------------
import webbrowser
# ---------------------------Play music---------------------------------------
import os
# -------------------------pywhatkit--------------------
from newsapi import NewsApiClient
from twilio.rest import Client
# -------------------------------------------
from smtplib import SMTP
# --------------------------------------------------
import pygame
from pygame import mixer
import requests
import random
import pywhatkit as kit
from spotifyp import Spotify

# from Twitter import InternetSpeedTwitterBot
# ---------------------------wether apis--------------------------------------------
API_Key = "f7cd520b1c47239d2ab0ab7be491dad8"
URL = "https://api.openweathermap.org/data/2.5/onecall"
# ----------------------------------------------------------------------
account_sid = "AC55baa23c3f99306ec5716664ae584ec8"
auth_token = "0aca884ebdbbf048d536f394958efe10"
Number = "+14155238886"
# ----------------------------------------------------------------
engine = pyttsx3.init('sapi5')  # microsoft devlope speech api
voices = engine.getProperty('voices')  # voices list (male and female)
engine.setProperty('voice', voices[1].id)
# =================================================================
pygame.init()

# ------------------------------------------------------------
month_name = ["None", "January", "febuary", "match", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]


def speak(audio):
    """This function will speak whatever argument you pass in"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """This function will wish you on basis of your current time"""
    time = datetime.now()
    hour = int(time.hour)

    if 0 <= hour < 12:
        speak("GoodMorning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")

    speak(
        "Hello Priyansh, i am EDITH,  Tony Stark's augmented reality security and defense system. What can i do for you")


def EDITH():
    speak("EDITH stands for Even Dead, I'm The Hero")


def takeCommand():
    """Take input from your speeker and perform task"""
    ear = sr.Recognizer()
    with sr.Microphone() as source:
        assistant_sound = mixer.Sound('tidin.wav')
        assistant_sound.play()
        print("Listening......")
        ear.energy_threshold = 600
        ear.pause_threshold = 1
        # If we take break between speaking it will not consider as sentence
        audio = ear.listen(source)

    try:
        print("Recognizing......")
        query = ear.recognize_google(audio, language='en-in')
        print(f"User said '{query}'\n")

    except Exception as e:
        print("Please say that again...........")
        return "None"
    return query


def sendEmail(to, contant):
    with SMTP('smtp.gmail.com') as connection:
        EMAIL = "piyuindia220@gmail.com"
        PASSWORD = "Piyu@412002"
        connection.ehlo()
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addr=to, msg=f"Subject:Mail From AI \n\n {contant}")


def todays_wether():
    parameters = {
        "lat": 22.176401,
        "lon": 76.068199,
        "exclude": "current, minutely, daily",
        "appid": API_Key
    }

    res = requests.get(URL, params=parameters)
    res.raise_for_status()

    data = res.json()
    weather_slice = data["hourly"][:12]

    for wether_data in weather_slice:
        condition_rain = wether_data["weather"][0]["id"]
        condition_rain = int(condition_rain)

        if 200 <= condition_rain < 300:
            speak("Thunder Strome today , be careful")
            break
        elif 300 <= condition_rain < 400:
            speak("Dizzle weather today, bring umbrella today")
            break
        elif 500 <= condition_rain < 600:
            speak("Rain today,bring umbrella")
            break
        elif 600 <= condition_rain < 700:
            speak("Snow today, bring umbrella")
            break
        elif 700 <= condition_rain < 800:
            speak("Foggy weather today")
            break
        elif condition_rain == 800:
            speak("Enjoy the clear sky today")
            break
        else:
            speak("Cloudy weather today")
            break


def singSong():
    speak(f"""When I was 13, I had my first love
    There was nobody that compared to my baby
    And nobody came between us who could ever come above
    She had me going crazy, oh I was starstruck
    She woke me up daily, don't need no Starbucks

    She made my heart pound
    I skip a beat when I see her in the street
    And at school on the playground
    But I really wanna see her on a weekend
    She know she got me dazin' 'cause she was so amazin'
    And now my heart is breakin' but I just keep on sayin'

    Baby, baby, baby, oh
    Like baby, baby, baby, no
    Like baby, baby, baby, oh
    I thought you'd always be mine, mine""")


def send_whatsapp_message(message):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'{message}',
        to='whatsapp:+919826392951'
    )


def story():
    speak(
        "Once upon a time there was a king and a queen, king died, story over, Would you like to listen more story sir")


def todays_motivation():
    with open("data/quotes.txt") as quote:
        r_q = quote.readlines()
        random_quote = random.choice(r_q)
        speak(random_quote)


# def speedTest():
#     os.startfile('C:\\Users\\priya\\PycharmProjects\\JARVIS\\Twitter.py')
#     # bot = InternetSpeedTwitterBot()
#     # bot.get_internet_speed()
#     # bot.tweet_at_provider()

def getNews(topic, category):
    # newsapi = NewsApiClient(api_key='3ccdd2feb04e4191a2b89d6bd724c655')
    # top_headlines = newsapi.get_top_headlines(q=f'{topic}',
    #                                           sources='bbc-news,the-verge',
    #                                           category=f'{category}',
    #                                           language='en',
    #                                           country='in')
    # sources = newsapi.get_sources(top_headlines)
    # speak(sources)
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={'3ccdd2feb04e4191a2b89d6bd724c655'}&category={category}&topics={topic}").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    speak(news_headlines[:5])


def get_trending_movies():
    TMDB_API_KEY = "00a03104170d378e428ff62054eea698"
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    speak(trending_movies[:5])


def setAlaram(query):
    timeHere = open("C:\\Users\\priya\\PycharmProjects\\JARVIS\\data\\data.txt", mode="a")
    timeHere.write(query)
    timeHere.close()
    speak("Done sir......")
    os.startfile("C:\\Users\\priya\\PycharmProjects\\JARVIS\\Alarm.py")


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def create_playlist(year, month, day):
    # if int(month)<10 :
    #     month = f"0{month}"
    # if int(day)<10:
    #     day = f"0{day}"
    name_of_month = month_name[int(month)]
    speak(f"Creating playlist of year {year} month {name_of_month}, {day}")
    spotifyobj = Spotify(year, month, day)
    spotifyobj.create_playlist()


def tell_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    joke = res["joke"]
    speak(joke)


def advise():
    res = requests.get("https://api.adviceslip.com/advice").json()
    advise =  res['slip']['advice']
    speak(advise)


if __name__ == '__main__':
    wishMe()
    sunrahaHuMai = True

    while sunrahaHuMai:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open('http://www.youtube.com')

        elif 'play song on youtube' in query:
            speak("Which song you like to play")
            print("Which song you like to play.....")
            song_req = takeCommand().lower()
            kit.playonyt(f"{song_req}")


        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')

        elif 'trending movies' in query:
            get_trending_movies()


        elif 'thank you' in query:
            speak("No problem Bro, Anytime")

        elif 'open hyper' in query:
            hyper_path = "C:\\Users\\priya\\AppData\\Local\\Programs\\Hyper\\Hyper.exe"
            os.startfile(hyper_path)
            speak("Opening hyper terminal")

        elif 'latest news' in query:
            speak(
                "Please tell me the catogery you like to listen on: business, entertainment, sports, science, technology, general")
            print("What topic news you are intrested in:")
            catogery = takeCommand().lower()

            speak("What topic news you are intrested in:")
            print("What topic news you are intrested in:")
            topic = takeCommand().lower()

            getNews(topic, catogery)


        elif 'open stackoverflow' in query:
            speak("opening StackOverflow")
            webbrowser.open('http://www.stackoverflow.com')

        elif 'what it means' in query:
            EDITH()

        elif 'open udemy' in query:
            speak("opening Udemy")
            webbrowser.open('http://www.udemy.com')

        elif 'play music' in query:
            speak("playing music from local library")
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'who are you' in query:
            speak("I am EDITH your personal assistant sir, How can i help you")

        elif 'the time' in query:
            strTime = datetime.now().strftime('%H:%M:%S')
            speak(f"Priyansh, time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\priya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak(f"Opening visual studio code")

        elif 'advise for me' in query:
            advise()

        elif 'send email' in query:
            try:
                speak(f"what should I say?")
                print("What should i say?")
                content = takeCommand().lower()
                to = 'piyuindia4@gmail.com'
                sendEmail(to, content)
                speak(f"Email has been send!")
            except:
                speak(f"sorry bhai, mai email nahi bhaj paya")

        elif 'sing a song' in query:
            singSong()

        elif 'send whatsapp' in query:
            try:
                speak(f"what should I say?")
                print("What should i say?")
                message = takeCommand().lower()
                send_whatsapp_message(message)
                speak(f"Message has been send!")
            except:
                speak(f"Mission abboted ! I repeat mission abboted")


        elif 'i want to send whatsapp' in query:
            speak("Whome should i send , message sir, can you tell me number")
            number = takeCommand().lower()
            speak(f"what should I say sir")
            message = takeCommand().lower()
            kit.sendwhatmsg_instantly(f"+91{number}", message)

        elif 'today motivation' in query:
            todays_motivation()

        elif 'today weather' in query:
            todays_wether()

        elif 'exit me' in query:
            speak(f"Exiting, I hope you like my service, call me whenever you want me")
            sunrahaHuMai = False

        # elif 'internet speed test' in query:
        #     if 'internet speed test' in query:
        #         speedTest()

        elif 'set alarm' in query:
            speak("What time sir......")
            cm = takeCommand().lower()
            setAlaram(cm)

        elif 'make a playlist of songs on spotify' in query:
            speak("Which year playlist sir........")
            year = takeCommand().lower()
            speak("Which month sir....")
            print("Which month sir....")
            month = takeCommand().lower()
            speak("Which day sir.....")
            print("Which day sir.....")
            day = takeCommand().lower()

            create_playlist(year, month, day)

        elif 'open camera' in query:
            open_camera()

        elif 'tell me a joke' in query:
            tell_joke()


        else:
            speak(f"Do you mean to say {query}")
            ch = takeCommand().lower()
            if 'yes' in ch:
                webbrowser.open(f'{query}')
            else:
                speak(f"Please repeat.........")

