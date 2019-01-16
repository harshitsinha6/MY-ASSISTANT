import speech_recognition as sr
from gtts import gTTS as gts
import os, time, give_ans

def listen_audio():
    r = sr.Recognizer()
    txt = ''
    with sr.Microphone() as source:
        print('Say something.. ')
        audio = r.listen(source)

        try:
            txt = r.recognize_google(audio)
            print('You said: ' + txt)
        except:
            print('Cannot able to recog. ')
    return txt
#listen_audio()


def speak(audioString):
    gtt = gts(text = audioString, lang = "en")
    gtt.save("speech_recognition_final.mp3")
    os.system("speech_recognition_final.mp3")
    

def Question_and_Answer(inputTxt):
    txt = ''
    try:
        if(inputTxt == 'quit'):
            txt = 'quit'
        elif(inputTxt == 'what is the time'):
            #print(time.ctime())
            txt = time.ctime()      
        elif(inputTxt == 'what is your name'):
            #print('My Name is ASKY')
            txt = 'My Name is ASKY'    
        elif(inputTxt == 'what is Java'):
            #print("""Java is a general-purpose
              #computer-programming language that is concurrent, class-based, object-oriented, and specifically designed
                  #to have as few implementation dependencies as possible""")
            txt = """Java is a general-purpose
                  computer-programming language that is concurrent, class-based, object-oriented, and specifically designed
                  to have as few implementation dependencies as possible ....."""
        elif(inputTxt == 'what is Hadoop'):
            #print("""Apache Hadoop is a collection of open-source software utilities that facilitate using a network of many computers to solve problems involving massive amounts of data and computation. It provides a software framework for distributed
                  #storage and processing of big data using the MapReduce programming model""")
            txt = """Apache Hadoop is a collection of open-source software utilities that facilitate using a network of many computers to solve problems involving massive amounts of data and computation. It provides a software framework for distributed
                  storage and processing of big data using the MapReduce programming models ....."""    
        elif(inputTxt == 'what is your speciality'):
            #print('I would like to answer your question.')
            txt = 'I would like to answer your question.'
        elif(inputTxt == 'what is your age'):
            #print('what is your age')
            txt = 'same as yours'    
        elif(inputTxt == ''):
            #print('')
            txt = 'cannot recognise'   
        elif(inputTxt == 'who is Ayushman'):
            #print('')
            txt = 'aysuhman is bajarang bali'
        elif(inputTxt == 'who is pushpa'):
            #print('')
            txt = 'pushpa is mummy'
        elif(inputTxt == 'who is Gullu'):
            #print('')
            txt = 'gullu is gulli mulli'
        elif(inputTxt == 'what are you doing'):
            #print('')
            txt = 'answering your question'
    except:
        txt = 'cannnot able to recognise'

    return txt


def main():
    while True:
        audioString = listen_audio()
        audioString.lower()
        if(audioString == "stop"):
            break
        else:
            if('tell me something about' in audioString):
                st = audioString
                STRING = st.split()
                STRING.remove('tell')
                STRING.remove('me')
                STRING.remove('something')
                STRING.remove('about')
                st = ' '.join(STRING)
                #print('--> ', st)
                ans = give_ans.find_wiki(st)
                #print(ans)
                speak(ans)
            else:
                ans_string = Question_and_Answer(audioString)
                speak(ans_string)
        break

#main()

#inp = input('Enter to exit:')
