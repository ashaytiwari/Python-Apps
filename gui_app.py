import FreeSimpleGUI as sg
import utilities


def parse_tasks_list(_tasks):

    proper_tasks_list= []

    for index, task_item in enumerate(_tasks):
        proper_tasks_list.append(f"{index + 1}. {task_item}")

    return proper_tasks_list


title = sg.Text("Task Manager App: Manage your Tasks easily here!", font=('Helvetica', 18))

label = sg.Text("Type in a Task:")
task_input = sg.InputText(tooltip="Enter your task here", key="task")
add_button = sg.Button("Add", key='add_action')

tasks = utilities.get_tasks("tasks.txt")
tasks_list = parse_tasks_list(tasks)

task_list_box = sg.Listbox(
    values=tasks_list, 
    key="task_lists", 
    enable_events=True,
    size=[45, 10]
    )

layout = [[title], [label], [task_input, add_button], [task_list_box]]
font = ('Helvetica', 14)

window = sg.Window("Task Manager App", layout, font=font)


while True:
    event, values = window.read()
    print(event, values)

    match event:
        
        case "add_action":
            
            tasks = utilities.get_tasks('tasks.txt')
            tasks.append(values['task'] + '\n')
            utilities.write_tasks(filepath='tasks.txt', data=tasks)

            tasks_list = parse_tasks_list(tasks)

            """ update UI """
            window["task"].update(value='')
            window["task_lists"].update(values=tasks_list)

        case sg.WIN_CLOSED:
            break

window.close()