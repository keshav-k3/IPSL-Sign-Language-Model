# main.py
import os

from cffi.setuptools_ext import execfile
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import pyttsx3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from gtts import gTTS
from playsound import playsound


class VoiceBasedEmail(Screen):
    recipient_email = ObjectProperty(None)
    subject = ObjectProperty(None)
    content = ObjectProperty(None)

    # def submit(self):
    #     sm.current = "login"

    def __init__(self, **kw):
        super().__init__()
        self.recognizer = None

    def open_menu(self):
        self.reset()
        sm.current = "menu"

    def reset(self):
        self.recipient_email.text = ""
        self.subject.text = ""
        self.content.text = ""

    def listen(self):
        with sr.Microphone() as source:
            print("Speak:")
            audio = self.recognizer.listen(source)
            message = self.recognizer.recognize_google(audio)
        return message

    def send_email(self, instance):
        try:
            self.recognizer = sr.Recognizer()
            recipient_email = "joeljacobstephen@gmail.com"
            self.recipient_email.text = recipient_email
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voices', voices[1].id)
            engine.setProperty('rate', 150)

            # create a gTTS object and save it as an mp3 file
            # tts = gTTS("Speak your subject")
            # tts.save("subject.mp3")
            #
            # # play the mp3 file using the playsound library
            # playsound("subject.mp3")
            sentence = "Speak your subject"
            engine.say(sentence)
            engine.runAndWait()

            with sr.Microphone() as source:
                print("Speak your subject:")
                audio = self.recognizer.listen(source)
                subject = self.recognizer.recognize_google(audio)

            self.subject.text = subject
            print(subject)

            # tts = gTTS("Speak your email content")
            # tts.save("content.mp3")
            # playsound("content.mp3")
            sentence = "Speak your email content"

            engine.say(sentence)
            engine.runAndWait()

            with sr.Microphone() as source:
                print("Speak your email content:")
                audio = self.recognizer.listen(source)
                message = self.recognizer.recognize_google(audio)

            print(message)

            sender_email = "1nh19cs077.keshavkk@gmail.com"
            sender_password = "ippqmezujyrlruan"
            content = self.content.text + "\n\n" + message
            self.content.text = content

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            text = MIMEText(content)
            msg.attach(text)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()

            self.show_popup("Success", "Email sent successfully.")
            # tts = gTTS("Email Sent Successfully")
            # tts.save("success.mp3")
            # playsound("success.mp3")
            sentence = "Email sent successfully"

            engine.say(sentence)
            engine.runAndWait()
        except Exception as e:
            print(e)
            self.show_popup("Error", "Failed to send email.")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


class Menu(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def open_ipsl(self):
        # sm.current = "ipsl"
        # execfile('app.py')
        os.system('python app.py')
        
    def open_vbe(self):
        sm.current = "vbe"

    def reset(self):
        self.subject.text = ""
        self.content.text = ""


class IPSL(Screen):
    n = ObjectProperty(None)
    content = ObjectProperty(None)
    subject = ObjectProperty(None)
    current = ""

    def on_enter(self, *args):
        pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

sm = WindowManager()
screens = [Menu(name="menu"), VoiceBasedEmail(name="vbe"), IPSL(name="ipsl")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "menu"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
