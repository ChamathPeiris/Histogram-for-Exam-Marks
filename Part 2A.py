def encoder(code,shift_key):
    new_code=''
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for cha in range(len(code)):
        index = code[cha]
        if index in alphabet:
          present_condition=alphabet.find(index)
          new_condition=(present_condition+shift_key) % 26
          new=alphabet[new_condition]
          new_code = new_code + new
        else:
            new_code = new_code+index
    return new_code
code=input("Enter the message:")
while True:
    shift_key=int(input("Enter the key:"))
    if shift_key>0 and shift_key<26:
            encrypted_code=encoder(code,shift_key)
            print('Secret messege: {}'.format(encrypted_code))
            break
    else:
        print("Invalid key entered, try again.")
