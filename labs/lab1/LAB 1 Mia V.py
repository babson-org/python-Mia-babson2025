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

def draw_diamond():
    
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
    if choice == "e":
        for idx in range(length):
            new_idx = (idx + shift) % length
            shifted_text[new_idx] = text[idx]
        print("".join(shifted_text))               #joins letters together into words
    if choice == "d":
        print(text)
caesar_cipher()                              #calling function
