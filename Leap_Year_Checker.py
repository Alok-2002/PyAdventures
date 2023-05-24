def Leap_Year():
    print("-----Welcome To The Leap Year Checker-----")
    year = int(input("Enter The Year To Check: "))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year,"Is A Leap Year.")
            else:
                print(year,"Is Not A Leap Year.")
        else:
            print(year,"Is A Leap Year.")
    else:
        print(year,"Is Not A Leap Year.")
        
Leap_Year()