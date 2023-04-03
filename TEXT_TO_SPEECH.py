import pyttsx3
import PySimpleGUI as sg

# initialize the engine
engine = pyttsx3.init()

# get available voices
voices = engine.getProperty('voices')

# assigning  voices
male_voice = voices[0].id
female_voice = voices[1].id

# define the layout of the GUI
layout = [
    [sg.Text("Enter text to speak:")],
    [sg.InputText(key="-INPUT-")],
    [sg.Text("Select voice:")],
    [sg.Radio("Male", "RADIO1", default=True, key="-MALE-"), sg.Radio("Female", "RADIO1", key="-FEMALE-")],
    [sg.Button("Speak"), sg.Button("Exit")]
]

# create the window
window = sg.Window("Text-to-Speech App", layout)

# main event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    text = values["-INPUT-"]
    if values["-MALE-"]:
        voice = male_voice
    else:
        voice = female_voice
    engine.setProperty('voice', voice)
    engine.say(text)
    engine.runAndWait()

# close the window and the engine
window.close()
engine.stop()