import time

def main():

    sec = int(input("Seconds: "))

    while sec > 0:

        print(sec)

        time.sleep(1)

        sec -= 1

    print("Time up!")
