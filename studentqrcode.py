import qrcode
a =int(input("enter how many students data you want to enter and generate qr code:"))
for i in range(0,a,1):
     data=str(input("enter student details:"))
     img= qrcode.make(data)
     img.save(data+".jpg")