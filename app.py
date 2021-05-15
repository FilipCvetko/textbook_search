import PySimpleGUI as sg

layout = [
    [sg.Image('haha.png')]
]

window = sg.Window(title="Hello World", layout=layout, margins=(500,300))

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break