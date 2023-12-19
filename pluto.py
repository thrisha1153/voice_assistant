import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')

#print(voices[0].id) -- DAVID
#print(voices[1].id) -  ZIRA
engine.setProperty('voice',voices[1].id)

#speaking rate default - 200
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-50)

#volume default 1 (100%)
volume=engine.getProperty('volume')
engine.setProperty('volume', volume+0.5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternon!")
    else:
        speak("Good Evening!")

    speak("Hello I am Pluto. Hope you are doing good. How can i help you?")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.energy_threshold=800
        r.pause_threshold=1
        audio=r.listen(source)
        try :
            print("Recognizing...")
            command=r.recognize_google(audio,language='en-in')
            print("The input is : ",command)
        except sr.RequestError:
            speak('Sorry my Service is down. Plz check your Internet connection')
        except sr.UnknownValueError:
            print('cant recognize')
            pass
    
    return command

if __name__ == "__main__":
    wish()
    while True:
        command=takecommand().lower()


        if ("name" in command) or ("what is your name" in command):
            speak("My name is Pluto")
        
        elif ("how are you" in command):
            speak("I am good.Hope you are doing great")

        #info from wikipedia
        elif "wikipedia" in command:
            speak("Searching Wikipedia....")
            command=command.replace("wikipedia","")
            info=wikipedia.summary(command,sentences=2)
            print(info)
            speak("According to wikipedia")
            speak(info)

        elif "about" in command:
            speak("Searching Wikipedia....")
            command=command.replace("wikipedia","")
            info=wikipedia.summary(command,sentences=2)
            print(info)
            speak("According to wikipedia")
            speak(info)

        elif ("open youtube" in command) or ("youtube" in command):
            webbrowser.open("youtube.com")

        elif ("bye" in command) or ("by" in command):
            speak("thank you bye")
            break

        


