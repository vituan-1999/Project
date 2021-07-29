import pyttsx3 as pt
import datetime
import speech_recognition as sr
import webbrowser as wb

# Describe: communicate with virtual_assistant
# Current_command:
#   google
#   youtube
#   what time is it
#   play music

boss = "Tuan"
virtual_assistant = "JARVIS"
speed = 145
VA = pt.init()  # khoi tao
voice = VA.getProperty("voices")    # lay giong
VA.setProperty("voice", voice[0].id)    # chon giong
VA.setProperty("rate", speed)
# voice[1].id: giong nu
# voice[0].id: giong nam

def speak(audio):   # bien string audio
    print(f"{virtual_assistant}: " + audio)
    VA.say(audio)
    VA.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("Now is " + Time)


def welcome():
    hour = datetime.datetime.now().hour    
    if hour >= 6 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour < 22:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")

    speak(f"I'm {virtual_assistant}")
    speak("Your personal virtual assistant")
    speak("How can I help you")


def again(query):
    import time
    time.sleep(3)
    speak("Do you want to continue sir ?")
    query = command().lower()
    if not "no" in query:
        speak("what else can i do for you sir")


def command():
    c = sr.Recognizer()                 # nhan dang giong noi
    with sr.Microphone() as source:     # source from microphone
        c.pause_threshold = 1           # wait 2s to recive command
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language = "en")    # command, nhan dien = google
        print(f"{boss}: " + query)
    except sr.UnknownValueError:                              # manual typing when voice error
        print("Please type again command: ",end="")
        query = str(input())
    return query


if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()                               # convert all command in lower
        if "google" in query:                                   # search google
            speak("What should I search sir")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"   # string url
            wb.get().open(url)                                  # webserver library
            speak(f"Here is your {search} on google")
        elif "youtube" in query:                                # search youtube
            speak("What should I search sir")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"  # string url
            wb.get().open(url)                                  # webserver library
            speak(f"Here is your {search} on youtube")
        elif "play music" in query:                             # open exiting video
            music = "https://www.youtube.com/watch?v=-R-xkfocsQc"
            wb.get().open(music)    # [ Autumn Leaves with Cat Vibe ] Jun-Hyuk Choi
        elif "what time is it" in query:
            time()            
        elif "quit" in query or "no" in query:
            speak(f"{virtual_assistant} will be stop. Goodbye sir")
            quit()
        again(query)
