import speech_recognition as sr
import os

while True:

    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as src:
        r.adjust_for_ambient_noise(src, duration = 1)
        audio = r.listen(src)

    text = r.recognize_google(audio)
    print("you said: " + text)

    if text == "exit":
        break

    elif text == "shut down":
        inpt = input("Are you sure?(y/n)")
        if inpt == "y":
            os.system('shutdown')
            break