import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'name1': 'email1@gmail.com',
    'name2': 'email2@gmail.com',
    'name3': 'email3@gmail.com',
    'name4': 'email4@gmail.com',
    'name5': 'email5@gmail.com'
}


def get_email_info():
    talk('Who do you want to send the email to?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me what you would like to say in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Email has been sent')
    talk('Do you want to send another email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
