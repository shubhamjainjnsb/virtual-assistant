import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys

def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Listening...")
            r.pause_threshold =  1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')# "hi-in" is code for hindi.
            print('User: ' + query + '\n')
            
        except sr.UnknownValueError:
            speak('Sorry sir! I didn\'t get that! please try again')
            myCommand()
            #query = str(input('Command: '))        #for typing the commands.
        return query

def speech_rep():
    
    engine = pyttsx3.init( )

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-1].id)

    def speak(audio):
        print('JTsstant: ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')

        if currentH >= 18 and currentH !=0:
            speak('Good Evening!')

    greetMe()

    speak("Hello Sir, I am JT'S digital assistant JTSSTANT!")
    speak('How may I help you?')

    if __name__ == '__main__':

        while True:
        
            query = myCommand();
            query = query.lower()
            
            if "open "in query:
                cnt=0
                for i in range(len(query)):
                    if query[i]==" ":
                        cnt+=1
                if cnt==1:
                    speak("done sir! Enjoy !")
                    x=query.split(' ', 1)[1]
                    site="www."+x+".com"
                    webbrowser.open(site)
                if query=="open youtube" :
                        speak("would you like to open any channel ?")
                        x=myCommand()
                        if x in"yes yeah yup":
                                speak("sure sir !  please speak the valid channel name")
                                y=myCommand()
                                webbrowser.open("www.youtube.com\y")                
                
                else:
                  #  speak("done sir! Enjoy !")
                    if query=="open google drive" :
                        webbrowser.open("drive.google.com")
                    elif query=="open google maps":
                        webbrowser.open("maps.google.com")
                    elif query=="open google translator":
                        webbrowser.open("translator.google.com")   
                    else:
                            x=query.split(' ', 1)[1]
                            site=x+".com"
                            webbrowser.open(site)
                
            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif 'nothing' in query or 'abort' in query or 'stop' in query:
                speak('okay')
                speak('Bye Sir, have a good day.')
                sys.exit()
               
            elif 'hello' in query:
                speak('Hello Sir !! How are you doing')

            elif 'goodbye' in query:
                speak('Bye Sir, have a good day.')
                sys.exit()
                                        
            elif 'play music' in query:
                speak('Okay, please try speaking the name of song')
                x=myCommand()
                webbrowser.open("youtube.com/x")
               # os.system("D:\Media\Music\videoplayback.m4a ")
                
            elif"what can you do" in query:
                speak("what do u want")
                speak("i can open youtube,google,gmail,send email and play music")

            elif "write something" in query:
                speak("got it  start speaking...")
                content = myCommand()
                print(content)

            elif "speak what i write" in query:
                x=input("Enter the text(#note pls dont press enter)")
                engine.say(x)
                engine.runAndWait
                
            else:
                query = query
                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('WOLFRAM-ALPHA says - ')
                        speak('Got it.')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(query, sentences=5)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
            
                except:
                    webbrowser.open('www.google.com')
            
            speak('Next Command! Sir!')

def  entry():
     r = sr.Recognizer()                                                                                   
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold =  1
         audio = r.listen(source)
     try:
         query = r.recognize_google(audio, language='en-in')# "hi-in" is code for hindi.
         print('User: ' + query + '\n')
        
     except sr.UnknownValueError:
         #speak('Sorry sir! I didn\'t get that! please try again')
         query = r.recognize_google(audio, language='en-in')

     while True:
             if query in "hello":
                     speech_rep()
             else:
                     entry()
entry()

