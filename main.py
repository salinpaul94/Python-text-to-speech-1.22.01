import time

from gtts import gTTS


def text_to_speech(filename):
    test = open("test.txt", "rt")
    mytext = test.read()
    language = "en"
    print("Started converting text ot speech")
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename+".mp3")
    print("Saved to file {0}".format(filename))
    time.sleep(120)
    print("\n\nBye")


filename1 = input("Please enter file name: ")

text_to_speech(filename1)
