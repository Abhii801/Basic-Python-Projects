import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = isexist(user)
    if not computer:
        return  'Please Enter the letter correctly'
    

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    check = is_win(user,computer)

    if check:
        return 'You won!'

    if(user!=computer and not check and computer):
         return 'You lost!'

def is_win(player, opponent):
    # return true if player wins and false if looses
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    return False

def isexist(chance):
    #check for correct letter entered by user or not 
    #returns value if correct else returns false
    tup = ('r','p','s')
    if(chance in tup):
        comp = random.choice(['r', 'p', 's'])
        return comp
    return False
        

flag = True
print(play())
while(flag):
    #to check for recurring game play
    repeat = input("Enter 'c' to continue or 'e' to exit: ").lower()
    if(repeat=='c'):
        print(play())
    elif(repeat=='e'):
        flag = False
    else:
        print("-------Enter the choice correctly-------")