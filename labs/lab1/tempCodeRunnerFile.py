def caesar_cipher():                          #defining function
    text = input("Enter text:")
    length = len(text)                        #number of characters in the text
    shifted_text = [None] * length            #empty list for shifted characters
    
    txt = "Enter shift value (integer): "
    while True:                              #loops until user inputs valid integer
        try:
            shift = int(input(txt))
            break
        except ValueError:
            txtm = 'A number for my kingdom'
            print(txtm)
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    for i, char in enumerate(text):  #each character and its position
        if char.isalpha():
            first_letter = ord('A') if char.isupper() else ord('a') #ASCII code
            shifted_char = chr((ord(char) - first_letter + shift) % 26 + first_letter)
            shifted_text[i] = shifted_char 
        else:
            shifted_text[i] = char        #keeps non-letters the same
    result = "".join(shifted_text)        #joins list into a string
    if choice == "e":           
        print("Encrypted message:", result)    
    elif choice == "d":
        print("Decrypted message:", text)          #decryption shows the original text
caesar_cipher()