# Vai dar pau se não instalar o PySimpleGui

#Para instalar coloque no CMD 'python -m pip install pysimplegui'




import PySimpleGUI as sg
b = ['pastel','ovo','banana']
a = 0


layout = [  [sg.Text(f'Vou comer seu {b[a]}', key='a')],
            [sg.Button('?'), sg.Button('EXPLODIR')] ]


window = sg.Window('Pastel, ovo, banana', layout)


while True:
    event, values = window.read()
    
    
    
    if event == sg.WIN_CLOSED or event == 'EXPLODIR':

        break
    elif event == '?':
        if a < 2:
            a += 1
        else:
            a = 0
        window['a'].update(f'Vou comer seu {b[a]}')
