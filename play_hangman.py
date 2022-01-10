

from draw_hangman import * 



###################################

def easy_hard(key, used_letters, word_condition_letters):

    print(" What Level do you want ? \n ")
    print(" (1) Easy ", " (2) Hard \n")


    while True:
        user_level = input("Enter here ur number : ")

        if user_level == "1":
            for i in range(  round(0.2 * len(key)) ):
                used_letters += f"{key[i].upper()}"
                word_condition_letters = word_condition_letters.replace(key[i].upper(), "")
            break    

        elif user_level == "2":
            used_letters = ""
            break

        else:
            print("enter only 1 or 2") 
            
    return used_letters, word_condition_letters

####################################




def play_hangman(key, hint):

    word = key.upper()
    word_condition_letters = word           # the condition to find the word even if there exist the same letter 
    used_letters = ""

    print("\n")
    
    used_letters, word_condition_letters = easy_hard(key, used_letters, word_condition_letters)
                        
    lives = 8
    
    

    while  len(word_condition_letters) > 0 and lives > 0:
        # when enter a letter
        if (len(used_letters) > 0):
            print("\n You have ",lives," lives left, and used these letters : ", (" ").join(used_letters))
            draw_hangman(lives)


        # what current word is (ie  W-R-D--)
        word_list = []
        for letter in word:
            if letter in used_letters:             
                word_list.append(letter)
            else:
                word_list.append("-")
        print("the word is ", " ".join(word_list), "        >>  hint : ", hint)


        # guess a letter
        user_guess = input("Take your guess : ").upper()

        
       # check the use input if it is in used_letters then if it is in word
       
        if  user_guess not in used_letters and len(user_guess) == 1:
            used_letters += user_guess
            
            if user_guess in word_condition_letters:
                word_condition_letters = word_condition_letters.replace(user_guess, "")

                
            else:
                print("Wrong, Letter is incorrect ! ") 
                lives -=1           
        
        elif user_guess in used_letters:
            print("you have already used that character. try again")
            lives -=1

        else: 
            print("invalid characters  !")
    
    if lives == 0:
        print("\n You died, the word is ", word,"\n")
        draw_hangman(lives)
        score =  (100 - round(len(word_condition_letters )/len(word) * 100 ))
        print(" you get = ",score," points \n")

    elif len(word_condition_letters) == 0:
        print("\n Congrats, you won the game 😎" , "the word is ", word)
        score = 100
        print(" you get = ", score," points \n")

    return score



# a =play_hangman("wolffffffffffff", "animal")
# print(a)
# a = "abcdef"
# index = a.find("c")
# print(index)
# b =  a[:index+1] + "0" + a[index+1:]
# print (  b  )

