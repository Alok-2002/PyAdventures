import qrcode

def generate_qr_code():
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4, 
    )
    
    text = input("Enter The Text Or Paste Link To Create The QR Code: ")
    # text = "https://www.google.com"
    
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color = '#9b59b6', back_color = 'white')
    filename = input("Enter File Name with extension of the image: ")
    img.save(filename)
    # img.save("1.png")


print("-----Welcome To QR Code Generator------")
print(" ")
print(" ")




generate_qr_code()
