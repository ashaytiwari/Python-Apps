def get_tasks():
    
    with open('tasks.txt', 'r') as file_local:
        tasks_local = file_local.readlines()

    return tasks_local


while True:
    user_action = input("Type add, add-many, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        
        todo = user_action[4:] # line slicing

        # if user didn't provided any task input with add command, ask them to enter tasks
        if todo == '':
            todo = input("Enter Task: ")

        tasks = get_tasks()

        tasks.append(todo + '\n')

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

    elif user_action == 'show':
            
        tasks = get_tasks()
            
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

            tasks = get_tasks()

            tasks[number - 1] = newTask

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

            print("Task Updated!")

        except ValueError:
            print('Invalid Value!')
            continue

    elif user_action == "complete":
        
        try:
            stringifiedNumber = input("Number of the task to mark as complete: ")
            number = int(stringifiedNumber)

            tasks = get_tasks()

            completedTask = tasks.pop(number - 1)

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

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