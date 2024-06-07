import pyttsx3 as p3
import speech_recognition as speech_recognition
import datetime
import webbrowser as wb
import pywhatkit
import wikipedia  


engine = p3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
query=[]
def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
      print("Listening.....")
      r.pause_threshold = 2
      r.energy_threshold = 300
      audio = r.listen(source,0,4)
    try:
      print("Understanding..")
      q = r.recognize_google(audio,language='en-in')
      print(f"You Said: {q}\n")
      
    except Exception as e:
      print("Say that again") 
      return "None"
    query.append(q)

def greetMe():
      hour  = int(datetime.datetime.now().hour+12)
      if hour>=0 and hour<=12: 
           speak("Good Morning,sir") 
      elif hour >12 and hour<=18:
           speak("Good Afternoon ,sir")
      else:
           speak("Good night,sir")
      speak("Please tell me, How can I help you ?")

def searchGoogle(query):
    if "Google" in query:
        import wikipedia as googleScrap
        query = query.replace("hey Jarvis","")
        query = query.replace("and search","")
        query = query.replace("open Google","")
        speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")
def searchYoutube(query):
    if "YouTube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("and search","")
        query = query.replace("open YouTube","")
        query = query.replace("hey Jarvis","")
        web = str("https://www.youtube.com/results?search_query= "+query[3:])
        print(web)
        wb.open(web)
def searchWikipedia(query):
    if "Wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace(" in Wikipedia","")
        query = query.replace("search","")
        query = query.replace("hey Jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)


def answer():
      if len(query[0]) >= 1:
             if "bhenchod" in query[(len(query)-1)]:
                 ans = "you are a gandu"
                 print(ans)
                 speak(ans)
            if "how are you" in query[(len(query)-1)]:
                  ans = "I am fine , What about you"
                  print(ans,"?")
                  speak(ans)
            if "I am fine" in query[(len(query)-1)]:
                  ans = "That's Great"
                  print(ans,"!!")
                  speak(ans)
            if "what can you do" in query[(len(query)-1)]:
                  ans = "i can try to do everything you ask me"
                  print(ans)
                  speak(ans)
            if "open Google and search" in query[(len(query)-1)]:
                  searchGoogle(query[(len(query)-1)])
                  query.append("stop")
            elif "open Google" in query[(len(query)-1)]:
                  speak("opening google")
                  print("Opening Google")
                  wb.open('https://www.google.com/')
                  query.append("stop")
            if "open YouTube and search" in query[(len(query)-1)]:
                  searchYoutube(query[(len(query)-1)])
                  query.append('stop')
            elif "open YouTube" in query[(len(query)-1)]:
                  speak("opening youtube ")
                  print("Opening YouTube")
                  wb.open('https://in.youtube.com/')
                  query.append("stop")
            
            if "open Instagram" in query[(len(query)-1)]:
                  speak("opening instagram")
                  print("opening instagram")
                  wb.open("https://www.instagram.com")
                  query.append("stop")
            if "open Wikipedia and search" in query[(len(query)-1)]:
                  searchWikipedia(query[(len(query)-1)])
                  query.append("stop")
            elif "open Wikipedia" in query[(len(query)-1)]:
                 speak("opening Wikipedia")
                 print("Opening Wikipedia....")
                 wb.open("https://www.wikipedia.org")
                 query.append("stop")
            if "open chat GPT" in query[(len(query)-1)]:
                 speak("opening chat g p t")
                 print("Opening Chatgpt")
                 wb.open("https://chatgpt.com")
                 query.append("stop")
def all_together():
   greetMe()
   while True:
      takecommand()
      if "stop" in query[(len(query)-1)]:
           break
      answer()
   
all_together()  
