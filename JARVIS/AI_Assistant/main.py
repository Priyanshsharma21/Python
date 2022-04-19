import os
import webbrowser
from datetime import datetime
import time

from AI_Assistant.features import base

from spotify_automation import main as spo
from spotify_automation import config

import kit
from wikipedia import wikipedia

from AI_Assistant.features.base import wishMe, takeCommand, speak, get_trending_movies, getNews, EDITH, advise, \
    sendEmail, singSong, send_whatsapp_message, todays_motivation, todays_wether, setAlaram, create_playlist, \
    open_camera, tell_joke, addTodo

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

        elif 'logout' in query:
            speak("Logging Out in 5 Second")
            time.sleep(5)
            os.system('shutdown - l')

        elif 'shutdown' in query:
            speak("Shutting Down in 5 Second")
            time.sleep(5)
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            speak("Restarting in 5 Second")
            time.sleep(5)
            os.system('shutdown /r /t 1')

        elif 'open spotify' in query:
            spotify = spo.Spotify()
            speak("which song you want me to search on spotify")
            sh = takeCommand().lower()
            speak(f'ok sir, opening spotify and playing {sh}')
            spotify.login(sh)

        elif 'todo' or 'today task' in query:
            speak("What should I name your todo list, sir")
            name_of_todo = takeCommand().lower()
            # speak("How many task do you wanna add, sir")
            # task = takeCommand().lower()
            # task = int(task , 10)
            items = []
            for i in range(0, 4):
                speak(f"Tell me the task {i}")
                ch = takeCommand().lower()
                items[i] = ch
            addTodo(name_of_todo,items)




        else:
            speak(f"Do you mean to say {query}")
            ch = takeCommand().lower()
            if 'yes' in ch:
                webbrowser.open(f'{query}')
            else:
                speak(f"Ok, can you Plese repeat")