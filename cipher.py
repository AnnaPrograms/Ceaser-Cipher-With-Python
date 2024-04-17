# grabs user input
message = list(input("Please enter message: ").lower())
shift = int(input("Please enter the shift: "))

for i in range(len(message)):
    
    # skips all the spaces and symbols
    if message[i] != " " and ord(message[i]) > 65:
        
        # if the shift would result in an ASCII number greater than z (which would give back other symbols)
        if (ord(message[i]) + shift) > ord("z"):
            
            # then just determine how much is it over and then add the "over" shift starting at a
            message[i] = chr((ord(message[i]) + shift - ord("z")) + ord("a") - 1)
        else: 
            
            # else just shift the letter down the alphabet
            message[i] = chr(ord(message[i]) + shift)
    else: 
        message[i] = message[i]
        
# puts it all back into a nice string
message = "".join(message)

print(message)
