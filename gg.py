import os

def load_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            return