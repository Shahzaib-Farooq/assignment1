def car():
    print("*****Welcome to Car Suggestion*******")
    name=input("Dear customer please enter your name: ")
    bud=int(input("How much budget do you have? "))
    if bud>=1000000:
        print("Dear",name,"you can buy following cars in this budget: \n1.BMW \n2.Land Cruiser \n3.Mercedes")
    elif 500000<=bud<1000000:
        print("Dear",name,"you can buy following cars in this budget: \n1.Corolla \n2.Civic \n3.Toyota Corolla")
    elif 300000<=bud<500000:
        print("Dear",name,"you can buy following cars in this budget: \n1.Mehran \n2.Suzuki \n3.Alto")

def loan():
    print("*****Welcome to Loan Suggestion*******")
    name=input("Dear customer please enter your name: ")
    loa=int(input("How much loan you want? "))
    inc=int(input("Please enter your monthly income:"))
    if loa>=500000 and inc>=50000:
        print("Dear",name,"you can get the desired amount of loan which is",loa)
    elif 200000<=loa<500000 and 20000<=inc<50000:
        print("Dear",name,"you can get the desired amount of loan which is",loa)
    elif 30000<=loa<200000 and 10000<=inc<20000:
        print("Dear",name,"you can get the desired amount of loan which is",loa)
    else:
        print("Sorry! Dear",name,"You are not eligible for loan")
        
def reg():
    print("******Welcome to the navtacc portal*******")
    name=input("Dear candidate please  enter your name: ")
    Fname=input("Please  enter your father name: ")
    phone=int(input("Please enter your phone number: "))
    email=input("Please enter your email address here: ")
    password=input("Please enter password: ")
    if name=="" or email=="" or password=="":
        print("Dear",name,"please fill the required fields")
    else:
        print("Dear",name,"your account created successfully!")
        
def pets():
    print("******Welcome to the Pet Suggestion*******")
    name=input("Please enter your name: ")
    cat=int(input("Please select the pet you want to buy: \n1.Cat \n2.Dog \n3.Fish: \n"))
    if cat==1:
        print("***Welcome to Cat Suggestion***")
        print("Dear",name,"you can buy cat")
    elif cat==2:
        print("***Welcome to Dog Suggestion***")
        typ=int(input("You want Big or Small Dog: \n1.Big \n2.Small: \n"))
        if typ==1:
            print("Dear",name,"you can buy Big dog")
        elif  typ==2:
            print("Dear",name,"you can buy Small dog")
    elif cat==3:
        print("***Welcome to Fish Suggestion***")
        print("Dear",name,"you can buy fishes here: \n1.Betta Fish \n2.Gold Fish \n3.Guppies \n4.Neon Tetras")
        
def table():
    while True:
        tab=int(input("Enter table number you want to print: "))
        for i in range(1,11):
            print(tab,"x",i,"=",(tab*i))
        else:
            rerun=input("Do you want to print another table: (yes/no)")
            if rerun=="yes":
                continue
            elif rerun=="no":
                print("Ok thanks!")
                break
            
def tour():
    print("***Welome to tour suggestion***")
    name=input("Please enter your name: ")
    while True:
        visit=int(input("What you like? \n1.Valleys \n2.Mountains \n3.Hills \n4.River \n"))
        if visit==1:
            print("Dear",name,"you can visit these attractive valleys in Pakistan: \n1.Hunza Valley \n2.Swat Valley \n3.Skardu Valley")
        elif visit==2:
            print("Dear",name,"you can visit these attractive mountains in Pakistan: \n1.K2 mountain \n2.Nanga Parbat \n3.Rakaposhi")
        elif visit==3:
            print("Dear",name,"you can visit these attractive Hills in Pakistan: \n1.Murree Hills \n2.Nathia gali \n3.Ayubia National Park")
        elif visit==4:
            print("Dear",name,"you can visit these beautiful rivers in Pakistan: \n1.Indus River \n2.Jhelum River \n3.Barmula River")
        
        rerun=input("Do you want to rerun the program? (yes/no)")
        if rerun=="yes":
            continue
        elif rerun=="no":
            print("Ok thanks!")
            break
         
