import speech_recognition as sr

def speak(s):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('volume',1.0) #o to 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(s)
    engine.runAndWait()
    engine.stop()


r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something...")
    audio=r.listen(source)
    try:
        print("recognizing now")
        text=r.recognize_google(audio)
        print(text)
        
      
        if("hello Google"==text): 
            speak("hai this is google bot, how to i help you!!")

    except Exception as e:
        print("error:"+str(e))
    