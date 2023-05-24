import urllib.request as urllib

   
def Site_Connectivity_Checker():
    print("-----Welcome To The Site Connectivity Checker-----")
    print(" ")
    input_url = input("Enter The URL Of The Site: ")
    print(" ")
    print("Checking Connectivity......")
    
    response = urllib.urlopen(input_url)
    print(" ")
    print("Connected To",input_url,"Succesfully")
    print(" ")
    print("The Response Code Was: ",response.getcode())



Site_Connectivity_Checker()
    
    