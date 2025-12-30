FILEPATH = "tasks.txt"

""" Read tasks from the text file. """
def get_tasks(filepath=FILEPATH):
    
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()

    return tasks_local


"""" Write Tasks in the text file. """
def write_tasks(data, filepath=FILEPATH):
    
    with open(filepath, 'w') as file_local:
        file_local.writelines(data)