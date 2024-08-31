#1)This is a simple text based Rock-paper-scissor game

import random
r=random.randint(0,3)
#print(r)--> it will print the number taken by the computer
l=['Rock','Paper','Scissor']
while True:
    print('_'*45)
    for i in range(0,len(l)):
        print(f'Enter {i+1}:',l[i])
    print(' ')
    
    ch=int(input('Enter your choice:'))
    print('You: ',l[ch-1])
    print('Computer:',l[r])

    print(' ')
    
    if l[ch-1]==l[r]:
        print('ohh! It is draw')
    elif l[ch-1]=='Scissor' and l[r]=='Paper':
        print('Hayy you won!!!!...')
    elif l[ch-1]=='Rock' and l[r]=='Scissor':
        print('Hayy,nice you won again!!!!...')
    elif l[ch-1]=='Paper' and l[r]=='Rock':
        print('nice you won again keep it up!!!!...')
    else:
        print('You loss the round')
        
     # Logic for Infinite loop   
    a=input('Do you want to play (y/n):')
    if a.lower()=='y': #a.lower() convert any uppercase letter into lowercase
        continue
    else:
        print('Thanks for playing')
        break

