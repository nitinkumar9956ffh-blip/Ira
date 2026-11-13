import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    print("Ira:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("सुन रहा हूँ...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="hi-IN").lower()
    except Exception:
        return ""

def run():
    speak("नमस्ते, मैं Ira हूँ। बताइए क्या करूँ?")
    while True:
        cmd = listen()
        print("आपने कहा:", cmd)
        if "समय" in cmd or "time" in cmd:
            speak(datetime.datetime.now().strftime("अभी %I बजकर %M मिनट हुए हैं"))
        elif "यूट्यूब" in cmd or "youtube" in cmd:
            speak("यूट्यूब खोल रही हूँ")
            webbrowser.open("https://youtube.com")
        elif "गूगल" in cmd or "google" in cmd:
            speak("गूगल खोल रही हूँ")
            webbrowser.open("https://google.com")
        elif "बंद" in cmd or "exit" in cmd or "stop" in cmd:
            speak("अलविदा!")
            break

run()
