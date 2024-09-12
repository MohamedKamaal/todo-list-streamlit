import streamlit as st 
from functions import get_tasks, write_tasks
st.title('To-do list')
st.subheader('manage your tasks easily')
st.write('improve your productivity')
def add_task():
    new_todo = st.session_state['new_task'] +"\n"
    tasks = get_tasks()
    tasks.append(new_todo)
    write_tasks(tasks)
    return True



tasks = get_tasks()
for index,task in enumerate(tasks):
    checkbox = st.checkbox(task,key=task)
    if checkbox:
        tasks.pop(index)
        write_tasks(tasks)
        del st.session_state[task]
        st.rerun()
    
st.text_input(label='aa',placeholder='add new task',on_change =add_task,key='new_task')
st.session_state