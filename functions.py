FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):  # default-argument -> argument with specified value
    """ method for returning a list with the contents of the file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ method for overwriting the file with the new content in the list """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
