
def validPosition(x,y): 
    '''Checks if the position (x,y) is a valid position on the board.'''
    return (0 <= x <= 5) and (0 <= y <= 5)

# These dicts map from strings to direction tuples and vice versa
str2Dir = {"EAST":(1,0), "WEST":(-1,0), "NORTH":(0,1), "SOUTH":(0,-1)} 
dir2Str = {d:s for s,d in str2Dir.items()} 

def main():
    pos,dir,startState = None,None,True   # initial starting state for the robot

    while True:
        print("> ", end='') # print the repl prompt without a newline 
        cmd = input()       # read user input

        if cmd.startswith("PLACE"):
            args = cmd.split("PLACE ")[1].split(",")  # parse the operands for the PLACE command
            x,y = int(args[0]),int(args[1])
            if validPosition(x,y):  # check if we're placing on a valid position 
                pos = x,y
                if len(args) == 3: 
                    dir = str2Dir[args[2]]    # n.b - we only accept a new direction if it was given with a valid position    
                    startState = False  # mark that we have exited the starting state 

        elif startState:  # we have not yet exited the start state:
            continue      # so discard command until we have got a valid PLACE command

        elif cmd == "MOVE": 
            x_,y_ = (pos[0] + dir[0], pos[1] + dir[1])  # compute the potential new position 
            if validPosition(x_,y_):  # if its a valid position - accept it as the new position
                pos = x_,y_ 
        
        elif cmd == "LEFT":
            dir = -dir[1],dir[0]  # rotating a point (a,b) anti-clockwise is (-b,a)

        elif cmd == "RIGHT":
            dir = dir[1],-dir[0] # rotating a point (a,b) clockwise is (b,-a)

        elif cmd =="REPORT":
            print(f'{pos[0]},{pos[1]},{dir2Str[dir]}')

if __name__ == '__main__':
    main()
