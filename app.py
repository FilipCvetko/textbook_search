import PySimpleGUI as sg
import os
from explorer import search
from config import *

img_size = (1000, 600)
full_fnames = [fname for fname in os.listdir(default_folder) if fname.endswith(".pdf")]

left = [
    [sg.Text("Choose textbooks folder: "), sg.In(default_folder,size=(50,1), change_submits=True, key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Text("Enter textbook: "), sg.Listbox(full_fnames,size=(40,20), key="-TEXTBOOK_LIST-", auto_size_text=True, enable_events=True)],
    [sg.Text('Enter input query: '), sg.InputText(key="-INPUT-")],
    [sg.Button("SEARCH", key="-SEARCH-"), sg.Button("ERASE", key="-ERASE-")],
]

right = [
    [sg.Image(key="-IMAGE-")],
    [sg.Text("Found what you're looking for? "), sg.Button("YES", key="-YES-"), sg.Button("NO", key="-NO-")]
]

layout = [
    [
        sg.Column(left),
        sg.VSeparator(),
        sg.Column(right)
    ]
]

window = sg.Window(title="Textbook search", layout=layout, resizable=True)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        dir = values["-FOLDER-"]
        full_fnames = [fname for fname in os.listdir(dir) if fname.endswith(".pdf")]
        window["-TEXTBOOK_LIST-"].update(full_fnames)

    if event == "-SEARCH-":
        text = values["-INPUT-"]
        textbook_file = values["-TEXTBOOK_LIST-"]
        to_open = (os.path.join(values["-FOLDER-"], textbook_file[0]))
        gen_obj = search(text, file=to_open)
        try:
            filename = next(gen_obj)
            window["-IMAGE-"].update(filename=filename)
           # window["-IMAGE-"].set_size(img_size)
        except:
            pass

    if event == "-NO-":
        try:
            filename = next(gen_obj)
            print(filename)
            window["-IMAGE-"].update(filename=filename)
            #window["-IMAGE-"].set_size(img_size)
        except:
            pass
       