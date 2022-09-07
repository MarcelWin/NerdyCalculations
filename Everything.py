DoingNerdStuff = True;

while DoingNerdStuff:
    #Type 1,2,3 or 4 or else it won't work
    Options = int(input('Decimal to hex(1), Decimal to binary(2), Hex to Decimal(3), Binary to Decimal(4): '))
    if Options==1: #Decimal to hex
        Number = int(input('Enter the number big nerd: '))
        print('The answer is',hex(Number)[2:])
        OneMoreTime = input('Do you want to calculate something else?: ')
        if(OneMoreTime=='Yes'or OneMoreTime=='yes'):
            continue
        else:
            break
    if Options==2: #Decimal to binary
        Number = int(input('Enter the number big nerd: '))
        print('The answer is',bin(Number)[2:])
        OneMoreTime = input('Do you want to calculate something else?: ')
        if(OneMoreTime=='Yes'or OneMoreTime=='yes'):
            continue
        else:
            break
    if Options==3: #Hex to Decimal
        Number = (input('Enter the hex value big nerd: '))
        print('The answer is',int(Number, 16))
        OneMoreTime = input('Do you want to calculate something else?: ')
        if(OneMoreTime=='Yes'or OneMoreTime=='yes'):
            continue
        else:
            break
    if Options==4: #Binary to Decimal
        Number = (input('Enter the binary value big nerd: '))
        print('The answer is',int(Number, 2))
        OneMoreTime = input('Do you want to calculate something else?: ')
        if(OneMoreTime=='Yes'or OneMoreTime=='yes'):
            continue
        else:
            break
    else:
        break