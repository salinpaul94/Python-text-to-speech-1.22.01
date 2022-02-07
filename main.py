import time
import guiTkinter
from gtts import gTTS


def text_to_speech(filename, filepath):
    # Open text file in read mode
    test = open(filepath, "rt")

    # Read text from file and store in variable my_text
    my_text = test.read()

    # Select conversion language
    language = "en"
    print("Started converting text ot speech")

    # Pass the text and language to gtts library for converting to audio
    my_obj = gTTS(text=my_text, lang=language, slow=False)

    # Save output file to .mp3 format
    my_obj.save(filename+".mp3")
    print("Saved to file {0}".format(filename))
    time.sleep(120)
    print("\n\nBye")


# Calling custom library to ask user to select input file and store the file path
filepath1 = guiTkinter.select_file()

# Ask the user for the output file name
filename1 = input("Please enter file name: ")

# Calling function and pass filepath and filename to start conversion to audio
text_to_speech(filename1, filepath1)
