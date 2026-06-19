def main():

    while True:

        cmd = input("notes> ")

        if cmd == "exit":
            break

        elif cmd.startswith("write "):

            text = cmd[6:]

            with open("notes.txt","a") as f:
                f.write(text + "\n")

        elif cmd == "read":

            try:
                with open("notes.txt","r") as f:
                    print(f.read())

            except:
                print("No notes.")
