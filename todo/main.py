todos = []

def main():

    while True:

        cmd = input("todo> ")

        if cmd == "exit":
            break

        elif cmd.startswith("add "):

            todos.append(cmd[4:])

        elif cmd == "list":

            for i, task in enumerate(todos,1):

                print(i, task)
