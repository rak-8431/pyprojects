def get_in():
    a=int(input('Enter val1: '))
    b=int(input('Enter val2:'))

    print(' ')
    return a,b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def true_div(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def mod(a,b):
    return a%b
def power(a,b):
    return a**b
def sqrt():
    a=int(input('Enter the number: '))
    return a**0.5
def fact():
    a=int(input('Enter the number: '))
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
    

while True:
    print('_'*45)
    print('Enter 1: Addition')
    print('Enter 2: Subtraction')
    print('Enter 3: Multiplication')
    print('Enter 4: True Division')
    print('Enter 5: Floor Division')
    print('Enter 6: Modulus')
    print('Enter 7: Power ')
    print('Enter 8: Square Root ')
    print('Enter 9: Factorial ')
    print('Enter 10: To Exit ')
    ch=int(input('Enter your choice: '))
    print(' ')

    if ch==1:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The sum is:',add(m,n))

    elif ch==2:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The Differnce is:',sub(m,n))

    elif ch==3:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The Product is:',mul(m,n))

    elif ch==4:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The Quotient is:',true_div(m,n))

    elif ch==5:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The Quotient is:',floor_div(m,n))

    elif ch==6:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The Remainder is:',mod(m,n))

    elif ch==7:
        m,n=get_in() #m,n store the value inside the get_in 
        print('The power is:',power(m,n))

    elif ch==8:
        print('The root is:',int(sqrt( )))

    elif ch==9:
        print('The factorial of a number is',fact())

    elif ch==10:
        print('Thank you for using calculator')
        break

    else:
        print('Invalid Choice')

    print(' ')

    a=input('Do you want to continue (y/n): ')
    if a.lower()=='y':
        continue
    else:
        print('Thank You for using the calculator ')
        break
