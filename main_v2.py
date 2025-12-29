def get_tasks(filepath):
    
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()

    return tasks_local


def write_tasks(filepath, data):
    
    with open(filepath, 'w') as file_local:
        file_local.writelines(data)

while True:
    user_action = input("Type add, add-many, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        
        todo = user_action[4:] # line slicing

        # if user didn't provided any task input with add command, ask them to enter tasks
        if todo == '':
            todo = input("Enter Task: ")

        tasks = get_tasks('tasks.txt')

        tasks.append(todo + '\n')

        write_tasks('tasks.txt', tasks)

    elif user_action == 'show':
            
        tasks = get_tasks('tasks.txt')
            
        # list comprehension: to modify the list of items
        # newTasks = [item.strip('\n') for item in tasks]

        for index, item in enumerate(tasks):
            # more direct way to remove \n from item rather than above
            item = item.title().strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action == "edit":
            
        try:
            stringifiedNumber = input("Number of the task to edit: ")
            number = int(stringifiedNumber)

            newTask = input("Enter new task: ") + '\n' # \n for new line escape character

            tasks = get_tasks('tasks.txt')

            tasks[number - 1] = newTask

            write_tasks('tasks.txt', tasks)

            print("Task Updated!")

        except ValueError:
            print('Invalid Value!')
            continue

    elif user_action == "complete":
        
        try:
            stringifiedNumber = input("Number of the task to mark as complete: ")
            number = int(stringifiedNumber)

            tasks = get_tasks('tasks.txt')

            completedTask = tasks.pop(number - 1)

            write_tasks('tasks.txt', tasks)

            print(f"Task marked as completed: {completedTask.strip('\n')}")

        except IndexError:
            print("Task with this index doesn't exists!")
            continue
        except ValueError:
            print('Invalid Value!')
            continue

    elif user_action == "exit":
        print('Bye, See you soon!')
        break
        
    else:
        print('Hey you have entered an unknown command')