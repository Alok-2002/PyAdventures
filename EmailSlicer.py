def Email_Slicer():
    
    print("--------------Welcome To The Email Slicer---------------")
    print(" ")
    print(" ")
    
    email_input = input("Enter Your Email: ")
    print(" ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Your Username Is:",username)
    print(" ")
    print("Your Email Domain Is:",domain)
    print(" ")
    print("Your Email Extension Is:",extension)
    
Email_Slicer()