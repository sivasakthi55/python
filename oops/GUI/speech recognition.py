import speech_recognition as sr
import webbrowser as wb
r=sr.Recognizer()
google="https://www.google.com/search?q="
youtube="https://www.youtube.com/results?search_query="
with sr.Microphone() as source:
    print("say something...")
    audio=r.listen(source)
    try:
        print("reconizing now...")
        text=r.recognize_google(audio) 
        wb.get().open_new(google+text)
        wb.get().open_new(youtube+text)
    except Exception as e:
        print("error:"+str(e))