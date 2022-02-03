import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia
import webbrowser
import os
import pyautogui
import psutil 


engine = pyttsx3.init()
newVoiceRate = 250
engine.setProperty('rate', newVoiceRate)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def time():  

    Time = datetime.datetime.now().strftime('%I:%M:%S')


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("The date today is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back, master wayne")

    hour = datetime.datetime.now().hour

    if hour >=6 and hour <=12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour >=18 and hour <24:
        speak("Good Evening")
    else:
        speak("Good Night")
        

    speak("Alfred here, How can i help you sir")

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.energy_thresholdc=100
            r.adjust_for_ambient_noise(source, duration= 1)
            audio = r.listen(source)
            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            print(query)
            
        except Exception as e:
            print(e)
            speak("can you please GO again..")
            
            return "None"

        return query  
    
def screenshot():
    img =pyautogui.screenshot()
    img.save('C:\\Users\\Asus Zenbook\\Desktop\\Bhomikvoiceassistance\\screenshot\\ss.png')
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak(" CPU is at " + usage)
    
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

if __name__ == "__main__":

    wishme()
    
    while True:
        query = takeCommand().lower()
        
        if "time" in query:
            time()

        elif "date" in query:
            date()
        
        elif "offline" in query:
            speak("By, see you next time master wayne ")
            quit()
            
        elif "wikipedia" in query:
            speak("Searching Wikikpedia...")
            query = query.replace("wikipeadia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
            print(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "open github" in query:
            webbrowser.open("github.com")
            
        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")
        
        elif "play music" in query:
            music_dir = 'D:\\Chrome Downloads\\samplemusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "open chrome" in query:
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome_path)
             
        
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken ")
            
        elif "cpu" in query:
            cpu()
           
