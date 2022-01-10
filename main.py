


import random
from play_hangman import *
from binary_search import *
from merge_sort import *





# def dict_of_words():
dict_of_words = {}

# open File and read
file_words = open('C:/Users/moham/Downloads/Learning languages/Python/Learning/Midterm/file_words.txt', 'r')

# append to dictionary
lines = file_words.readlines()
merge_Sort(lines, 0, len(lines)-1 )

for line in lines:
    list = line.strip().split(":")
    dict_of_words[list[0]] = list[1] 



list_words_keys = [*dict_of_words]          # to transform dict keys to a list




#############################

#dictionary of users
dict_of_users = {}

file_names = open('C:/Users/moham/Downloads/Learning languages/Python/Learning/Midterm/file_names.txt', 'r')

name_lines = file_names.readlines()

for line in name_lines:
    list = line.strip().split(":")
    dict_of_users[list[0]] = list[1] 

list_names = [*dict_of_users] 



def save_user_in_dict():
    print ("      Welcome to Hangman   \n")
    user_name = input("Please Enter you name here : ")
    
    if user_name not in dict_of_users.keys():
        dict_of_users[user_name] = 0
        
    score = dict_of_users[user_name]

    return user_name, int(score)


#############################

def list_of_words():
    print("\n Here you can see the list of sorted words in the file : ")
    # global dict_of_words
    if len(dict_of_words) == 0:
        print("There are no data please add new !")
    else:

        for key,value in dict_of_words.items():
            print(key, " : ", value) 
     


############################

def add_to_dictionary():
    global dict_of_words
    global list_words_keys 

    print("\n Hint :  Here you can add a word and a value like=>   happy : emotion  ")

    user_key = input("Enter the key  : ")
    user_value = input("Enter its value : ")
    

    for key in list_words_keys:                                      # to keep the list sorted 
        if user_key < key:
            list_words_keys.insert(list_words_keys.index(key), user_key)   # the only way to add into specific index
            dict_of_words[user_key] = user_value 
            print("The word is added successfully ! ")
            break                                                    # to stop iterating once found olny item


    dict_of_words = {key:dict_of_words[key] for key in list_words_keys}
    

############################

def search_for_word():

    print("\n Hint :  Here you can the search for the word   ")
    search_word = input("Enter here your word : ")

    global list_words_keys         
    return BinarySearch(list_words_keys, search_word), search_word

############################

def remove_word():
    global list_words_keys
    result, search_word = search_for_word()

    if result:
        dict_of_words.pop(search_word)   
        list_words_keys[result] = list_words_keys.pop() 

        print("\n Your word is deleted successfully  \n")
        
    else:
        print("your word is not found !! Search again \n")
    
   

##########################

def change_hint():
    
    result, search_word = search_for_word()

    if result:
        changed_hint = input("Enter your hint : ")
        dict_of_words[search_word] = changed_hint    
        print("\n  Changed successfully  ")
        
    else:
        print("your word is not found !! Search again ")



##########################

def save_changes():
    print("\n Do you want to save the changes done in the Dictionary ?\n")
    print("(yes) or (no) Enter here : ")

    global dict_of_users
    global list_names

    while True: 
        user_decide = input("").upper()


        if user_decide == "YES" or user_decide == "Y":
            file_words = open('C:/Users/moham/Downloads/Learning languages/Python/Learning/Midterm/file_words.txt', 'w') 
            

            for key in list_words_keys:
                if key == list_words_keys[-1]:
                    file_words.write( f"{key}:{dict_of_words[key]}" )
                else:
                    file_words.write( f"{key}:{dict_of_words[key]}\n" )
            file_words.close()

            file_names = open('C:/Users/moham/Downloads/Learning languages/Python/Learning/Midterm/file_names.txt', 'w') 
            for key in list_names:
                if key == list_names[-1]:
                    file_names.write( f"{key}:{dict_of_users[key]}" )
                else:
                    file_names.write( f"{key}:{dict_of_users[key]}\n" )
            file_names.close()

            print("\n Saved successfully .")
            break


        elif  user_decide == "No" or user_decide == "N":
            print("\n Discard changes  .")
            break


        else: 
            print("(yes) or (no) Enter here : ")




#########################

# Start of the program 

def main():

   
    global dict_of_words
    global list_words_keys
    
    user_name,score = save_user_in_dict()

    print(f"\n Hi  {user_name}       \n")
   
   
    while True:
        print(f"\n \n  Your Total Score  =   {score}     \n")

        print("\n \n Hint: Please enter the number next to each option ")
        print("\n (1) Play Hangman \n", "(2) List Words in Dictionary \n", "(3) Add Word to Dictionary \n", "(4) Remove Word from Dictionary \n", "(5) Change Word Hint \n", "(6) Exit")

        selected_option = input("\n enter your nb : ")
     
        if selected_option == "1":
             
            word = random.choice( list_words_keys)
            score = score +  play_hangman(word, dict_of_words[word] ) 
            dict_of_users[user_name] = score
            

        elif  selected_option == "2":
            list_of_words()
           
        elif selected_option == "3":
            add_to_dictionary()
           

        elif selected_option == "4":
            remove_word()

        elif selected_option == "5":
            change_hint()

        elif selected_option == "6":
            save_changes()
            break

        else:
            print("invalid chars !\n Please enter a num btw 1 and 6 ")





main()




# references:
 
# code snippet for play_hangman()  from youtube video at 24 min  https://www.youtube.com/watch?v=8ext9G7xspg&t=5685s 

# reading from a file     https://fedingo.com/python-reading-writing-to-same-file/

# code snippet to split the spaces   https://quick-adviser.com/how-do-you-convert-a-text-file-to-a-dictionary-in-python/

# code snippet for deleting from dictionary    https://www.askpython.com/python/dictionary/delete-a-dictionary-in-python
#                                               https://favtutor.com/blogs/python-sort-dictionary