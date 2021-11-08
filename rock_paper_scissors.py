"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition 
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3

def main():
    print_welcome()
    
    total_score = 0

    for i in range(N_GAMES):
        ai_move = get_ai_move() #get ai move
        human_move = get_human_move() #get human move
        winner = get_winner(ai_move, human_move) #get winner
        total_score = update_score(winner, total_score) #based on whose the winner, update toal score
        print("ai move was ", ai_move)
        print("winner was ",winner)
        print('') #empty line between moves
    print('total score', total_score)

def update_score(winner, total_score):
    if winner == 'ai':
        total_score -=1
    if winner == 'human':
        total_score +=1
    if winner == 'tie':
        total_score +=0
    #now the total_Score variable in main will be updated based on our conditions
    return total_score

def get_ai_move():
    #you can have the ai choose something random, choose strategies 
    ai_move = random.randint(1, 3)
    if ai_move == 1:
        return 'rock'
    if ai_move == 2:
        return 'paper'
    return 'scissors'

def get_human_move():
    while True:
        human_move = input("Enter your move: ")
        if is_valid_move(human_move):
            return human_move
        print("Invalid move")

def is_valid_move(move):
    """
    parameter move: stirng representing what the user entered
    return:boolean which is true if the move was valid
    ad doc test 
    >>> is_valid_move('rock')
    True
    >>> is_valid_move('unicorn')
    False
    """
    if move == 'rock':
        return True
    if move == 'paper':
        return True
    if move == 'scissors':
        return True
    return False #we will get falase if these moves arent correct

def get_winner(ai_move,human_move):
    """
    return 'ai' #return ai, human or tie 
    >>> get_winner('rock,'scissors')
    'ai'
    >>>get_winner('scissors','rock')
    'human'
    >>>Get_winner('rock','rock')
    'tie'
    """
    if ai_move == human_move:
        return 'tie'
    if ai_move == 'rock':
        if human_move == 'scissors':
            return 'ai'
        return 'human'
    if ai_move == 'paper':
        if human_move == 'rock':
            return 'ai'
        return 'human'
    if ai_move == 'scissors':
        if human_move == 'paper':
            return 'ai'
        return 'human'
    print('you should not get here.....')


def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()