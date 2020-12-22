#!/usr/bin/env python3

"""
Attempt to write a gui
I want it to open a file
apply the clean
and save the file to the same place
then let me choose another or close
"""

import PySimpleGUI as sg


def clean_rewards(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if 'Reward' in line:
                lines.remove(line)
    with open(filename, 'w') as f:
        for line in lines:
            if 'Quest' in line:
                f.write(line)
                f.write('\n')
            else:
                f.write(line)
                f.write('\n\n')


sg.theme('DarkBlack')  # what other theme could there be?

# step 1 define layout
# noinspection PyTypeChecker
layout = [
    [sg.Text("Choose a file to clean.")],
    [sg.Input(key='-FILE-'), sg.FileBrowse(file_types=(("Text Files", "*.txt"),))],
    [sg.Button('Clean'), sg.Button('Exit')]
]

# step 2 create window
window = sg.Window("Quest List Cleaner", layout, grab_anywhere=True)

# step 3 event loop
while True:
    event, values = window.read()  # Read the event that happened and the values dictionary
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':  # exit if user closes window or clicks exit
        break
    if event == 'Clean':
        clean_rewards(values['-FILE-'])
        sg.popup_ok("Done!")
window.close()
