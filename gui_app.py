import FreeSimpleGUI as sg
import utilities

title = sg.Text("Task Manager App: Manage your Tasks easily here!", font=('Helvetica', 18))

label = sg.Text("Type in a Task:")
task_input = sg.InputText(tooltip="Enter your task here", key="task")
add_button = sg.Button("Add", key='add_action')

layout = [[title], [label], [task_input, add_button]]
font = ('Helvetica', 16)

window = sg.Window("Task Manager App", layout, font=font)

while True:
    event, values = window.read()
    print(event, values)

    match event:
        
        case "add_action":
            tasks = utilities.get_tasks('tasks.txt')
            tasks.append(values['task'] + '\n')
            utilities.write_tasks(filepath='tasks.txt', data=tasks)

        case sg.WIN_CLOSED:
            break

window.close()