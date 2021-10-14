import smtplib
import os
import webbrowser
import wikipedia 
import speech_recognition as sr
import datetime
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
#print(voices)
engine.setProperty('voice',voices[1].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant. How may i help you SIR??")
def takeCommand():
    #It takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening sir....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "none"
    return query
def sendEmail(to, content):
    server.ehlo()
    server.starttls()
    server.login('shyambhattarai057@gmail.com', '@@@ma@engineer###1')
    server.sendmail('shyambhattarai1999@gmail.com', to, content)
    server.close()
if __name__ =="__main__":
    #wishMe()
    while(True):
        query=takeCommand().lower()
    #logic for executing tasks based on query
    
        if "wikipedia" in query :
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak("Accordind to wikipedia")
            speak(results)
        elif "open youtube " in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "photo" in query:
            path="C:\\Users\\DELL\\Pictures\\Camera Roll\\shyam.jpg"
            os.startfile(path)
        elif " email " in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shyambhattarai057@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Shyam bhai. I am not able to send this email")