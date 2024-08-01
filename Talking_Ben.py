import pygame
from tkinter import *
import speech_recognition as sr
import random
import threading
from PIL import Image, ImageTk

pygame.mixer.init()

root = Tk()
root.title("Talking Ben")

ben_sit = PhotoImage(file='Ben_sitting.png')
ben_talk = PhotoImage(file='Ben_talking.png')
ben_sit_label = Label(root, image=ben_sit)
ben_talk_label = Label(root, image=ben_talk)
ben_sit_label.grid(row=0, column=0)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def ben_answer():
    poss = [1, 2, 3, 4, 5]
    answer = random.choice(poss)
    if answer == 1:
        play_sound('yes-101soundboards.mp3')
    elif answer == 2:
        play_sound('no-101soundboards.mp3')
    elif answer == 3:
        play_sound('uhh-101soundboards.mp3')
    elif answer == 4:
        play_sound('hohoho-101soundboards.mp3')
    elif answer == 5:
        return 'quit'

def speak():
    ben_sit_label.destroy()
    ben_talk_label = Label(root, image=ben_talk)
    ben_talk_label.grid(row=0, column=0)
    play_sound('phone-ring-101soundboards.mp3')
    play_sound('ben-101soundboards.mp3')

    recognizer = sr.Recognizer()

    def listen_and_respond():
        while True:
            with sr.Microphone() as source:
                print("Please say something:")
                audio = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio)
                    print("You said: " + text)
                except sr.UnknownValueError:
                    print("Sorry, I could not understand the audio")
                except sr.RequestError:
                    print("Could not request results; check your internet connection")

                response = ben_answer()
                if response == 'quit':
                    play_sound('phone-drop-1-101soundboards.mp3')
                    ben_talk_label.destroy()
                    ben_sit_label = Label(root, image=ben_sit)
                    ben_sit_label.grid(row=0, column=0)
                    break

    threading.Thread(target=listen_and_respond).start()

phone_button = Button(root, text="Talk to Ben", bg='green', command=speak)
phone_button.grid(row=1, column=0)

root.mainloop()
