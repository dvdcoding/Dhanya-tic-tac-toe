##Tic-Tac_Toe


import random
new = ['','','','','','','','','']
man = ''
machine = ''
null = ''

#team assignement
def sign(man, machine):
    man = raw_input("What team do you want to play for? X or O ")
    while man not in ('x','X','o','O'):
        print "Invalid Choice!"
        man = raw_input("What team do you want to play for? X or O ")
    if man == 'x' or man == 'X':
        print "Ok, X is yours!"
        machine = 'o'
    else:
        print "Ok, O is yours!"
        machine = 'x'
    return man.upper(), machine.upper()
    
    
# decding who gets to go first
def decide_turn():
    turn = None
    while turn not in ('y','Y','n','N'):
        turn = raw_input("Would you like to go first? type y (yes) or n (no)")
        if turn == 'y' or turn == 'Y':
            return 1
        elif turn == 'n' or turn == 'N':
            return 0
        else:
            print "its an invalid choice."

#drawing the grid
def draw(a):
    
    print "\n\t",a[0],"|",a[1],"|",a[2]
    print "\t", "--------"
    print "\n\t",a[3],"|",a[4],"|",a[5]
    print "\t", "--------"
    print "\n\t",a[6],"|",a[7],"|",a[8], "\n"

# text for when someone wins
def congo_man():
    print "Congrats! You won!!"

def congo_machine():
    print "Wohoo! I won!!!"

# If the player goes first
def man_first(man, machine, new):
    while winn(man, machine, new) is None:
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
        if winn(man, machine, new) != None:
            break
        else:
            pass
        print "ummmm....i'll take.."
        p_move = machine_move(man, machine, new)
        print p_move
        new[int(p_move)] = machine
        draw(new)
    q = winn(man, machine, new)
    if q == 1:
        congo_man()
    elif q == 0:
        congo_machine()
    else:
        print "Awe man! Its a tie."
   

# if the computer goes first
def machine_first(man, machine, new):
    while not winn(man, machine, new):
        print "i'll take..."
        p_move = machine_move(man, machine, new)
        print p_move
        new[p_move] = machine
        draw(new)
        if winn(man, machine, new) != None:
            break
        else:
            pass
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
    q = winn(man, machine, new)
    if q == 1:
        congo_man()
    elif q == 0:
        congo_machine()
    else:
        print "Awe man! Its a tie."

# strategies to win and text for a tie
def winn(man, machine, new):
    ways = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in ways:
        if new[i[0]] == new[i[1]] == new[i[2]] != null:
            winner = new[i[0]]
            if winner == man:
                return 1
            elif winner == machine:
                return 0
            if null not in new: 
                return 'TIE'
    if null not in new: 
        return 'TIE'    
    return None

# when player moves 
def man_move(man, new): 
    a = raw_input("Where you want to move? ")
    while True:
        if a not in ('0','1','2','3','4','5','6','7','8'):
            print "Sorry, you can't move there."
            a = raw_input("Where you want to move? ")
        elif new[int(a)] != null:
            print "Sorry, that place is already taken"
            a = raw_input("Where do you want to move? ")
        else:
            return int(a)



# when the computer makes a move  
def machine_move(man, machine, new):
    best = [4, 0, 2, 6, 8]
    blank = []
    for i in range(0,9):
        if new[i] == null:
            blank.append(i)
    
    for i in blank:
        new[i] = machine
        if winn(man, machine, new) is 0:

            return i
        new[i] = null

    for i in blank:
        new[i] = man
        if winn(man, machine, new) is 1:

            return i
        new[i] = null

    return int(blank[random.randrange(len(blank))])

#instruction to play
def display_instruction():
      """ Displays Game Instuructions. """
      print 
      """
      Welcome to the Game...
      You will make your move known by entering a number, 0 - 8.
      The will correspond to the board position as illustrated:


                          0 | 1 | 2            
                         -----------
                          3 | 4 | 5            
                         -----------
                          6 | 7 | 8

                          
      Prepare yourself, the ultimate bettel is about to begin.....
      """

# main begining text  
def main(man, machine, new):
    display_instruction()
    print "Welcome to tic tac toe! You will be playing against me!"
    a = sign(man, machine)
    man = a[0]
    machine = a[1]
    b = decide_turn()
    if b == 1:
        print "Ok, you are first!"
        print "Lets get started, here's a new board!"
        draw(new)
        man_first(man, machine, new)
    elif b == 0:
        print "Ok, I'll go first."
        print "Let the games begin!"
        draw(new)
        machine_first(man, machine, new)
    else:
        pass

#exiting the game
main(man, machine, new)
raw_input("Press enter to exit")
exit()
       
      
       
