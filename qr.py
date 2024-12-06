import qrcode as qr
url = input("enter the url :- ")
img = qr.make(url)
img.save("number.png")
