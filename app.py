import PySimpleGUI as sg
from explorer import search

sg.theme_previewer()

img_size = (1000, 600)

layout = [
    [sg.Text('Enter input query: '), sg.InputText(key="-INPUT-")],
    [sg.Button("SEARCH", key="-SEARCH-"), sg.Button("ERASE", key="-ERASE-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("YES", key="-YES-"), sg.Button("NO", key="-NO-")]]

window = sg.Window(title="Hello World", layout=layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

    if event == "-SEARCH-":
        text = values["-INPUT-"]
        print(text)
        gen_obj = search(text)
        try:
            filename = next(gen_obj)
            window["-IMAGE-"].update(filename=filename)
            window["-IMAGE-"].set_size(img_size)
        except:
            pass

    if event == "-YES-":
        try:
            filename = next(gen_obj)
            print(filename)
            window["-IMAGE-"].update(filename=filename)
            window["-IMAGE-"].set_size(img_size)
        except:
            pass
       