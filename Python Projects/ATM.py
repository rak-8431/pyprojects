pin=0
bal=0
def set_pin():
    global pin 
    pin1=(int(input('Enter a 4 digit pin:')))
    pin2=(int(input('Confirm your pin:')))
    if pin1==pin2:
        print('Pin set successful')
        pin=pin1
    else:
        print('Pin doesnot match....enter correct pin')

def deposit():
    global bal
    in_pin=int(input('Enter 4 digit pin: '))
    if in_pin==pin:
        amt=int(input('Enter amount: '))
        bal+=amt
        print(f'Amount of {amt} Rs. Deposited Successfully')
    else:
        print('Incorrect Pin')


def checkbal():
    while True:
        inpin=int(input('Enter 4 digit pin:'))
        if inpin==pin:
            print("Your Available Balance is:",bal)
            break
        else:
            print("Pin Inccoreect....Retry")



def withdraw():
    global bal
    in_pin=int(input('Enter 4-digit pin:'))
    if in_pin==pin:
        amt=int(input('Enter amount: '))
        if amt<=bal:
             bal-=amt
             print(f'Amount of{amt} Rs.withdraw successfully')
        else:
            print('Insufficient balance')
    else:
        print('Incorrect Pin')


while True:
    print('_'*45)
    print('Enter 1: To set pin')
    print('Enter 2: To Deposit')
    print('Enter 3: To Withdraw')
    print('Enter 4: To check balance')
    print('Enter 5:To Exit')
    print(' ')
    ch=int(input('Enter your choice: '))
    print(' ')
    if ch==1:
        set_pin()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        checkbal()
    elif ch==5:
        print('Thank You!!!')
        break
    else:
        print('Invalid Choice')

    print(' ')
    a=input('Do you want to continue?(y/n)')
    if a.lower()=='y':
        continue
    else:
        print('Thank You!!!')
        break










