def caesar_cipher():                          #defining function
    alphabet = []
    for idx in range(26):
        letter = chr(idx+97) #ASCII code for 'a'
        alphabet.append(letter)

    text = input("Enter text:")
    length = len(text)                        #number of characters in the text
    shifted_text = [None] * length            #empty list for shifted characters
    
    txt = "Enter shift value (integer) between 1-25: "
    while True:                       #loops until user inputs valid integer (1-25)
        try:
            shift = int(input(txt))
            if 1<= shift <=  25:
                break
            else:
                print("Shift must be between 1 and 25")
        except ValueError:
            txtm = 'A number for my kingdom'
            print(txtm)

    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    for i, char in enumerate(text):  #each character and its position
        char_lower = char.lower()    #converts character to lowercase
        if char_lower in alphabet:
            index = alphabet.index(char_lower)   #identify the index of character
            shifted_index = (index + shift) % 26   #apply shift with wrap around
            shifted_char = alphabet[shifted_index]
            shifted_text[i] = shifted_char      
        else:
            shifted_text[i] = char        #keeps non-letters the same
    result = "".join(shifted_text)        #joins list into a string
   
    if choice == "e":           
        print("Encrypted message:", result)   
    elif choice == "d":             #decryption shows the original text
        print("Decrypted message:", text) 
    else:
        print("Invalid choice, choose either 'e' or 'd'")
caesar_cipher()   