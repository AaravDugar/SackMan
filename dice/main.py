import random

def main():

    while True:

        cmd = input("Press enter to roll or exit: ")

        if cmd == "exit":
            break

        print(random.randint(1,6))
