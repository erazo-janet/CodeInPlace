import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def main():
    #first milestone, load all of the words from a file into a list
    with open(FILE_NAME) as file:
        words = [] #declaring an empty list
        for line in file:
            line = line.strip()
            words.append(line)
            #print(words)

    #second milestone, you can use this way or use the index game method
    #we need to repeat this
    while True:
        chosen_value = random.choice(words) # comes with ‘import random’
        print(chosen_value)
    #third milestone. wait for the user to hit enter. but we dont need to store anything from the user
        input() #we can just do this
    


if __name__ == '__main__':
    main()