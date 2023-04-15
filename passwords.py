"""
Maksim Popov
"""

#menu for user to choose from
MENU = """
Bytewerks Password Manager
--------------------------
[1] - Add new password 
[2] - Retrieve password 
[3] - Update password
[4] - Display stored accounts
[5] - Quit
"""

print(MENU)

#empty dictionary that will store username/password combos that are related to an account key
passwords = {}

#dictionary used to encrypt 
encryption = {
    "A" : "1",
    "a" : "2",
    "B" : "3",
    "b" : "4",
    "C" : "5",
    "c" : "6",
    "D" : "7",
    "d" : "8",
    "E" : "9",
    "e" : "0",
    "F" : "!",
    "f" : "@",
    "G" : "#",
    "g" : "$",
    "H" : "%",
    "h" : "^",
    "I" : "&",
    "i" : "*",
    "J" : "(",
    "j" : ")",
    "K" : "A",
    "k" : "B",
    "L" : "C",
    "l" : "D",
    "M" : "E",
    "m" : "F",
    "N" : "G",
    "n" : "H",
    "O" : "I",
    "o" : "J",
    "P" : "K",
    "p" : "L",
    "Q" : "M",
    "q" : "N",
    "R" : "O",
    "r" : "P",
    "S" : "Q",
    "s" : "R",
    "T" : "S",
    "t" : "T",
    "U" : "U",
    "u" : "V",
    "V" : "W",
    "v" : "X",
    "W" : "Y",
    "w" : "Z",
    "X" : "a",
    "x" : "b",
    "Y" : "c",
    "y" : "d",
    "Z" : "e",
    "z" : "f",
    "1" : "g",
    "2" : "h",
    "3" : "i",
    "4" : "j",
    "5" : "k",
    "6" : "l",
    "7" : "m",
    "8" : "n",
    "9" : "o",
    "0" : "p",
    "!" : "q",
    "@" : "r",
    "#" : "s",
    "$" : "t",
    "%" : "u",
    "^" : "v",
    "&" : "w",
    "*" : "x",
    "(" : "y",
    ")" : "z",
}

#dictionary used to decrypt 
decryption = {}

#populate decryption dictionary 
for x, y in encryption.items():
    decryption[y] = x

while True:
    start = input("Select a menu option: ") #selects what we are doing 

    if start == "1": #add password 
        while start != "n": #allow user to continue adding passwords until quit
            account = input("Enter account: ") #will serve as key from which to retrieve
            username = input("Enter username: ") #will serve as first value in key
            password = input("Enter password: ") #serve as second value in key 

            password_letters = [] #split password into list 

            for i in password:
                password_letters.append(i) #populate list we created above

            scrambled_pass = [] #create empty list for encypted password

            for letter in password_letters: #loop through each letter in password letter list 
                if letter in encryption.keys(): #if that letter is in our dictionary 
                    scrambled_letter = encryption[letter] #encypted letter is the value that the letter is associated with in the dictionary

                    scrambled_pass.append(scrambled_letter) #add it to the encrypted password list 

                if letter not in encryption.keys(): #if letter is not in our dictionary (catch all)
                    scrambled_pass.append(letter) #just add that letter to the scrambled password

            encrypted_pass = "".join(scrambled_pass) #join the password together to make it coherent 

            passwords[account] = [username, encrypted_pass] #the new password ky value pair is created, using lists so we can index rather than nested dict 

            password = None #clear password variable so it is inaccessible
            
            start = input("Enter [n] to quit, [] to add new: ") #allow user to continue

    elif start == "2": #retrieve password 
        retrieve = input("Enter account to retrieve password: ") #what account do they want to get?
        
        retrieved_acc = passwords[retrieve] #access the key of the account they want to retrieve in the passwords dict 
        retrieved_user = retrieved_acc[0] #since we used lists, pos0 is the username
        retrieved_pass = retrieved_acc[1] #pos1 is the scrambled password

        split_retrieved_pass = [] #create empty list to populate

        for i in retrieved_pass:
            split_retrieved_pass.append(i) #split the retrieveed scrambled password into letters 

        unscrambled_pass = [] #create a list for our decrypted password 
        
        for character in split_retrieved_pass: #for every character in the scrambled password 
            if character in decryption.keys(): #if that character is in the decryption dict 
                unscrambled_char = decryption[character] 

                unscrambled_pass.append(unscrambled_char) #append the unscarmbled character

            if character not in decryption.keys(): #if we didnt originally account for that character
                unscrambled_pass.append(character) #just add that character onto the unscrambled password since we never scrambled it

        decrypted_pass = "".join(unscrambled_pass) #put the now decrypteed password together 
        
        #print it all back to user 
        print(f"""{retrieve}: 
        Username: {retrieved_user}
        Password: {decrypted_pass}
        """)

    elif start == "3": #update password 
        update = input("Enter account to update password: ") #enter key we will be accessing 

        updated_user = input("Update username (retype if same): ") #allow them to update the username if necessary 
        updated_pass = input("Update password: ") #what is the new password 

        updated_pass_letters = [] #empty list to populate

        for i in updated_pass:
            updated_pass_letters.append(i) #turn string into list to be able to work with letters

        new_scrambled_pass = [] #now to scramble it, need an empty list 

        for symbol in updated_pass_letters: #for every character in the new entered password 
            if symbol in encryption.keys(): #if that character is in the encryption keys 
                new_scrambled_symbol = encryption[symbol] #get what its encrypted version is 

                new_scrambled_pass.append(new_scrambled_symbol) #add it to the encypted password list

            if symbol not in encryption.keys(): #if we arent accounting for that characte r
                new_scrambled_pass.append(symbol) #just add the original letter on 

        updated_encrypted_pass = "".join(new_scrambled_pass) #join it all together 

        passwords[update] = [updated_user, updated_encrypted_pass] #store it in the key accessed 

    elif start == "4": #list stored accounts 
        print("Accounts stored with us:")

        for account in passwords.keys(): #just list through keys stored 
            print(f"\t{account}")

    elif start == "5": #allow user to quit
        print("Thank you for using the Bytewerks Password Manager.")

        break



    
