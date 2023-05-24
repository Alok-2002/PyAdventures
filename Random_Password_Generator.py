import random
import string

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    
    password_length = int(input("How Long You Want Your Password To Be ?: "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = " ".join(password)
    
    print(password)
    
    
def Random_Password_Generator():
        
    flag = True
    
    while flag:
        print("-----Welcome To The Random Generator-----")
    
        choice = input('''Do You Want To Generate A Password ?
                    1.Type Y Or Yes To Generate A Password.
                    2.Type N Or No To Exit..... ''').lower()
        if choice == "y" or choice == "yes":
            generate_password()
        elif choice == "n" or choice == "no":
            print("Exiting......")
            break            
        else:
            print("Invalid Input.............Please Try Again With Yes Or No.....")
            break


Random_Password_Generator()