def encoder(code,shift_key): #encode the message
    new_code=''
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for cha in range(len(code)):
        index = code[cha]
        if index in alphabet:#position
          present_condition=alphabet.find(index)
          new_condition=(present_condition+shift_key) % 26
          new=alphabet[new_condition]
          new_code = new_code + new
        else:
            new_code = new_code+index
    return new_code#update the code

def decoder(code,shift_key): #decode the message
    new_code=''
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for cha in range(len(code)):
        index = code[cha]
        if index in alphabet:#position
          present_condition=alphabet.find(index)
          new_condition=(present_condition-shift_key) % 26
          new=alphabet[new_condition]
          new_code = new_code + new
        else:
            new_code = new_code+index
    return new_code

def show_help():
    print("***To encode the message press 'e'***")
    print("***To decode the message press 'd'***")
    print("***To quit the process press 'q'***")
    
while True:
    print()
    show_help()
    process=input("What do you want to do:")
    if process.lower()=='e':
        code=input("Enter the message:")
        while True:
            shift_key=int(input("Enter the key:"))
            if shift_key>0 and shift_key<26:
                encrypted_code=encoder(code,shift_key)#call function
                print('Secret messege: {}'.format(encrypted_code))
                break
            else:
                print("Please enter a value between 0 and 26")                
    elif process.lower()=='d':
        code=input("Enter the message:")
        while True:
            shift_key=int(input("Enter the key:"))
            if shift_key>0 and shift_key<26:
                decrypted_code=decoder(code,shift_key)#call function
                print('Original messege: {}'.format(decrypted_code))
                break
    elif process.lower()=='q':
        break
    else:
        print("Invalid key entered, try again.")
    
print("Process End. Thank you!")


    



        








         
