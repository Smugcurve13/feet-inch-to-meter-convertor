import FreeSimpleGUI as gui

feet_label = gui.Text("Enter Feet: ")
feet_input = gui.Input()
inch_label = gui.Text("Enter Inches: ")
inch_input = gui.Input()

convert_button = gui.Button("Convert")
output_label = gui.Text(key = "output",text_color="red")

window = gui.Window("Convertor",
                    layout = [[feet_label,feet_input],
                              [inch_label,inch_input],
                              [convert_button, output_label]])

window.read()
window.close()