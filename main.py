while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    match user_action.strip():
        
        case "add":
            todo = input("Enter Task: ") + '\n' # \n for new line escape character

            file = open('tasks.txt', 'r')
            tasks = file.readlines()
            file.close()

            tasks.append(todo)

            file = open('tasks.txt', 'w')
            file.writelines(tasks)
            file.close()

        case "show":
            
            file = open('tasks.txt', 'r')
            tasks = file.readlines()
            file.close()

            # list comprehension: to modify the list of items
            # newTasks = [item.strip('\n') for item in tasks]

            for index, item in enumerate(tasks):
                # more direct way to remove \n from item rather than above
                item = item.title().strip('\n')

                print(f"{index + 1}. {item}") 

        case "edit":
            stringifiedNumber = input("Number of the task to edit: ")
            number = int(stringifiedNumber)
            newTask = input("Enter new task: ")
            tasks[number - 1] = newTask
            print("Task Updated!")

        case "complete":
            stringifiedNumber = input("Number of the task to mark as complete: ")
            number = int(stringifiedNumber)
            completedTask = tasks.pop(number - 1)
            print(f"Task marked as completed: {completedTask}")

        case "exit":
            break
        
        case _:
            print('Hey you have entered an unknown command')
        
print('Bye, see you soon!')