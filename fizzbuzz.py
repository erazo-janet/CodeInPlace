"""
Prints the Fizz Buzz sequence up to a given number.
In the game Fizz Buzz, players take turns counting up from one. 
If a player’s turn lands on a number that’s divisible by 3, she should say fizz
instead of the number, and if it lands on a number that’s divisible by 5,
she should say buzz instead of the number. 
If the number is both a multiple of 3 and of 5, she should say fizzbuzz instead of the number. 
"""

def main():
    #get input from user
    count = int(input("Number to count to: "))
    fizz = 0
    buzz = 0
    fb = 0

    #display the numbers we are counting and the key words
    for i in range(1,count+1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
            fizz += 1
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
            buzz += 1
        elif i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
            fb += 1
        else: #we only print if these conditions are not met 
            print(i)

    #display summary 
    print("")
    print("Num fizzed: " + str(fizz))
    print("Num buzzed: " + str(buzz))
    print("Num fizzbuzzed: " + str(fb))
 
if __name__ == '__main__':
    main()