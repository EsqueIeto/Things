import PySimpleGUI as sg
b = ['pastel','ovo','banana']
a = 0

# All the stuff inside your window.
layout = [  [sg.Text(f'Vou comer seu {b[a]}', key='a')],
            [sg.Button('?'), sg.Button('EXPLODIR')] ]

# Create the Window
window = sg.Window('Pastel, ovo, banana', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'EXPLODIR':

        break
    elif event == '?':
        if a < 2:
            a += 1
        else:
            a = 0
        window['a'].update(f'Vou comer seu {b[a]}')