def Password(): 
      
    capital_letters = 0
    small_letters = 0
    symbols = 0
    numbers = 0
    strength = 0
    
    Password = input("Enter your password: ")
    
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    smallalphabets="abcdefghijklmnopqrstuvwxyz"

    specialcharacters="$@_%&#"

    digits="0123456789"
    
    if (len(Password) >= 8):
        
        for i in Password:
             
            if (i in smallalphabets):
                small_letters += 1	
                strength += 1
                	
            if (i in capitalalphabets):
                capital_letters += 1	
                strength += 1	
             
            if (i in digits):
                numbers += 1	
                strength += 1
            
            if(i in specialcharacters):
                symbols += 1	
                strength += 1
                
    if (small_letters >= 1 and capital_letters >= 1 and numbers >= 1 and symbols >= 1 and small_letters + capital_letters + numbers + symbols == len(Password)):
         
        print("Your Password Strength is :",strength)
        
        #to know how many capital letters are in the password
        # print("There Are",capital_letters,"Capital Letters In Your Password")
        
        #to know how many small letters are in the password
        # print("There Are",small_letters,"Small Letters In Your Password")
        
        #to know how many number are in the password
        # print("There Are",numbers,"Numbers In Your Password")
        
        #to know how many symbol are in the password
        # print("There Are",symbols,"Symbols In Your Password")
        
    else:
        
        print("Your Password Is Not Strong Enough")
        
        


def Password_Strength_Checker():

    flag = True
    
    while flag:
        
        print(" ")
        print("----------Welcome To The Password Strength Checker-------------")
        print(" ")
        print(" ")
        print("-----Do You Want To Check Your Password Strength: ")
        
        user_input = input('''Enter Y To Check Password
Enter E To Exit ''').lower()
        
        if user_input == 'y':
            
            Password()
            
        else:
            
            print("Exiting.........")
            
            break
            
Password_Strength_Checker()