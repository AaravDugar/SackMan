def main():
    print("Calculator")
    print("Type exit to quit")

    while True:
        expr = input("calc> ")

        if expr.lower() == "exit":
            break

        try:
            print(eval(expr))
        except:
            print("Invalid expression")
