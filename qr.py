# Importing library
import qrcode
#to get qrcode :<pip install qrcode> in command prompt

# variable that adds link to our qr code
data = "https://resize.indiatvnews.com/en/resize/newbucket/400_-/2023/04/PTI04_03_2023_000319B.jpg"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,box_size = 12,border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'black',back_color = 'white')

img.save('picture.png')
