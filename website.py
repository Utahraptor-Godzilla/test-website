import streamlit as st
from signup import created_password
file = created_password()
def get_todos(filepath=file):
    """Reads a text file and returns a list of all the to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_arg, file_path=file):
    """Writes a list of to-do items in the text file."""
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)
todos = get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    write_todos(todos)
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index} {todo}")
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[f"{index} {todo}"]
        st.experimental_rerun()
if "new_todo" not in st.session_state:
    st.session_state.new_todo = ""
st.text_input(label="Enter a todo:", placeholder="Add a new todo", on_change=add_todo, key="new_todo", value="")