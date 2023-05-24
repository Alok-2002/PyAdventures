from PIL import Image

def Resized_Image():
    
    # image = Image.open('./me.jpg')
    
    filepath = input("Enter The Name Of The File : ")
    
    image = Image.open(filepath)
    
    print(f"Current Size :{image.size}")
    
    x_size = int(input("Enter The Width In Pixels : "))
    
    y_size = int(input("Enter The Height In Pixels : "))

    resized_image = image.resize((x_size, y_size))

    # resized_image.save('me2.jpg')
    
    filename = input("Enter The FileName For Your Resized Image : ")
    
    resized_image.save(filename)

def Image_Resizer():
    flag = True
    while flag:
        print(" ")
        print("----------Welcome To The image Resizer-------------")
        print(" ")
        print(" ")
        print("-----Want To Resize The Image : ")
        user_input = input('''Enter Y To Resize Image
Enter E To Exit ''').lower()
        if user_input == 'y':
            Resized_Image()
        else:
            print("Exiting.........")
            break
            
Image_Resizer()