import PySimpleGUI as sg
from music import NOTES, create_scale

layout1 = [
    [sg.Text('Select key', size=(10, 1)), sg.DropDown(NOTES, readonly=True, size=(10, 1), key='-NOTE-')],
    [sg.Text('Scale type', size=(10, 1)), sg.Radio('Major', group_id='type', size=(5, 1), default=True, key='-MAJOR-'), sg.Radio('Minor', group_id='type', size=(5, 1), key='-MINOR-')],
    [sg.Button('Go!', key='-GO-'), sg.Button('Exit!', key='-EXIT-')]
]

layout_scales = [
    [sg.Text(size=(35, 1), key='-SCALE-', justification='center')]
]

layout_relative = [
    [sg.Text(size=(35, 1), key='-RELATIVE-', justification='center')]
]

layout_chords = [
    [sg.Text(size=(35, 14), key='-CHORDS-', justification='center')]
]

layout2 =[
    [sg.Frame('Scale', layout_scales
    )],
    
    [sg.Frame('Relative Scale', layout_relative
    )],
    
    [sg.Frame('Chords', layout_chords
    )],
    [sg.Button('Back', key='-BACK-')]
]

main_layout = [
    [
        sg.Column(layout1, key='-COL1-'),
        sg.Column(layout2, key='-COL2-', visible=False),
     ]
]

window = sg.Window('Music Theory', main_layout)

while True:
    event, values = window.read()
    print(event, values)
    
    if event in (None, '-EXIT-'):
        break
    
    if event == '-GO-':
        scale, relative, chords = create_scale(values['-NOTE-'], values['-MAJOR-'])
        window['-COL1-'].update(visible=False)
        window['-SCALE-'].update(scale)
        window['-RELATIVE-'].update(relative)
        window['-CHORDS-'].update(chords)
        window['-COL2-'].update(visible=True)
    
    if event == '-BACK-':
        window['-COL2-'].update(visible=False)
        window['-COL1-'].update(visible=True)
    
window.close()