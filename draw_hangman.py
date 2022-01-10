


def print_for_8():
        for i in range(14):
            if i < 3:
                print(" ",end="")
            elif i < 6:
                print("_",end="")
            elif i < 7:
                print(" ",end="")
                print("")
            elif i < 8:
                print("  ",end="")       
            elif i < 9:
                print("|",end="")  
            elif i < 12:
                print("_",end="")
            elif i < 13:
                print("|",end="")



def print_for_6():
    for i in range(7*2):
            if i < 4:
                print(" ",end="")
            elif i == 4:
                print("|", end="")
                print("")
            elif i < 9:
                print(" ",end="")
            elif i == 9:
                print("|")




def print_for_4():
    print_for_8()
    print("")

    for i in range(7*2):
        if i < 2 :
            print(" ",end="")
        elif i == 2 :
            print("\\",end="")
        elif i == 4:
            print("|", end="")
        elif i == 5:
            print(" ",end="")
        elif i == 6:
            print("/",end="")
            print("")
        elif i < 11:
            print(" ",end="")
        elif i == 11:
            print("|")

###############################




def draw_hangman(lives):

    if lives == 7:
        print_for_8()

        print("")
        print_for_6()

    elif lives == 6:
        print_for_8()
        print("")

        for i in range(7*2):
            if i < 4 :
                print(" ",end="")
            elif i == 4:
                print("|", end="")
            elif i == 5:
                print(" ",end="")
            elif i == 6:
                print("/",end="")
                print("")
            elif i < 11:
                print(" ",end="")
            elif i == 11:
                print("|")
            

    elif lives == 5:
        print_for_4()

    elif lives == 4:
        print_for_4()

        for i in range(7*2):
            if i < 5 :
                print(" ",end="")
            elif i == 5:
                print("\\", end="")
                print("")
            elif i < 12:
                print(" ",end="")
            elif i == 12:
                print("\\",end="")
      

    elif lives == 3:
        print_for_4()

        for i in range(7*2):
            if i < 3 :
                print(" ",end="")
            elif i == 3 :
                print("/",end="")
            elif i < 5:
                print(" ",end="")
            elif i == 5:
                print("\\", end="")
                print("")
            elif i < 12:
                print(" ",end="")
            elif i == 12:
                print("\\",end="")
               


    elif lives == 2:
        print_for_4()

        for i in range(7*2):
            if i < 3 :
                print(" ",end="")
            elif i == 3 :
                print("/",end="")
            elif i < 5:
                print(" ",end="")
            elif i == 5:
                print("\\", end="")
                print("")
            elif i == 8:
                print("/", end="")
               
            elif i < 12:
                print(" ",end="")
            elif i == 12:
                print("\\",end="")


    elif lives == 1:
        print_for_4()

        for i in range(7*2):
            if i < 3 :
                print(" ",end="")
            elif i == 3 :
                print("/",end="")
            elif i < 5:
                print(" ",end="")
            elif i == 5:
                print("\\", end="")
                print("")
            elif i == 8:
                print("/", end="")
            elif i < 12:
                print(" ",end="")
            elif i == 12:
                print("\\",end="")
            elif i == 13:
                print("/",end="")

   
    elif lives == 0:
        print_for_4()

        for i in range(7*2):
            if i < 3 :
                print(" ",end="")
            elif i == 3 :
                print("/",end="")
            elif i < 5:
                print(" ",end="")
            elif i == 5:
                print("\\", end="")
                print("")
            elif i == 7:
                print("\\", end="")    
            elif i == 8:
                print("/", end="")
            elif i < 12:
                print(" ",end="")
            elif i == 12:
                print("\\",end="")
            elif i == 13:
                print("/",end="")
        



# print (  draw_hangman(8) )