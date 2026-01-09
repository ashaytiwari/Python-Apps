import FreeSimpleGUI as sg
import utilities

label = sg.Text('Compress your files in one go!')

label1 = sg.Text('Select files to compress:')
input1 = sg.Input(key="selected_files")
button1 = sg.FilesBrowse('Choose', key="choose_files")

label2 = sg.Text('Select destination folder:')
input2 = sg.Input(key="selected_path")
button2 = sg.FolderBrowse('Choose', key="choose_path")

row1 = [label1, input1, button1]
row2 = [label2, input2, button2]

compressButton = sg.Button('Compress', key="compress")
response_text = sg.Text(key='response')

layout = [[label], [row1], [row2], [compressButton, response_text]]

window = sg.Window('Compress Files', layout)

while True:
    event, values = window.read()
    print(event, values)

    if values['selected_files'] == '' or values['selected_path'] == '':
        window['response'].update(value="Please select files and destination folder before compressing!", text_color='pink', )
        continue

    match event:
        
        case "compress":
            filepaths = values['selected_files'].split(';')
            folder_path = values['selected_path']

            utilities.make_zip_archive(filepaths, folder_path)

            window['response'].update(value="File Compressed successfully!", text_color='green')
            window['selected_files'].update(value='')
            window['selected_path'].update(value='')

        case sg.WIN_CLOSED:
            break;   

window.close()