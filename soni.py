import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Soni. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    r.adjust_for_ambient_noise(source)
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
    
        audio = r.listen(source, timeout=15)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aman135kumar@gmail.com', 'vhin xztm rbcs oemq')
    server.sendmail('aman135kumar@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open word' in query:
            wordpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\Word.lnk"  
            os.startfile(wordpath)


        elif 'play music' in query:
            music=random.randint(0, 347)
            music_dir = "Z:\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[music]))  
            print(music)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\Arjun narayann\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open firefox" in query:
            firefox = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefox)

        elif 'email' in query:
            try:
                speak("Who should I send the email to?")
                speak("What should I say?")
                content = takeCommand()
                to =  takeCommand().lower()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Aman. I am not able to send this email") 
        elif "about you" in query:
            print("I am soni programmed by aman on 10 january 2023. I am designed to assist you and automate tasks ")
            speak("I am soni programmed by aman on 10 january 2023. I am designed to assist you and automate tasks ")

        elif "exit" or "quit" in query:
            break
        elif ("laugh" or "jokes") in query:
            print("how do you get a squirrel to like you?\n","Act like a 'nut'")
            speak("how do you get a squirrel to like you? Act like a 'nut'")
        

      
