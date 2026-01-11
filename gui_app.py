import FreeSimpleGUI as sg
import utilities


def parse_tasks_list(_tasks):

    proper_tasks_list= []

    for index, task_item in enumerate(_tasks):
        proper_tasks_list.append(f"{index + 1}. {task_item}")

    return proper_tasks_list


def get_actual_task_text(_task):
    
    task_text = _task.split('.')[1].strip()
    return task_text


title = sg.Text("Task Manager App: Manage your Tasks easily here!")

label = sg.Text("Type in a Task:")
task_input = sg.InputText(tooltip="Enter your task here", key="task")
add_button = sg.Button("Add", key='add_action')

tasks = utilities.get_tasks("tasks.txt")
tasks_list = parse_tasks_list(tasks)

edit_info_label = sg.Text("Click from the below list to edit/complete the task.")

task_list_box = sg.Listbox(
    values=tasks_list, 
    key="task_lists", 
    enable_events=True,
    size=[45, 10]
    )
edit_button = sg.Button("Edit", key='edit_action')
complete_button = sg.Button("Complete", key='complete_action')
exit_button = sg.Button("Exit", key='exit_action')


layout = [
    [title], 
    [label], 
    [task_input, add_button], 
    [edit_info_label], 
    [task_list_box, edit_button, complete_button],
    [exit_button]]

window = sg.Window("Task Manager App", layout)

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

        case "task_lists":
            
            """
              Extract the exact tasks:
              1. Get the values['task_lists'][0] that would be "1. Buy Books"
              2. Split the above value that would be [1, ' Buy Books']
              3. Get the second value from thr above array and then strip that string
            """
            tasks_to_edit = get_actual_task_text(values['task_lists'][0])
            window["task"].update(value=tasks_to_edit)

        case "edit_action":
            
            try:
                selected_task = get_actual_task_text(values['task_lists'][0]) + '\n'
                edited_task = values['task']

                all_tasks = utilities.get_tasks('tasks.txt')
                editing_index = all_tasks.index(selected_task)

                all_tasks[editing_index] = edited_task + '\n'
                utilities.write_tasks(all_tasks)

                parsed_tasks_list = parse_tasks_list(all_tasks)

                """ update ui """
                window["task"].update(value='')
                window["task_lists"].update(values=parsed_tasks_list)

            except:
                print('Something went wrong, check console!')


        case "complete_action":

              try:
                  selected_task = get_actual_task_text(values['task_lists'][0]) + '\n'
                  all_tasks = utilities.get_tasks('tasks.txt')

                  all_tasks.remove(selected_task)
                  utilities.write_tasks(all_tasks)

                  parsed_tasks_list = parse_tasks_list(all_tasks)

                  """ update ui """
                  window["task"].update(value='')
                  window["task_lists"].update(values=parsed_tasks_list)

              except:
                print('Something went wrong, check console!')

        case "exit_action":
            break
          
        case sg.WIN_CLOSED:
            break

window.close()