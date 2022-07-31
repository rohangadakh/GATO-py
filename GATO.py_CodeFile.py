import speech_recognition as sr
import pyttsx3
import pyautogui as aug

global query

'''
import pyttsx3 - this library is used to convert the text to speech.
This is not the built-in so it means that we have to import it for that use command : pip install pyttsx3 
'''

engine = pyttsx3.init('sapi5')
# Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices = engine.getProperty('voices')
engine.setProperty("rate", 165)  # This command is used to make slow the voice of sapi5
engine.setProperty('voice', voices[1].id)  # voices[0], voices[1], voices[2],



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening   - ")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)
    try:
        print("Recognising - ")
        query = r.recognize_google(audio, language="en-in")
        print("Admin : {}".format(query).capitalize().title())
    except:
        # print("Can you please say that again !")
        return "none"
    query = query.lower()
    return query


if __name__ == '__main__':

    print(aug.position())
    print("Say Start.......")
    query = takeCommand()
while True:

    if "start" in query:
        print("Game Started....")
        while True:

            query = takeCommand()

            if "speed" in query:
                print(query)
                print("Car is Running")
                aug.mouseDown(692, 519, duration=3) 
                '''
                692, 519 are the co-ordinates for my Laptop, to find co-ordinates for your screen, take the mouse to that BREAK or GAS button and run the code.
                use this command to get the co-ordinates - print(aug.position())
                '''
            elif "break" in query:
                aug.mouseUp()
                print(query)
                print("Car is Reversing")
                aug.mouseDown(128, 509)
            elif "quit" in query:
                quit()
