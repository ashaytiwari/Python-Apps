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