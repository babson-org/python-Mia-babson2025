def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()
main()

def draw_diamond():       #defining function
    prompt = "Enter an odd number for the diamond height: "
    while True:                                   #looping until valid odd integer inputed
        try:
            oddnum = int(input(prompt))
            if oddnum % 2 == 0:
                print("Enter an odd integer please")
            else:
                break
        except ValueError:
            txtb = 'An odd integer for my kingdom'
            print(txtb)
    tophalf = (oddnum // 2)+1   #includes rows in top half and middle line
    for i in range(tophalf):
        stars = 2 * i + 1                #calc for number of stars in each row
        spaces = (oddnum - stars) // 2     #centers the diamond with decreasing spaces
        print(" " * spaces + "*" * stars)
    bottomhalf = tophalf-1     #includes rows in bottom half and excludes middle line
    for i in range (bottomhalf -1, -1, -1):     #builds bottom half in reverse
         stars = 2 * i + 1                
         spaces = (oddnum - stars) // 2     
         print(" " * spaces + "*" * stars)
        
draw_diamond()               #calling function

def text_analysis():
    
def caesar_cipher():                          #defining function
    text = input("Enter text:")
    length = len(text)                       
    shifted_text = [None] * length  
    
    txt = "Enter shift value (integer): "
    while True:                              #to avoid break if user inputs text
        try:
            shift = int(input(txt))
            break
        except ValueError:
            txtm = 'A number for my kingdom'
            print(txtm)
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()      
    if choice == "e":                              #performing the shift
        for idx in range(length):
            new_idx = (idx + shift) % length       #new position, makes shift wrap around
            shifted_text[new_idx] = text[idx]
        result = "".join(shifted_text)             #joins letters together into words
        print("Encrypted message:", result)             
    if choice == "d":
        print("Decrypted message:", text)
        
caesar_cipher()                              #calling function
