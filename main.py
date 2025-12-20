tasks = []

while True:
    user_action = input("Type add, show, edit or exit: ")

    match user_action.strip():
        
        case "add":
            todo = input("Enter Task: ")
            tasks.append(todo)

        case "show":
            number = 1
            for item in tasks:
                print(f"{number}. {item.title()}")
                number = number + 1

        case "edit":
            stringifiedNumber = input("Number of the task to edit: ")
            number = int(stringifiedNumber)
            newTask = input("Enter new task: ")
            tasks[number - 1] = newTask
            print("Task Updated!")

        case "exit":
            break
        
        case _:
            print('Hey you have entered an unknown command')
        
print('Bye, see you soon!')