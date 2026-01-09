import zipfile
import pathlib
import time

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


""" Create Zip Archive """
def make_zip_archive(filepaths, destination_folder):
    
    destination_path = pathlib.Path(destination_folder, f"compressed-{time.time()}.zip")

    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath_local = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath_local.name)
