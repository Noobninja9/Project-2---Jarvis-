import pyttsx3                   #module 1       #pip install pyttsx3 
import speech_recognition as sr  #module 2       #pip install speechRecognition
import datetime                  #module 3
import wikipedia                 #module 4       #pip install wikipedia
import webbrowser                #module 5
import os                        #module 6
import requests

from utils import opening_text
from random import choice
from os_ops import paths,open_cmd
from online_ops import find_my_ip,play_yt,search_on_google,get_random_joke,get_random_advice

from weather_rep import get_weather_report

#creating speech engine
engine = pyttsx3.init('sapi5')  # Microsoft speech API - windows gives an api through which we can get voice.(for inbuilt voice ) 
voices = engine.getProperty('voices')
#print(voices)   #--- to know how many voices we have on our computer
engine.setProperty('voice',voices[1].id)     #print(voices[0].id) -- to know the name of voices we have.
engine.setProperty('rate',180) #voice speed

#defining speak function
def speak(audio):
    engine.say(audio) # the engine will spell the audio string
    engine.runAndWait() #it is a function

#defining the greet function
def wishMe():
    hour = int(datetime.datetime.now().hour) #time in hour ko int me typecast kr liya h which gives int value from 0 to 24
    if hour>=0 and hour<12:
        print("Jarvis : Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Jarvis : Good Afternoon!") 
        speak("Good Afternoon!")

    else:
        print("Jarvis : Good Evening!")
        speak("Good Evening!")

    print("I am Jarvis! Your Smart Virtual Desktop Assistant,Please tell me how may I help you?")  
    speak("I am Jarvis! Your Smart Virtual Desktop Assistant,Please tell me how may I help you?")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()  #Recognizer class will help in recognizing audio
    with sr.Microphone() as source:   #we use it as source microphone
        print("Listening...")
        r.pause_threshold = 1 #use to take time after pause in speech
        r.adjust_for_ambient_noise(source) #to counter the ambient noises so that my microphone can hear it clearly
        audio = r.listen(source) #all this coming from speech recognition module  

        print("Recognizing...")
        
    try:  #we use it when we feel there comes an error
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  #we are using f string for printing

        if not 'quit' in query:
            speak(choice(opening_text)) #reply after recognizing our speech
        else:
            speak("Have a good day sir!")

    except Exception as e: #if its not recognized then it sends to exception block where we can print the exception error
        print(e) #we used it to show error in the console  and DON'T FORGET TO COMMENT IT
        speak('Sorry, I could not understand. Could you please say that again?')
        print("Sorry, I could not understand. Could you please say that again?") 
        return "None"   #returning a string none
    
    return query

#main function      
if __name__ == "__main__":
    #speak("Anwesh is good guy!") --- testing the speech recoginition

    wishMe()

    #takeCommand() for testing the recognition


    while True:
    #if 1:
        query = takeCommand().lower() #converting into lowercase so that it can match to our if-else keyword
    
        #logic for executing tasks based on query

        #wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","") #replacing term wikipedia with blank 
            results = wikipedia.summary(query, sentences=2) # take 2 sentences from the summary of wikipedia
            speak("According to wikipedia")
            print(results) #displaying the result
            speak(results) #speaking the result
        
        #search on yt
        elif 'on youtube' in query:
            query = query.replace("on youtube","")
            speak("Got it! Here is the recommended video for your query.")
            play_yt(query)

        #yt
        elif 'youtube' in query:
            speak("Opening the youtube!")
            webbrowser.open("youtube.com")    #from module webbrowser

        #search on google
        elif 'on google' in query:
            speak("I found the best result for you.")
            query = query.replace("on google","")
            search_on_google(query)


        #google
        elif 'google' in query:
            speak("Opening google search engine!")
            webbrowser.open("google.com")

        #fb
        elif 'facebook' in query:
            speak("Opening facebook for you sir!")
            webbrowser.open("facebook.com")

        #linkedin
        elif 'linkedin' in query:
            speak("Opening linkedin for you sir!")
            webbrowser.open("linkedin.com")

        #get my ip
        elif 'ip' in query:
            ip = find_my_ip()
            print("Your IP is " + ip)
            speak("Your IP address is"+ip)
            
        
        #musicplayer
        elif 'music' in query:
            speak("Let me play music for you sir!")
            music_dir = 'E:\\Anwesh\\Songs\\Poco F1 Song' #we are using double backslash character so that we can escape it 
            songs = os.listdir(music_dir) #list all the songs of the directory #using from module os      
            print(songs) #print all the songs
            os.startfile(os.path.join(music_dir,songs[0])) #open the file at index 0

        #time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") #get the time in string format
            speak(f"Sir,the time is{strTime}") 

        #chrome
        elif 'chrome' in query:
            speak("Opening Chrome for you sir!")
            #codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
            os.startfile(paths['chrome'])  

        #calculator
        elif 'calculator' in query:
            speak("Opening Calculator for you sir!")
            #codePath = "C:\\Windows\\System32\\calc.exe" 
            os.startfile(paths['calculator'])
        
        #notepad    
        elif 'notepad' in query:
            speak("Here we go,Opening notepad for you sir!")
            os.startfile(paths['notepad'])
        
        #cmd
        elif 'command prompt'in query:
            speak("opening command prompt!")
            open_cmd()    
        
        #weather report
        elif 'weather report' in query:
            speak("Getting the weather report for your city!")
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Weather report for your city {city}")
            weather,temperature,feels_like = get_weather_report(city)

            speak(f"The current temperature of your city is around {temperature},but it feels like {feels_like}")
            speak(f"And the weather report talks about {weather}")
            speak(f"I am printing all the details on the screen for you.")
            print(f"City: {city}\nDescription: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        
        #random joke
        elif 'joke' in query:
            speak("Here we go sir,hope you like this one!")
            joke = get_random_joke()
            speak(joke)
            print(f"Jarvis : "+joke)
            speak("For your convenience I had printed the joke so that you can go through it. ")

        #random advice   
        elif 'advice' in query:
            speak("If you want some then here is an advice for you sir!")
            advice = get_random_advice()
            speak(advice)
            print(f"Jarvis : "+advice) 
            speak("For your convenience I had printed my advice so that you can go through it.")

        #quiting the JARVIS Program
        elif 'quit' in query:
            print("Jarvis : Quiting the Smart Virtual Desktop Assistant ,Sir")
            speak("Quitting the Smart Virtual Desktop Assistant ,Sir!")
            break

        

