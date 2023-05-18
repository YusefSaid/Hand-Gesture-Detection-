import os

def interface(output):
    file_name = f"{os.getcwd()}/gesture.txt"
    with open(file_name, 'w') as file:
        file.write(output)
