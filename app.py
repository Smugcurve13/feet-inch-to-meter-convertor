# Gui for Convert function

import FreeSimpleGUI as gui
from convertor import convert

gui.theme("Black")

feet_label = gui.Text("Enter Feet: ")
feet_input = gui.Input(key = 'feets')

inch_label = gui.Text("Enter Inches: ")
inch_input = gui.Input(key = 'inches')

convert_button = gui.Button("Convert", key="convert")
exit_button = gui.Button("Exit",key='exit')
output_label = gui.Text(key = "output",text_color="white",)

window = gui.Window("Convertor",
                    layout = [[feet_label,feet_input],
                              [inch_label,inch_input],
                              [convert_button, exit_button ,output_label]],
                    font = (15))

while True:
    event , values = window.read()
    print(event,values)
    feet = values["feets"]
    inch = values["inches"]
    meters = convert(feet,inch)
    match event:
        case 'convert':
            window["output"].update(value = f"{round(meters,3)}m")
        case 'exit':
            break

window.read()
window.close()