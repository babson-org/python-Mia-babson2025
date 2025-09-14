def draw_diamond():       #defining function
    prompt = "Enter an odd number for the diamond height: "
    while True:                                   #to avoid break if user inputs text or even int
        try:
            oddnum = int(input(prompt))
            if oddnum % 2 == 0:
                print("Enter an odd integer please")
            else:
                break
        except ValueError:
            txtb = 'An odd integer for my kingdom'
            print(txtb)
    tophalf = (oddnum // 2)+1   # round down and +1 includes middle line
    for i in range(tophalf):
        stars = 2 * i + 1                #gives symmetrical increasing amount of stars
        spaces = (oddnum - stars) // 2     #centers the diamond with decreasing spaces
        print(" " * spaces + "*" * stars)
    bottomhalf = tophalf-1     #excludes middle
    for i in range (bottomhalf-1, -1, -1):
         stars = 2 * i + 1                
         spaces = (oddnum - stars) // 2     
         print(" " * spaces + "*" * stars)
        
draw_diamond()        