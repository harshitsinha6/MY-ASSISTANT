import speech_recognition as sr
import os, webbrowser , extractinfo
import googlesearch
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def speech():
    
    r = sr.Recognizer()
    b = ''
    a = ''
    with sr.Microphone() as source:
        print('Say something.')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            txt = r.recognize_google(audio)
            c = txt.split()
            a = c[0]
            b = ' '.join(c)
            b = b.lstrip(a)
            b = b.lstrip(' ')
            #print('You said: '+ txt,'  ',  a,'  ', b)
            print('You said: '+ txt)

            if(a == 'play' or a == 'Play'):
                print('playing: ', b)
                extractinfo.opengoogle(b)
            elif(a == 'open'):
                if(b == 'college'):
                    webbrowser.open('http://www.soa.ac.in/iter/')
                elif(b == 'student'):
                    webbrowser.open('http://111.93.164.90:8282/CampusPortalSOA/index#/')
                elif(b == 'compete' or b == 'codearena'):
                    webbrowser.open('https://www.hackerearth.com/codearena/')
                else:
                    webbrowser.open('www.'+b+'.com')
            elif('search on Google about' in txt):
                txt1 = txt.split()
                txt1.remove('search')
                txt1.remove('on')
                txt1.remove('Google')
                txt1.remove('about')
                txt1 = ' '.join(txt1)
                print(txt1)
                webbrowser.open('https://www.google.com/search?q='+txt1)
        except:
            print('Sorry')

#os.system(b)
#speech()
#inm= input('Enter to exit:')
