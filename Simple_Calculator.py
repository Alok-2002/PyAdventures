def Simple_Calculator():
    flag = True
    while flag:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("6.Exponential")
        print("7.Floor Division")
        print("8.EXIT")
        
        User_Choice = int(input("Select The Operation You Want To Perfrom: "))
        
        if User_Choice == 1:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Addition Result Is:",(num1+num2))
            
        elif User_Choice == 2:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Subtraction Result Is:",(num1-num2))
        
        elif User_Choice == 3:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Multiplication Result Is:",(num1*num2))
        
        elif User_Choice == 4:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Division Result Is:",(num1/num2))
        
        elif User_Choice == 5:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Modulus Result Is:",(num1%num2))
        
        elif User_Choice == 6:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Exponential Result Is:",(num1**num2))
        
        elif User_Choice == 7:
            num1 = int(input("Enter The First Number: "))
            num2 = int(input("Enter The Second Number: "))
            print("The Floor Division Result Is:",(num1/num2))
        
        elif User_Choice == 8:
            print("Exiting...........")
            flag = False
        
        else:
            print("Invalid Choice..........")
            flag = False

        
Simple_Calculator()