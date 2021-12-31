import qrcode

# data example
data = "www.google.com"

# file name
file_name = "qrcode.png"

# generate qr code
img = qrcode.make(data=data)

# save generated qr code as img

img.save(file_name)
