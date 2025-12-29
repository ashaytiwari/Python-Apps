import utilities

while True:
    user_action = input("Type add, add-many, show, edit, complete or exit: ")

    if user_action.startswith("add"):
        
        """ line slicing """
        todo = user_action[4:] 

        """ if user didn't provided any task input with add command, ask them to enter tasks """
        if todo == '':
            todo = input("Enter Task: ")

        tasks = utilities.get_tasks('tasks.txt')

        tasks.append(todo + '\n')

        utilities.write_tasks(filepath='tasks.txt', data=tasks)

    elif user_action == 'show':
            
        tasks = utilities.get_tasks('tasks.txt')
            
        """ list comprehension: to modify the list of items """
        # newTasks = [item.strip('\n') for item in tasks]

        for index, item in enumerate(tasks):
            """" more direct way to remove \n from item rather than above """
            item = item.title().strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action == "edit":
            
        try:
            stringifiedNumber = input("Number of the task to edit: ")
            number = int(stringifiedNumber)

            newTask = input("Enter new task: ") + '\n' # \n for new line escape character

            tasks = utilities.get_tasks('tasks.txt')

            tasks[number - 1] = newTask

            utilities.write_tasks(filepath='tasks.txt', data=tasks)

            print("Task Updated!")

        except ValueError:
            print('Invalid Value!')
            continue

    elif user_action == "complete":
        
        try:
            stringifiedNumber = input("Number of the task to mark as complete: ")
            number = int(stringifiedNumber)

            tasks = utilities.get_tasks('tasks.txt')

            completedTask = tasks.pop(number - 1)

            utilities.write_tasks(filepath='tasks.txt', data=tasks)

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