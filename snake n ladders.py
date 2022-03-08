import random

global player_dict
global snakes
global laders
snakes = {}
laders = {}
n_snakes=int(input("Add no.of snakes : "))

for i in range(0,n_snakes):
    head = int(input("Enter head of the snake : "))
    tail = int(input("Enter tail of the snake :"))
    snakes[head]=tail
n_laders=int(input("Add no.of laders : "))
for i in range(0,n_laders):
    base = int(input("Enter base of the lader : "))
    top = int(input("Enter top of the lader : "))
    laders[base]=top
               
player_dict ={}



def board(): 
    board_numbers=range(1,101)
    board_num=[]
    board_numbers = list((board_numbers[i:i+10] for i in range(0,len(board_numbers), 10)))
    board_numbers.reverse()
    for i in range(0,len(board_numbers)):
        board_numbers[i]=list(board_numbers[i])
        if i%2==0:
            board_numbers[i].reverse()
        board_num.append(board_numbers[i])
    #print(board_num)
    return board_num



def start_player(player_name):
    brd=board()
    for i in range(0,len(brd)):
        try:
            start_pos =[i, brd[i].index(1)]
        except :
            pass
    return start_pos


def start_game():

    brd=board()
    print(brd)
    Num_players=int(input("No.of Players : "))
    i=0
    while i < Num_players:
        player=(input("Enter Player name : "))
        if player in player_dict.keys():
            print("Player already exists : ")
        else:
            player_dict[player]=start_player(player)
            i=i+1    

def player_pos():
    brd=board()
    if player_dict.keys() == None :
        print("No players")
    else:
        for i in player_dict:
            print(i , " --> " , brd[player_dict[i][0]][player_dict[i][1]])
        print()

def disp_board():
    brd=board()
    temp_plist=player_dict.copy()
    flipped = {}
    for i in brd:
        i = str(i)
    for i in temp_plist.keys():
        temp_plist[i]=tuple(temp_plist[i])
    for key, value in temp_plist.items():
        if value not in flipped:
           flipped[value] = [key]
        else:
            flipped[value].append(key)
    if temp_plist.keys() == None:
        for i in brd:
            for j in i :
                print(j ,end=' ')
            print("\n")
    else:
        same_pos=[]
            
        for i in flipped.keys():
            brd[i[0]][i[1]] = flipped[i]
        for i in brd:
            for j in i :
                print(j ,end=' ')
            print("\n")
        

def role_dice():
    brd=board()
    print("Rolling dice for all players..")
    for i in player_dict.keys():
        dice_val = random.randint(1,6)
        print(dice_val)
        position = brd[player_dict[i][0]][player_dict[i][1]] + dice_val
        if position > 100 or position ==100 :
            print("Game won by ",i)
            exit()
        for ii in laders.keys():
            if position==int(ii):
                postion=laders[ii]
        for ii in snakes.keys():
            if position==int(ii):
                postion=snakes[ii]
        for indx in range(0,len(brd)):
            try:
                current_pos =[indx, brd[indx].index(position)]
                print(current_pos)
                player_dict[i]= current_pos
            except Exception as e:
##                print(e)
                pass
     
        
def main() :
    start_game()
    q=1
    while q != 0:
        print("\n")
        print(" Enter 1 to role dice")
        print(" Enter 2 to display positions")
        print(" Enter 3 to display board")
        print(" Enter 0 to Quit")
        q=int(input("Enter choice : "))
        print("\n")
        if q ==1 :
            role_dice()
        elif q==2 :
            player_pos()
        elif q==3 :
            disp_board()
    
main()
