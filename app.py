# Gui for Convert function

import FreeSimpleGUI as gui
from convertor import convert

feet_label = gui.Text("Enter Feet: ")
feet_input = gui.Input(key = 'feets')
inch_label = gui.Text("Enter Inches: ")
inch_input = gui.Input(key = 'inches')

convert_button = gui.Button("Convert")
output_label = gui.Text(key = "output",text_color="white",)

window = gui.Window("Convertor",
                    layout = [[feet_label,feet_input],
                              [inch_label,inch_input],
                              [convert_button, output_label]],
                    font = (15))

while True:
    event , values = window.read()
    print(event,values)
    feet = values["feets"]
    inch = values["inches"]
    meters = convert(feet,inch)
    window["output"].update(value = f"{round(meters,2)}m")

window.read()
window.close()