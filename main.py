tasks = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action:
        
        case "add":
            todo = input("Enter Task: ")
            tasks.append(todo)

        case "show":
            print(tasks)

        case "exit":
            break