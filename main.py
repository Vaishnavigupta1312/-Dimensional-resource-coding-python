import qrcode
from barcode import Code128

print("\n__________________________________________________"
      "WELCOME TO DIMENSIONAL RESORURCE CODING PLATFORM"
      "____________________________________________________\n")
print("\nHere you can transform your resource links, text phrases, phone numbers, passwords"
      " in the form of dimensional codes i.e.QR Code and Bar Code")
def barcode_maker():

    data = input("Enter the alphanumeric data to transform into Bar Code"
                 "       (Can share your wifi passwords or mobile numbers)\n")
    code = Code128(data)
    # code == barcode.get('code39', data, writer=ImageWriter())
    code.save('barcode')


def qrcode_maker():
    qr = qrcode.QRCode(version=1, box_size=15, border=15)
    data = input("Enter the text or link you want to transform into QR Code:\n")
    qr.add_data(data)
    # color = inputdede("Enter the color you wish to see you QRCode in ")

    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('Linked-QR-Code.png')


def main():
    print('''
    What you would like to generate???
    1 -> Barcode
    2 -> QR code
    3 -> Quitb
    ''')
    choice = None
    while choice == None:
        try:
            choice = int(
                input("Enter your choice (1,2 or 3) : "))
        except:
            # To catch error in case the user enters a char instead of int
            print("Enter an integer.")

    if choice == 1:
        barcode_maker()
    elif choice == 2:
        qrcode_maker()
    elif choice == 3:
        quit()    
    else:
        print("Invalid Choice")

main()