def get_tasks(filepath='tasks.txt'):
    with open(filepath,'r') as file:
        return file.readlines()
    
def write_tasks(tasks,filepath='tasks.txt'):
    with open(filepath,'w') as file:
             file.writelines(tasks)
    return True