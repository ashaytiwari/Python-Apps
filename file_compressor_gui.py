import FreeSimpleGUI as sg

label = sg.Text('Compress your files in one go!')

label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
button1 = sg.FilesBrowse('Choose')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
button2 = sg.FolderBrowse('Choose')

row1 = [label1, input1, button1]
row2 = [label2, input2, button2]

compressButton = sg.Button('Compress')

layout = [[label], [row1], [row2], [compressButton]]

window = sg.Window('Compress Files', layout)

# Display and interact with the Window
event, values = window.read()   

window.close()