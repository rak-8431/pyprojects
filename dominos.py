import sqlite3
conn=sqlite3.connect('dom.db')
b=conn.cursor()
#b.execute('create table Domuser(name char,phno number,email char)')
#b.execute('create table cart(phno number,cartvalues char)')

d={
    'veg':{'Margerita':129,'chese_and_corn':169,'peppi_paneer':260,'veg_loaded':210,'Tomato_tangi':170},
    'non_veg':{'pepper_barbeque':199,'non_veg_loaded':169,'chicken_sausage':200},
    'snacks':{'garlic_braed':120,'zingy':59,'c_cheese_balls':170},
    'desserts':{'choco_lava':100,'mousse_cake':169},
    'drinks':{'coke':90,'pepsi':78,'sprite':50}

}

login_status=False
cart={}
pnum=''
mode=0

def valid_phno(phno):
    s=str(phno)
    return len(s)==10 and '6'<=s[0]<='9' and s.isnumeric()

def check_phno(phno):
    l=list(b.execute('select phno from Domuser'))
    return(phno,) in l

def valid_email(e):
    s=e[-10:]
    return s in ['@gmail.com','@yahoo.com']  and 'a'<=e[0]<='z' and e[0:-10].isalnum()

def check_email(e):
    l=list(b.execute('select email from Domuser'))
    return(e,) in l # the values inside the database are stored in the form of tuple

def Dominos():
    print('Enter 1: signup')
    print('Enter 2: login')

    ch=int(input('Enter your choice: '))
    if ch==1:
        while True:
            print('Please fill details')
            name=input('Enter your name: ')
            while True:
                phno=int(input('Enter your phno: '))
                if valid_phno(phno):
                    break
                else:
                    print('Invalid phno')

            while True:
                email=input('Enter your email: ')
                if valid_email(email):
                    break
                else:
                    print('Invalid email')

            m,n=check_email(email),check_phno(phno)
            if m==False and n==False:
                b.execute(f'insert into Domuser values("{name}","{phno}","{email}")')
                conn.commit()
                print('Signup successful')
                break
            elif m==True:
                print('Email already Exists')
            else:
                print('phno already Exists')
    else: 
        login()

def get_otp(a):
    global login_status
    import random 
    while True:
        otp=random.randint(100000,999999)
        print('Your otp is: ',otp)
        print('An otp has been sent to your ',a)
        tp=int(input('Enter otp:'))
        if tp==otp:
            print('Logged in successfully')
            login_status=True
            break
        else:
            print('Incorrect otp')

def login():
    global pnum,login_status
    if login_status==True:
        return 'Already logged in'
    print('Enter 1: login with phno')
    print('Enter 2: login with email')
    c=int(input('Enter your choice: '))
    if c==1:
        pnum=int(input('Enter phno: '))
        if check_phno(pnum):
            get_otp(pnum)
        else:
            print('phno doesnot exist')
    else:
        email=input('Enter email: ')
        pnum=list(b.execute(f'select phno from Domuser where email="{email}"'))[0][0] #indexing like  i[0][0]
        if check_email(email):
            get_otp(email)
        else:
            print('Email doesnot exists')

def log_out():
    global login_status
    login_status=False
    print('Logged out successfully')

def order(new=0):
    global mode
    if login_status==True:
        print('Enter 1: Dine in')
        print('Enter 2: Take away')
        print('Enter 3: Home Delivery')
        ch=int(input('Enter your choice: '))
        mode=ch
        out={}
        di=list(d) # here d contains['veg','nonveg','desserts']
        while True:
            print('Enter 1: Veg')
            print('Enter 2: Non-Veg')
            print('Enter 3: Snacks')
            print('Enter 4: Desserts')
            print('Enter 5: Drinks')
            print('Enter 6: End')
            c=int(input('Enter your item: '))
            if 1<=c<=6:
                if c==6:
                    break
                m=list(d)[c-1] # here enter 1 for veg but veg present in the index of 0,so we take c-1 to get the index of the enterd value
                m=list(d[m])  # ['Margerita','peppi_panner',...]
                for i in range(1,len(m)+1):
                    print(f'Enter {i}: {m[i-1]}')

                choice=int(input('Enter choice: '))
                q=int(input('Enter quantity: '))
                if 1<=choice<=len(m):
                    out[m[choice-1]]=[q,q*d[di[c-1]][m[choice-1]]]
                    print('Item added')
                else:
                    print('Invalid choice')
            else:
                print('Invalid Choice')
        cart.update(out)
        if cart!={} and new==0:
            b.execute(f'insert into cart values("{pnum}","{cart}")')
            conn.commit()
    else:
        print('Login is required')

def disp_bill():
    if login_status==True:
        if mode==1:
            total_amt=0
        elif mode==2:
            print('Parcel charges of 25Rs. will be included')
            total_amt=25
        elif mode==3:
            print('parcel charges of 25Rs and Delivery charges of 50Rs will be charged ')
            total_amt=75
        print('Item',' '*11,'Quantity','Price')
        for i in cart:
            print(i,' '*(20-len(i)),cart[i][0],cart[i][1])
            total_amt+=cart[i][1]

        print('Total Bill:',' '*20,total_amt)
    else:
        print('login is required')

# Steps to run the programm
# go to the required folder,preess ctrl+L and type cmd and enterIt directed to the command prompt where enter (code(space).)  
# 1)py
# 2)from dominos import *
# 3)Dominos()

# for atm,dominoss programs