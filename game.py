def instruction():
    print("These are the places where you place your character")
    print(" 1 | 2 | 3\n"
          "___ ___ ___\n"
          " 4 | 5 | 6\n"
          "___ ___ ___\n"
          " 7 | 8 | 9\n")

v = ['','','','','','','','','']

def board():
    print(" %s | %s | %s\n"
          "___ ___ ___\n"
          " %s | %s | %s\n"
          "___ ___ ___\n"
          " %s | %s | %s\n" % (v[0], v[1], v[2], v[3], v[4], v[5], v[6],v[7],v[8]))

def userinput(char):
    u = int(input("where you want to insert the  %s"%(char)))
    if u<=0 or u>9:
        print("you are out of the box")
        return False
    if v[u-1] == "x" or v[u-1] == "0":
        print("place already have a character")
    return u


def main():
    for i in range(9):
        if i%2 == 0:
            character = "x"
        else:
            character = "0"
        instruction()
        board()
        user = userinput(character)
        while user == False:
            user = userinput(character)
        user = user-1
        v[user] = character

main()


# function call
# instruction()