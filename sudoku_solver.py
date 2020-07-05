# NOTE : THIS IS A SUDOKU SOLVER FOR RANDOMLY GENERATED SUDOKU. IT GENERATES UNTIL IT FINDS ONE VALID SUDOKU FORM
# AND IT SHOWS THE GENERATED SUDOKU WITH NULL VALUES.

import random
from time import * 

# we CREATE a 9x9 board with null values(zeros) and we insert numbers from 1-9 in random columns
# to generate the potential sudoku array
def create_board():
    brd = [  
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]
    number = 1
    rand_num = random.randint(1,9)
    rand_col = random.randint(0,8)
    #if value of 1st row of array null insert a random number
    if brd[0][rand_col] == 0:
        brd[0][rand_col] = rand_num
        number+=1
    # insert random values in random rows and columns
    while number <= 9 :
        if number != rand_num:
            rand_row = random.randint(0,8)
            rand_col = random.randint(0,8)
            if brd[rand_row][rand_col] == 0:
                brd[rand_row][rand_col] = number
                number+=1
        else:
            number+=1
    return (brd)

# used to CREATE the array of SOLVED array with null values,so that it can be printed in a "sudoku playable form"
def create_play_board(brd,dif):
    def create_blank_spaces(num):
        while num >= 0:
            rand_row = random.randint(0,8)
            rand_col = random.randint(0,8)
            rand_number = random.randint(1,9)
            if brd[rand_row][rand_col] != 0:
                brd[rand_row][rand_col] = 0
                num-=1
    if dif == '1' :
        number= random.randint(40,45)
        create_blank_spaces(number)
    elif dif == '2' :
        number= random.randint(46,54)
        create_blank_spaces(number)
    elif dif == '3' :
        number= random.randint(55,62)
        create_blank_spaces(number)
    return (brd)

# PRINT the array in a "sudoku form"
def print_board(brd):
    for row in range(len(brd)): # range(0,9)
        # seperate the boxes with rows 
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        # seperate the boxes with columns 
        for col in range(len(brd)):
            if col % 3 == 0 and col != 0:
                print(" | ",end="")
            # show array in a 9x9 form
            if col == 8:
                print(brd[row][col]) #its the last number so you change line 
            else:
                print(str(brd[row][col]) + " ", end="") # with end="",you continue on the shame line

# find an empty "square/field" in the array
def find_empty(brd):
    for row in range(len(brd)):
        for col in range(len(brd[0])):
            if brd[row][col] == 0:
                return (row, col)  
    return None

# used to PRINT the SOLVED array in a "sudoku form" with null values 
def print_play_board(brd,dif):
    if dif == '1' :
        #depending on the difficulty we put null values to the boxes,the rand number is the number of the null values of sudoku
        number= random.randint(40,45)
    elif dif == '2' :
        number= random.randint(46,54)
    elif dif == '3' :
        number= random.randint(55,62)
    for row in range(len(brd)): # range(0,9)
        # seperate the boxes with rows 
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        # seperate the boxes with columns 
        for col in range(len(brd)):
            if dif == '1' :
                rand= random.randint(1,4)
            elif dif == '2' :
                rand= random.randint(1,3)
            elif dif == '3' :
                rand= random.randint(1,3)
            
            if col % 3 == 0 and col != 0:
                print(" | ",end="")
            # show array in a 9x9 form
            if col == 8:
                #insret the null values randomly 
                if  number >0 and (rand in (1,2)):
                    print(0)
                    number-=1
                else:
                    print(brd[row][col]) 

            else:
                #insret the null values randomly
                if  number >0 and (rand in (1,2)):
                    print(str(0) + " ", end="") # with end="",you continue on the shame line
                    number-=1
                else:
                    print(str(brd[row][col]) + " ", end="") # with end="",you continue on the shame line

# check the number we inserted in the "square/field" is valid
def valid(brd,num,pos):
    # Check row
    for i in range(len(brd[0])):
        # pos[1] != i is the exact position that we just inserted the number so we want to exclude it
        if brd[pos[0]][i] == num and pos[1] != i: 
            return False
    # Check column
    for i in range(len(brd)):
        # pos[0] != i is the exact position that we just inserted the number so we want to exclude it
        if brd[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True

# solve the array to see if is a sudoku
def solve(brd):
     # we look for am empty field,if there is not then probably the array for the sudoku is completed and there is a solution
    if find_empty(brd) == None:
        return True
    else:
        row,col = find_empty(brd)
        t1_start = process_time() # Start the stopwatch / counter 
        for i in range(1,10):
            if valid(brd, i, (row, col)):
                brd[row][col] = i
                t1_stop = process_time() # Stop the stopwatch / counter 
                if t1_stop-t1_start > 0.5 : 
                    return False
                if solve(brd):
                    return True
                brd[row][col] = 0
    return False



