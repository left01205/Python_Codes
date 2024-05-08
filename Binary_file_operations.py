#Search
def search():
    e= input("Enter field to be serached [NAME,CLASS,SEC,AGE] ->")
    k=input("Enter char ->")
    
    while True:
        try:
            s=pickle.load(f)
            if s[e]==k:
                print(s,"Data found in file...")
        
        except EOFError:
            break
#Replace
def rep():
    while True:
        try:
            s=pickle.load(f)
            print(s,"\n","Change required?[y/n]...")
            u=input()
            if u.lower()==y:
                e= input("Enter field to be changed [Name,Class,Section,Age](be case sensetive...) ->")
                k=input("Enter change  ->")
                d[e]=k
                pickle.dump(d,f)
                
        except EOFError:
            print("Ran out of data...")
            break
#Adding new entries
def add():
    while True:
        d={}
        n=input("Enter name ->")
        c=int(input("Enter class ->"))
        s=input("Enter section ->")
        a=int(input("Enter age ->"))
        d['Name']=n
        d['Class']=c
        d['Section']=s
        d['Age']=a
        pickle.dump(d,f)
        r=input("Do you want to contnue [y/n]")
        if r.lower() == 'n':
                break
#Reading entries 
def read():
    while True:
        try:
            s=pickle.load(f)
            print(s)
        except EOFError:
            print("Ran out of data...")
            break
    
#Main
f=open("Bintrash.dat","ab+")

while True:
    print("1.Search \n 2.Replace \n 3.Adding new entries \n 4.Read entries \n 5.Exit")
    o=input()
    if o=='1':
        search()
    elif o=='2':
        rep()
    elif o=='3':
        add()
    elif o=='4':
        read()
    elif o=='5':
        print('Thanks for using our service...')
        f.close()
        break
    else:
        print("Wrong input")
