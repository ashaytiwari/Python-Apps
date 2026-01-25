while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.strip():
        
        case "add":
            todo = input("Enter Task: ") + '\n' # \n for new line escape character

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()

            tasks.append(todo)

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

        case "show":
            
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
                
            # list comprehension: to modify the list of items
            # newTasks = [item.strip('\n') for item in tasks]

            for index, item in enumerate(tasks):
                # more direct way to remove \n from item rather than above
                item = item.title().strip('\n')

                print(f"{index + 1}. {item}") 

        case "edit":
            
            stringifiedNumber = input("Number of the task to edit: ")
            number = int(stringifiedNumber)

            newTask = input("Enter new task: ") + '\n' # \n for new line escape character

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()

            tasks[number - 1] = newTask

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

            print("Task Updated!")

        case "complete":
            stringifiedNumber = input("Number of the task to mark as complete: ")
            number = int(stringifiedNumber)

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()

            completedTask = tasks.pop(number - 1)

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

            print(f"Task marked as completed: {completedTask.strip('\n')}")

        case "exit":
            break
        
        case _:
            print('Hey you have entered an unknown command')
        
print('Bye, see you soon!')