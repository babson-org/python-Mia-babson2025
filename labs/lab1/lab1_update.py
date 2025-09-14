def draw_diamond():       #defining function
    prompt = "Enter an odd number for the diamond height: "
    while True:                                   #looping until valid odd integer inputed
        try:
            odd_num = int(input(prompt))
            if odd_num % 2 == 0:
                print("Enter an odd integer please")
            else:
                break
        except ValueError:
            txtb = 'An odd integer for my kingdom'
            print(txtb)
    top_half = (odd_num // 2)+1   #includes rows in top half and middle line
    for i in range(top_half):
        stars = 2 * i + 1                #calc for number of stars in each row
        spaces = (odd_num - stars) // 2     #centers the diamond with decreasing spaces
        print(" " * spaces + "*" * stars)
    bottom_half = top_half-1           #includes rows in bottom half and excludes middle line
    for i in range (bottom_half -1, -1, -1):     #builds bottom half in reverse
         stars = 2 * i + 1                
         spaces = (odd_num - stars) // 2     
         print(" " * spaces + "*" * stars)
        

def text_analysis():                            #defining function
    block = input("Enter a block of text: ")
    words = len(block.split())           #splits text into words then counts words with len()
    print("# of Words:", words)
    letter_count = 0
    for char in block:                #iterates over every character in block
        if char.isalpha():             #checks if character is a-z or A-Z (letters)
            letter_count = letter_count + 1       #counts number of characters that are letters
    print("# of Letters:", letter_count)
    punctuation = ('.', '!', '?')          #list of punctuation that goes at end of a sentence
    sentence_count = 0
    for char in block:                   #iterates over every character in block
            if char in punctuation:      #checks if character is ending punctuation
                sentence_count = sentence_count + 1   #increments setence count
    print("# of Sentences:", sentence_count)

    
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


def main():           #placed last because functions are defined above
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":            
            draw_diamond()             #calling diamond function defined above
        elif choice == "2":            
            text_analysis()            #calling text analysis function defined above
        elif choice == "3":             
            caesar_cipher()            #calling caesar cipher function defined above
        else:
            exit()
main()                     #calling main function

if __name__ == "__main__":   #main function only runs when this file is executed directly
    main()
