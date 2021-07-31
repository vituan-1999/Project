"""
    File: main.py
    Describe: virtual assistant use API, version 2.0
    Author: Trieu Vi Tuan
    Date: 31/07/21
"""
import pyttsx3 as pt
import datetime as date
import speech_recognition as sr
import webbrowser as wb
import wikipedia as wiki
"""
Current_command:
    # friendly: hello, goodbye, good morning
    # search web: google, youtube, facebook, wikipedia
    # daily task: time
    # boss, virtual_assistant variable can be personally modified
"""

boss = "Tuan"
virtual_assistant = "BayMax"
speed = 145
VA = pt.init()
voice = VA.getProperty("voices")        # get voice
VA.setProperty("voice", voice[0].id)    # select voice
VA.setProperty("rate", speed)
# voice[1].id: female voice
# voice[0].id: male voice

def speak(audio):   # string string audio
    print(f"{virtual_assistant}: " + audio)
    VA.say(audio)
    VA.runAndWait()


def time(_type):
    if "time" in _type:
        Time = date.datetime.now().strftime("%I:%M:%p")
        speak("Now is " + Time)
    else:
        Date = date.datetime.now().strftime("%d %B %Y")
        speak("Today is " + Date)


def good_morning_night():
    hour = date.datetime.now().hour    
    if hour >= 6 and hour < 12:
        speak("Good Morning, today is the beautiful day")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Half of the day is over;\
               have a marvelous afternoon and enjoy the rest of the day!")
    elif hour >= 18 and hour < 22:
        speak("Good Evening, how are you today")
    else:
        speak("Good Night, have a nice dream")


def welcome():
    speak(f"Hi, I'm {virtual_assistant}")
    speak("Your personal virtual assistant")
    speak("How can I help you")

def command():
    voice_data = sr.Recognizer()                                       # voice recognize
    with sr.Microphone() as mic:                                       # source from microphone
        audio = voice_data.record(mic, duration=3)
    try:
        query = voice_data.recognize_google(audio, language = "en")    # command, recognize by google
        print(f"{boss}: " + query)
    except sr.UnknownValueError:                                       # manual typing when voice error
        query = ""
    return query


if __name__ == "__main__":
    welcome()  
    while True:     
        query = command().lower()    # convert all command in lower 
        
        # hello task
        if "hi" in query or "hello" in query:
            speak("hi friend")
            speak("i'm here, what can I do for you")
        elif "good morning" in query or "good afternoon" in query \
              or "good evening" in query or "good night" in query:
            good_morning_night()
        elif "introduce" in query:
            welcome()
        elif "quit" in query or "goodbye" in query or "bye" in query:
            speak(f"{virtual_assistant} goes to sleep now. Goodbye friend")
            break
        elif "name" in query:
            speak(f"My name is {virtual_assistant}")
            speak("Nice to meet you")

        # entertainment task
        elif "music" in query:  # open exiting video
            music = "https://www.youtube.com/watch?v=gNy5e1--Dgg"
            wb.get().open(music)    # Best lullaby for meow (Meowssage) #2

        # time task
        elif "time" in query:
            time("time")
        elif "date" in query or "today" in query:
            time("date")

        # search web task 
        elif "google" in query:                                 # search google
            speak("What should I search friend")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"   # string url
            wb.get().open(url)                                  # webserver library
            speak(f"Here is your {search} on google")
        elif "youtube" in query:                                # search youtube
            speak("What should I search friend")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"  # string url
            wb.get().open(url)                                  # webserver library
            speak(f"Here is your {search} on youtube")
        elif "facebook" in query:
            url = "https://www.facebook.com/"                   # string url
            wb.get().open(url)                                  # webserver library
            speak(f"Here is your facebook")
        elif "dictionary" in query:
            try:
                wiki.set_lang("en")
                speak("What should I search friend")
                search = command().lower()
                speak(wiki.summary(search, sentences=1))         
            except:
                speak(f"Sorry, I don't know {query}")
        # other task
        elif "" in query:                                       # no one say
            print("I'm listening... :)")
        else:
            speak("sorry friend, could you say that again")
