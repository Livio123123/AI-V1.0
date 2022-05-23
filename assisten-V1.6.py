
import speech_recognition as sr
import os
import re
import webbrowser
import datetime
import time
import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output
   
   
   
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >=0 and currentH <12:
        a="Selamat Pagi Leon"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print("Selamat Pagi Leon")
    if currentH >=12 and currentH <18:
        a="Selamat Siang Leon"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print("Selamat Siang Leon")
    if currentH >=18 and currentH <0:
        a="Selamat Malam Leon"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print("Selamat Malam Leon")

greetMe()

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('Leon : ' + command + '\n')

    except sr.UnknownValueError:
        print('AI : Your last command couldn\'t be heard')
        a="try, again"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        command = myCommand();

    return command

def assistant(command):
    "if statements for executing commands"

    if 'hello' in command:
        a="Hello Leon"
        print('AI : Hello Leon')
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
    
    if 'open file manager' in command:
        a="open file manager laptop"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print("AI : open file manager laptop")
        time.sleep(1)
        os.system("nautilus")
    
    if 'lagu' in command:
        url = 'https://www.youtube.com/watch?v=f02mOEt11OQ'
        webbrowser.open(url)
    
    elif 'close browser' in command:
        os.system("killall firefox")
        a="close firefox"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print("ok")
    
    elif 'buka browser' in command:
        a="open browser firefox"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        os.system("firefox")
    


    elif 'open google' in command:
        reg_ex = re.search('google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        a="open google.com"
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
        execute_unix(c)
        print('Done!')
        
    elif 'open my web' in command:
        reg_ex = re.search('web (.*)', command)
        url = 'https://dunia73asal.blogspot.com'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            a="open website"
            c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
            execute_unix(c)
            print('Done!')
        else:
            pass
          
    elif 'toto' in command:
            a="close program AI"
            c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
            execute_unix(c)
            print('AI : sampai jumpa lagi Leon')
            exit()



while True:
    assistant(myCommand())