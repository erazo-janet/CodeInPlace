"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    val = 1
    running_total = 0

    while val !=0:
        val = int(input("Enter a value: "))
        running_total = running_total+val
        print("Running total is ", running_total)
        print("")

if __name__ == '__main__':
    main()