while True:
    user_action = input("Type add, add-many, show, edit, complete or exit: ")

    if 'add' in user_action:
        
        todo = user_action[4:] # line slicing

        # if user didn't provided any task input with add command, ask them to enter tasks
        if todo == '':
            todo = input("Enter Task: ")

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        tasks.append(todo + '\n')

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

    elif user_action == 'show':
            
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            
        # list comprehension: to modify the list of items
        # newTasks = [item.strip('\n') for item in tasks]

        for index, item in enumerate(tasks):
            # more direct way to remove \n from item rather than above
            item = item.title().strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action == "edit":
            
        stringifiedNumber = input("Number of the task to edit: ")
        number = int(stringifiedNumber)

        newTask = input("Enter new task: ") + '\n' # \n for new line escape character

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        tasks[number - 1] = newTask

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

        print("Task Updated!")

    elif user_action == "complete":
        
        stringifiedNumber = input("Number of the task to mark as complete: ")
        number = int(stringifiedNumber)

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        completedTask = tasks.pop(number - 1)

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

        print(f"Task marked as completed: {completedTask.strip('\n')}")

    elif user_action == "exit":
        print('Bye, See you soon!')
        break
        
    else:
        print('Hey you have entered an unknown command')