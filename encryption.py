# encryption.py
# LUJAINA ELDELEBSHANY, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

def encryption(user_message, user_cipher):
    '''
    Parameters taken are user's message and their valid cipher. Function runs if choice 1 (encryption) is chosen; splits user's message into a list, and
    connects the alphabet list to the cipher list as a new dictionary. Loops over all characters in user message, 
    takes the dictionary value at that key, and appends to new list. New list turned into a string is the encoded
    message. No return value.
    '''
    #add all the letters of the cipher into list 
    list_cipher = [char for char in user_cipher]  
    alphanumeric_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #add list of alphanum chars into keys of dictionary and cipher list to dictionary values
    cipher_dict = {alphanumeric_list[i]: list_cipher[i] for i in range(len(list_cipher))} 
    encoded_list = []
     #loops all chars in string, adds that key's value to empty list and turns into string
    for k in user_message:  
            encoded_list.append(cipher_dict[k])
    encoded_string = ''.join(encoded_list)
    print('Encoded message:', encoded_string)

def decryption(user_message, user_cipher):
    '''
    Parameters taken are user's message and their valid cipher. Function runs if choice 2 (decryption) is chosen; 
    splits user's message into a list, and connects the cipher list to the alphabet list as a new dictionary 
    (linked opposite direction to encryption function). Loops over all characters in user message, takes the 
    dictionary value at that key, and appends to new list. New list turned into a string is the encoded 
    message. No return value.
    '''
    list_cipher = [char for char in user_cipher]  
    alphanumeric_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #links cipher and alphabet the opposite way from encoding function
    cipher_dict = {list_cipher[i]: alphanumeric_list[i] for i in range(len(list_cipher))}
    decoded_list = []
    #loops all chars in string and adds that key's value to a new list  
    for k in user_message: 
            decoded_list.append(cipher_dict[k])
    decoded_string = ''.join(decoded_list)
    print('Decoded message:', decoded_string)

def say_goodbye():
    '''Runs if choice 0 is chosen. Says goodbye to user. Takes no parameters and returns nothing.'''
    print('\n')
    print('Thank you for using the encryption program.')

def main():
    '''
    Main function. Takes no parameters and returns no values. Runs the while loop that controls menu 
    choices, and encryption/decryption method running.
    '''  
    #user_input variables
    user_message = ''
    user_cipher = ''
    user_choice = ''                                                                                         
    print("ENDG 233 Encryption Program")

    while True:
        user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: '))
        if user_choice == 0: #automatically exits recurring loop if user chooses exit
            break
        user_message = input('Please enter the text to be processed: ')
        user_cipher = input('Please enter the cipher text: ')

        while True:
            if (user_cipher.isalnum() == True and len(set(user_cipher)) == 26): # all alphanumeric characters and has 26 unique characters
                print('Your cipher is valid.')
                user_cipher = user_cipher.lower() #convert to lowercase
                break
            if( user_cipher.isalnum() == True and set(user_cipher) != 26): #removing duplicated values 
                user_cipher = str(list(set(user_cipher))) 
                user_cipher = user_cipher.lower() #convert to lowercase
                
            else:
                if(set(user_cipher) != 26 or list(user_cipher) != 26):
                    print('Your cipher is not valid because it is not 26 unique characters long')
                print('Your cipher is not valid because it is not alphanumeric, it must also contain 26 UNIQUE elements of a-z or 0-9')
                user_cipher = input('Please enter a valid cipher text: ') #continue to ask for user's cipher while keeping user_message the same

        #run encryption function
        if user_choice == 1:
            encryption(user_message, user_cipher)

        #run decryption function
        elif user_choice == 2:
            decryption(user_message, user_cipher)
    
    say_goodbye()

#run main function
main()