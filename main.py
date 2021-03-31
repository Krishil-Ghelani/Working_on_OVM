import datetime

import pyautogui as autog
import virtualbox
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')  # creating a voice obj
voices = engine.getProperty('voices')   # getting voice
engine.setProperty('voice', voices[0].id)   # selecting voice


def speak(audio):
    '''this function is used to
    speak the given string'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():   # it will wish acording to time ever time when it will run
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak('good afternoon!')
    else:
        speak('good evening!')


def takeCommand():
    """ this function will take the command from the user and analyse it according to the
    sentence spoken by the user and return it in the form of string."""
    # the return type is only ""STRING""
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")

        # r.energy_threshold = 200
        r.phrase_threshold = 1

        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said {query}\n")

        except Exception as e:
            print(e)
            speak("i did not get that, can you please repeat it?")
            return 'None'
        return query


wishMe()


# nested if-else begins here
if __name__ == '__main__':
    speak("hello sir, i am your personal assistant jarvis, how may i help you?")
    while True:
        query = takeCommand().lower()
        if "start hacking" or "open ovm" or "open vm" or "open virtualbox" or "open virtual machine"in query:
            import booting_up_VM
            booting_up_VM.Virtual()